# neepy ((Not) Enough Embedded PYthon)
pretty bad template engine without sandboxing

python syntax is not quite suitable for a templating engine but i like the outcome 

python code line starts with `@`(at) symbol<br>
"Variable Expressions" must be in double curly braces: `{{post['created_at']}}`<br>
you can include other templates with `@include:`: `@include:whatever_template.eepy`<br>
"Compound Statements"(if, for) must be closed with `@end`:
```
@for level in range(1,6+1):
<h{{level}}>header {{level}}</h{{level}}>
@end
```

## example:
index.eepy
```
@for post in posts:
<h1>{{ post['title'] }}</h1>
<p>{{ post['text'] }}</p>
@end
```
```
import neepy
posts = [
    {"title":"hello", "text": "world"}
]
html = neepy.read("index.eepy", {"posts": posts})
response(html)
```
## API:
`read("template.eepy")` is equal to:
```
with open("template.eepy", "r") as f:
    html = render(f.read())
```
```
render(template: str, variables: dict = None, escape_html: bool = True, newmodule: bool = True) -> str:
read(filename: str, variables: dict = None, escape_html: bool = True, newmodule: bool = True) -> str:
```
