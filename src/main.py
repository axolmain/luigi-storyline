frompages.gematria import build_gematria_page
fromcomponents.layout import *
frompages.index import build_landing_page

# Initialize app
app, rt = fast_app()


links = [
    ("Home", "/"),
    ("268 explored via Gematria", "/268-gematria")
]


@rt("/")
def get():
    content = build_landing_page()
    return create_layout(content, "Navigation")


@rt("/268-gematria")
def get():
    content = build_gematria_page()
    return create_layout(content, "Navigation")


@rt("/{fname:path}.{ext:static}")
def get(fname: str, ext: str):
    return FileResponse(f'public/{fname}.{ext}')

@rt("/popup/{path:path}")
def get_popup(path: str):
    return Div(
        Img(src=f"/{path}", cls="max-w-full max-h-full rounded shadow-lg"),
        Button("Close",
               cls="absolute top-4 right-4 text-white bg-red-600 px-4 py-2 rounded",
               hx_get="#",
               hx_target="#image-modal",
               hx_swap="innerHTML")
    )



serve()
