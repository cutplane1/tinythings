from bottle import route, post, run, request
from clamav_client.scanner import get_scanner # type: ignore
import tempfile
import os

index_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>clamp</title>
</head>
<body>
    <form action="/scan" method="post" enctype="multipart/form-data">
        <input type="file" name="f">
        <br>
        <input type="submit" value="scan this file">
    </form>
</body>
</html>"""

result_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>{}</title>
</head>
<body style="background-color: {};">
    <h1>{}</h1>
</body>
</html>"""

scanner = get_scanner({"backend": "clamd"})

@route('/')
def index():
    return index_page

@post('/scan')
def scan():
    f = request.files.get('f')

    if f is None and not f.filename:
        return "No file uploaded"

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, f.filename)
        f.save(path)
        scan_res = scanner.scan(path)
        if scan_res.state == "ERROR":
            return "Internal error"
        elif scan_res.state == "OK":
            return result_page.format("PASS", "white", "FILE IS OK")
        elif scan_res.state == "FOUND":
            return result_page.format(scan_res.details, "red", scan_res.details)
        return ":3"



run(host='localhost', port=8080)