import html
def render(body):
    return f'<p>{html.escape(body, quote=True)}</p>'
