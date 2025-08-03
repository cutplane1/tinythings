import parser
# import requests

# response: str = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html").text
#response: str = requests.get("http://example.com").text
html = '<h1>Hello, World!</h1><br><a href="https://github.com/cutplane1">my github profile!</a><br>bye!!'
root = parser.parse_html(html)

from dataclasses import dataclass
from enum import Enum

class ElemType(Enum):
    H1 = "h1"
    A = "a"
    BR = "br"
    TEXT = "text"
    UNKNOWN = "unknown"


@dataclass
class LayoutObject:
    x: int
    y: int
    type: ElemType = ElemType.UNKNOWN

# def layout(e: parser.Element) -> list[LayoutObject]:
#     coord_stack = 0
#     layout_objects = []

#     def layout_closure(element: parser.Element):
#         global coord_stack
#         global layout_objects
#         if element.tag == "h1":
#             layout_objects.append(LayoutObject(coord_stack, 0, ElemType.H1))
#             # text measuring would go here
#             coord_stack += 20 # assuming
#         elif element.tag == "br":
#             coord_stack += 10
#         elif element.tag == "a":
#             layout_objects.append(LayoutObject(coord_stack, 0))

#     e.process(layout_closure)
#     return layout_objects



print(root)
