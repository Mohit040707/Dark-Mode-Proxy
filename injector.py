from mitmproxy import http

dark_css = """
<style>
html {
    filter: invert(1) hue-rotate(180deg) !important;
    background: #111 !important;
}
img, video {
    filter: invert(1) hue-rotate(180deg) !important;
}
</style>
"""

def response(flow: http.HTTPFlow):
    if "text/html" in flow.response.headers.get("content-type", ""):
        content = flow.response.get_text()
        content = content.replace("</head>", dark_css + "</head>")
        flow.response.set_text(content)