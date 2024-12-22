from typing import List, Tuple
from fasthtml.common import *

def create_layout(content, title: str = "Navigation", max_width: str = "max-w-3xl"):
    js = """
    document.addEventListener('DOMContentLoaded', () => {
        const sidebar = document.getElementById('sidebar');
        const toggleSidebarBtn = document.getElementById('toggle-sidebar-btn');
        let sidebarOpen = false;

        // Toggle sidebar
        toggleSidebarBtn.addEventListener('click', () => {
            if (sidebarOpen) {
                sidebar.style.width = '0';
                toggleSidebarBtn.textContent = '☰'; // Set to open icon
            } else {
                sidebar.style.width = '17rem';
                toggleSidebarBtn.textContent = '✖'; // Set to close icon
            }
            sidebarOpen = !sidebarOpen; // Toggle state
        });
    });
    """
    links = main.links
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title("Did Luigi shoot the CEO of United Healthcare"),
            Link(rel="stylesheet", href="app.css", type="text/css"),
            Script(js)
        ),
        Body(
            Div(
                build_header(),
                Div(
                    Sidebar(links, title),
                    Main(
                        Div(
                            content,
                            cls=f"{max_width} mx-auto px-4 py-8 transition-all duration-300",
                            id="main-content"
                        ),
                        cls="flex-1 min-h-[calc(100vh-128px)]"
                    ),
                    cls="flex flex-row flex-1"
                ),
                build_footer(),
                cls="flex flex-col h-full"
            )
        )
    )


def build_header():
    return Header(
        Nav(
            Div(
                Button(
                    "☰",
                    id="toggle-sidebar-btn",
                    cls="mr-4 p-2 text-white hover:text-gray-800 transition",
                    aria_label="Toggle sidebar"
                ),
                A("Did Luigi shoot the CEO of United Healthcare?", href="/", cls="text-xl font-bold text-white"),
                cls="container mx-auto px-4 py-6 flex justify-start items-center"
            ),
            cls="bg-blue-600"
        )
    )


def build_footer():
    return Footer(
        Div(
            P("© 2024 Axolmain works. All rights reserved.", cls="text-center text-gray-500"),
            cls="container mx-auto px-4 py-6"
        ),
        cls="bg-gray-100"
    )


def Sidebar(links: List[Tuple[str, str]], title: str = "Navigation"):
    def create_nav_item(text: str, href: str) -> Div:
        return Div(
            A(
                Span(text, cls="ml-3"),
                href=href,
                cls="flex items-center p-3 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors duration-200"
            ),
            cls="mb-1"
        )

    nav_items = [create_nav_item(text, href) for text, href in links]

    return Div(
        Div(
            Div(
                Span(title, cls="text-xl font-semibold text-gray-800"),
                cls="flex items-center p-4 border-b border-gray-200"
            ),
            Div(*nav_items, cls="p-4 space-y-2"),
            cls="h-full bg-white shadow-lg overflow-x-hidden transition-all duration-300 ease-in-out",
            id="sidebar",
            style="width: 0;"
        ),
        cls="h-full"
    )
