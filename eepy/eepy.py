import re
import io
from contextlib import redirect_stdout
from typing import TypeAlias

PythonScript: TypeAlias = str

def parse(template: str, variables: dict = None, escape_html: bool = True, newmodule: bool = True) -> PythonScript:
    code = ""

    if variables is not None:
        for var, value in variables.items():
            code += "{} = {}\n".format(var, repr(value))
    
    if escape_html and "from html import escape" not in template and newmodule:
        code += "from html import escape\n"
    if newmodule:
        code += "buf = ''\n"
    tab_count = 0
    tab_str = "    "
    for i in template.split("\n"):
        if 0 > tab_count:
            raise SyntaxError("too many @end's")
        if i.startswith("@") and not i.startswith("@end") and not i.startswith("@include"):
            expr = i[1:].strip()
            code += expr + "\n"
            if any(o in i for o in ["for", "if", "while", "else", "elif", "try", "except", "finally", "with", "def", "class"]):
                tab_count += 1
        elif i.startswith("@end"):
            tab_count -= 1
        elif i.startswith("@include"):
            filename = i.replace("@include:", "").strip()
            with open(filename) as f:
                aa = f.read()
            code += parse(aa, escape_html=escape_html, newmodule=False) # cooooooool reeeeeeecursion
        elif "{{" in i:
            matches = re.findall(r'{{([^>]+)}}', i)
            if escape_html:
                i = i.replace("{{", "{escape(str(").replace("}}", "))}") 
            else:
                i = i.replace("{{", "{").replace("}}", "}")
            code += tab_str*tab_count + "buf += f'{}'\n".format(i)
        else:
            code += tab_str*tab_count + "buf += '{}\\n'\n".format(i)

    if tab_count != 0:
        raise SyntaxError("some @end's are missing")
    return code


def execute(code: PythonScript) -> str:
    """evals python and returns html"""
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exec(code+"\nprint(buf, end='')")
    return stdout.getvalue()

def render(template: str, variables: dict = None, escape_html: bool = True, newmodule: bool = True) -> str:
    """renders template and returns html"""
    py = parse(template, variables, escape_html, newmodule)
    return execute(py)

def read(filename: str, variables: dict = None, escape_html: bool = True, newmodule: bool = True) -> str:
    """reads template's file and returns html"""
    with open(filename) as f:
        return render(f.read(), variables, escape_html, newmodule)
