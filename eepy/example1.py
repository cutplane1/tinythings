import neepy

links = [("Home", "/"), ("About", "/about"), ("Contact", "/contact")]
my_posts = [
    {"title": "Hello", "content": "world"},
    {"title": "things i dislike", "content": "raw orange plup"},
    {"title": "r8 my xss", "content": "<script>alert('hi n00b')</script>"}
]

print(neepy.read("examples/index.eepy", {"posts": my_posts, "links": links}))
