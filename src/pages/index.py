fromcomponents.library import *


def build_landing_page():
    """
    Returns a modern landing page for "TikTok vs The Media: Luigi Mangione & UnitedHealthcare."
    """
    modal = build_modal(Div(
        P("This is the modal body."),
        Button("Close", cls="btn btn-secondary", data_bs_dismiss="modal"),
        cls="modal-body"
    ))
    return Main(
        Div(
            # HERO / HEADER
            Div(
                H1(
                    'Welcome to TikTok vs "The Media": Luigi Mangione & UnitedHealthcare',
                    cls="text-3xl sm:text-4xl font-extrabold text-center mb-4"
                ),
                modal,
                P(
                    (
                        "In the aftermath of the tragic events surrounding UnitedHealthcare "
                        "CEO Brian Thompson's death, the internet has become a whirlwind of "
                        "emotions, opinions, and theories. This site is my personal endeavor "
                        "to delve into the Luigi Mangione case, aiming to shed light on the "
                        "complex narratives that have emerged online."
                    ),
                    cls="text-center max-w-2xl mx-auto text-gray-700 mb-8"
                ),
                cls="hero-section pt-12 pb-8"
            ),

            # CONTENT SECTIONS
            Div(
                # ---- WHAT THIS SITE IS ABOUT ----
                Section(
                    H2("What This Site Is About", cls="text-2xl font-bold mb-3"),
                    P(
                        'At TikTok vs "The Media": Luigi Mangione & UnitedHealthcare, I just want to focus on:',
                        cls="mb-4 text-gray-700"
                    ),
                    Ul(
                        Li(Span("Compiling News Reports" , cls="font-bold"), ": Read and watch real-time news and official statements."),
                        Li(Span("Analyzing Social Media" , cls="font-bold"), ": Scroll through TikTok & Reels to find circulating trends."),
                        Li(Span("Tracking Public Sentiment" , cls="font-bold"), ": Observe how feelings evolve via screenshots, X, and Reddit."),
                        Li(Span("Exploring Digital Footprints" , cls="font-bold"), ": Investigate Mangione's online presence and interpretations."),
                        cls="list-disc pl-5 space-y-2 text-gray-700 mb-8"
                    ),
                    cls="site-purpose mb-10"
                ),

                # ---- MY APPROACH ----
                Section(
                    H2("My Approach", cls="text-2xl font-bold mb-3"),
                    P(
                        (
                            "I aim to present an unbiased perspective on the case, and will do my best "
                            "to refrain from taking a stance on whether Mangione was involved or whether "
                            "his actions were justified. Instead, my goal is to highlight how people are "
                            "processing this incident, giving enough data from both sides so that ignorance "
                            "is minimized."
                        ),
                        cls="text-gray-700 mb-8"
                    ),
                    cls="approach-section mb-10"
                ),

                # ---- KEY FEATURES ----
                Section(
                    H2("Key Features", cls="text-2xl font-bold mb-3"),
                    Ul(
                        Li(Span("News Timeline" , cls="font-bold"), ": A chronological collection of news articles and updates. (NOT RELEASED YET)"),
                        Li(Span("Theory Tracker" , cls="font-bold"), ": A look at popular theories and discussions happening online."),
                        Li(Span("Sentiment Analysis" , cls="font-bold"), ": Insights into how public opinion shifts over time. (NOT RELEASED YET)"),
                        Li(Span("Digital Footprint Exploration" , cls="font-bold"), ": Examination of Mangione's online activity. (NOT RELEASED YET)"),
                        cls="list-disc pl-5 space-y-2 text-gray-700 mb-8"
                    ),
                    cls="features-section mb-10"
                ),

                # ---- WHY THIS MATTERS ----
                Section(
                    H2("Why This Matters", cls="text-2xl font-bold mb-3"),
                    P(
                        (
                            "In today’s age of social media and people's apparent lack of direction, events like this "
                            "reveal the intricate relationship between what people deem right, and what those elected "
                            "by said people deem is right. By exploring the responses to the Mangione case, I hope to "
                            "foster a better understanding of how information spreads and how everyone reacts."
                        ),
                        cls="text-gray-700 mb-6"
                    ),
                    cls="why-it-matters mb-10"
                ),

                # ---- DISCLAIMER ----
                Section(
                    P(
                        (
                            Span("Disclaimer:" , cls="font-bold"), " This site is not intended to solve the case or replace official "
                            "investigations. It serves as a personal exploration of digital culture and media "
                            "discourse surrounding this event. If you want to contribute, feel free to open a "
                            "pull request on Github."
                        ),
                        cls="text-sm text-gray-500"
                    ),
                    cls="disclaimer mb-16"
                ),

                cls="content-container max-w-3xl mx-auto"
            ),
            cls="landing-page"
        )
    )
