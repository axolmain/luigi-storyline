# src/pages/gematria_page.py

from fasthtml.common import *

fromcomponents.library import (
    build_card,
    build_callout,
    build_pokemon_card
)


def build_gematria_page():
    """
    Returns the entire Gematria page with a cleaner reading flow.
    """
    return Main(
        Div(
            # ---- INTRODUCTION ----
            Div(
                H2("Introduction to Gematria and the Number 286", cls="text-2xl font-bold mb-4"),
                P(
                    (
                        "Gematria is the practice of assigning numerical values to letters, words, or phrases, "
                        "often used to find hidden meanings or connections. This page explores the number 286 "
                        "and its potential significance in various contexts."
                    ),
                    cls="mb-4 text-gray-700"
                ),
                cls="mb-8"
            ),

            # ---- DISCLAIMER ----
            Div(
                P(
                    (
                        "Disclaimer: The connections and interpretations presented on this page may or may not be "
                        "related. It's up to the user to determine the relevance and significance of these "
                        "associations. This information is provided for educational and entertainment purposes only."
                    ),
                    cls="text-sm text-gray-600 italic mb-8"
                )
            ),

            # ---- CARD 1: WHERE DO WE FIND '286'? ----
            build_card(
                title="Where can we find the number 286?",
                content=[
                    Div(
                        H4("Luigi Mangione’s Profile", cls="font-medium mb-2"),
                        Ul(
                            Li("Post count: ", Span("286", cls="font-normal"), cls="font-bold"),
                            Li("Breloom Pokédex input: ", Span("286", cls="font-normal"), cls="font-bold"),
                            cls="list-disc pl-5 space-y-1 mb-4"
                        ),
                        P("Related", cls="text-md mt-2 mb-1"),
                        Ul(
                            Li(
                                A(
                                    "Nino Mangione (Luigi’s cousin) follower count: ",
                                    href="https://x.com/NinoMangione42",
                                    cls="text-primary hover:underline font-bold"
                                ),
                                "286",
                                cls="font-normal"
                            ),
                            cls="list-disc pl-5 space-y-1"
                        )
                    )
                ]
            ),

            # ---- CARD 2: EVENTS ----
            build_card(
                title="Events",
                content=[
                    Ul(
                        Li(
                            "CEO shooting - McDonald's Altoona: ",
                            Span("286 miles", cls="font-normal"),
                            Sup('*'),
                            cls="font-bold"
                        ),
                        cls="list-disc pl-5 space-y-1 mb-2"
                    ),
                    P(
                        Sup('*'),
                        Span(
                            "Shortest Apple Maps route shows 286 miles. Uncertain which McDonald's was involved.",
                            cls="text-sm text-gray-600"
                        )
                    )
                ]
            ),

            # ---- CARD 3: WHAT IT MIGHT MEAN ----
            build_card(
                title="Possible Meanings",
                content=[
                    Ul(
                        Li(
                            A(
                                "Proverbs 28:6 - ",
                                href="https://www.churchofjesuschrist.org/study/scriptures/ot/prov/28?lang=eng",
                                cls="font-bold text-primary hover:underline"
                            ),
                            "Better is the poor that walketh in his uprightness, than he that is perverse "
                            "in his ways, though he be rich."
                        ),
                        Li(
                            A(
                                "Denial code 286 - ",
                                href="https://www.mdclarity.com/denial-code/286",
                                cls="font-bold text-primary hover:underline"
                            ),
                            "Used when the appeal time limits for a claim have not been met."
                        ),
                        cls="list-disc pl-5 space-y-2 mb-4"
                    ),
                    P(
                        "Remember that these interpretations are subjective—some might "
                        "resonate with you, others might not."
                    ),
                ]
            ),

            # ---- CARD 4: POKÉMON SAMPLE (Breloom) ----
            build_pokemon_card("breloom"),

            # ---- CALLOUT: SOURCES ----
            build_callout(
                title="Sources",
                description=Div(
                    P("Check out the TikTok compilation by ",
                      A('@juanbergman', 
                        href='https://www.tiktok.com/@juanbergman/video/7447666971967032598?_r=1&_t=ZN-8sPiCLXugul',
                        cls='font-bold text-primary hover:underline'),
                      "f or more 286 connections."),
                    Div(
                        Img(
                            src='pictures/nino_mangione.png',
                            cls="w-full h-auto cursor-pointer"
                        ),
                        Img(
                            src="pictures/hilton_to_mcdonalds.png",
                            cls="w-full h-auto cursor-pointer"
                        ),
                        Img(
                            src='pictures/x_cover.png',
                            cls="w-full h-auto cursor-pointer"
                        ),
                        cls="grid grid-cols-3 gap-4"
                    )
                ),
                variant="default",
                collapsible=True
            ),
            cls="space-y-8 py-8 px-4"
        )
    )
