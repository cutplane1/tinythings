import parser
import requests

# response: str = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html").text
#response: str = requests.get("http://example.com").text
response = '<h1>Hello, World!</h1><br><a href="https://github.com/cutplane1">my github profile!</a><br>bye!!'
root = parser.parse_html(response)

context = {"is_link": False, "link": None}
def render(e):
    global context

    if e.tag == "<text_internal>":
        print(e.attributes["text"], end="")
        if context:
            print("({})".format(context["link"]), end="") if context["is_link"] else print("", end="")
            print("\033[0m", end="")
            context["is_link"] = False
            context["link"] = None

    if e.tag == "<a>":
        # color ascii text
        print("\033[0;34m", end="")
        context["link"] = e.attributes["href"]
        context["is_link"] = True
    
    if e.tag == "<br>":
        print("\n", end="")


# root.process(parser.str_debug)
root.process(render)