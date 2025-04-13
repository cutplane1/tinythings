# http://info.cern.ch/hypertext/WWW/TheProject.html

from typing import List, Tuple

# response: str = requests.get("http://example.com").text

class Element:
    def __init__(self, tag: str, attributes: dict = {}, children: List["Element"] = [], parent: "Element" = None):
        self.tag = tag
        self.attributes = attributes
        self.children = children
        self.parent = parent
    
    def add_child(self, child: "Element") -> "Element":
        child.parent = self
        self.children.append(child)

        return child
    
    def level(self) -> int:
        if self.parent is None:
            return 0
        return self.parent.level() + 1
    
    def process(self, closure):
        closure(self)
        if self.children:
            for each in self.children:
                each.process(closure)

    def print_element_tree(self) -> None:
        print('*'*self.level(), end = '')
        if self.tag == "<text_internal>":
            print("<text_internal>" + self.attributes["text"] + "</text_internal>")
        else:
            print(self.tag)
        if self.children:
            for each in self.children:
                each.print_element_tree()


def parse_html(html: str) -> Element:
    """
    shitty implementation of a HTML parser (or rather XML because I assume that in HTML tags are always closed :))
    """
    tag_c = False
    tag_str = ""
    text_str = ""

    root = Element("root", {}, [])

    index: Element = root

    for c in html:
        if c == "<":
            text_str = text_str[1:]
            if text_str:
                index.add_child(Element("<text_internal>", {"text": text_str}, []))
                text_str = ""
            tag_c = True
        elif c == ">":
            tag_str += c
            tag_str = tag_str.replace("\n", " ").lower()
            tag, attributes = parse_html_attributes(tag_str)
            tag = f"<{tag}>"
            if tag_str.count("</") > 0:
                if index:
                    index = index.parent
            else:
                if tag_str in ["<dd>", "<dt>", "<br>"] or tag_str.endswith("/>"):
                    index = index.add_child(Element(tag, attributes, []))
                    index = index.parent
                else:
                    index = index.add_child(Element(tag, attributes, []))
            tag_str = ""
            tag_c = False
        
        if tag_c:
            tag_str += c
        else:
            text_str += c
    text_str = text_str[1:]
    if text_str:
        index.add_child(Element("<text_internal>", {"text": text_str}, []))
        text_str = ""
    root.add_child(Element("<EOT>", {}, []))
    return root

# root.print()
# print(response)

def parse_html_attributes(html: str) -> Tuple[str,dict]:
    html = html.replace(">", "").replace("<", "").split()
    tag = html[0]
    attributes = {}

    if len(html) > 1:
        for attr in html[1:]:
            try:
                key, value = attr.split("=")
                value = value.strip('"\'')
            except ValueError:
                key, value = attr, None
            attributes[key] = value

    return tag, attributes

def str_debug(element: Element):
    if element.tag == "<text_internal>":
        a = element.attributes["text"]
        print("STRING({}, \"{}\", {})".format(len(a), a, a.count("\n")))