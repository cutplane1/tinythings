tmpl = '<div class="post">\n<time>{}</time>\n<p>{}</p>\n</div>\n'

def add_post(pattern: tuple, text: str, file_name: str, date: str):
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.read()
    
    with open(file_name, "w", encoding="utf-8") as f:
        m_contents = contents.replace(pattern[0]+pattern[1], pattern[0]+tmpl.format(date, text)+pattern[1],1)
        f.write(m_contents)

def upload_to_github_pages():
    # i made tmp

if __name__ == "__main__":
    import sys
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    add_post(('</a>\n', '<div class="post">\n'), " ".join(sys.argv[1:]), "microblog.html", now)