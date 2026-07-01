"""Local review server for the SYNCON site with Netlify-style clean URLs.

Run from the repo root:  py tools/serve_clean.py [port]
Then open http://localhost:5174/  (default port 5174).

It serves the ../sitio folder and resolves extensionless routes the same way
Netlify does, so nav links like /faqs, /productos, /productos/har work:

    /about            -> sitio/about.html
    /productos        -> sitio/productos.html   (file wins over the dir)
    /productos/har    -> sitio/productos/har.html
    /                 -> sitio/index.html
    missing route     -> sitio/index.html        (the `/* -> /index.html 200` rule)
    missing asset     -> 404                      (so broken files stay visible)
"""

import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitio")
)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5174


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        fs = super().translate_path(path)
        if os.path.isdir(fs):
            index = os.path.join(fs, "index.html")
            if os.path.exists(index):
                return index
            sibling = fs.rstrip("/\\") + ".html"
            if os.path.exists(sibling):
                return sibling
            return fs
        if os.path.exists(fs):
            return fs
        if os.path.exists(fs + ".html"):
            return fs + ".html"
        # A missing path WITH an extension is a broken asset (.mp4/.css/.svg):
        # let it 404 so the problem is visible, instead of masking it as HTML.
        if os.path.splitext(fs)[1]:
            return fs
        # Extensionless routes fall back to index.html, like Netlify's /* rule.
        return os.path.join(ROOT, "index.html")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    print(f"Serving {ROOT} with clean URLs on http://localhost:{PORT}")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
