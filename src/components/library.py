from fasthtml.common import *
import pokebase as pb

def build_input(label: str, name: str, placeholder: str = "", type: str = "text"):
    return Div(
        Label(label, For=name, cls="block text-sm font-medium text-foreground"),
        Input(
            id=name,
            name=name,
            type=type,
            placeholder=placeholder,
            cls="mt-1 block w-full rounded-md border border-input shadow-sm focus:ring-primary focus:border-primary sm:text-sm"
        ),
        cls="mb-4"
    )

def build_button(text: str, href: str = "#", cls: str = ""):
    return A(
        text,
        href=href,
        cls=(
            "inline-flex items-center justify-center px-4 py-2 text-sm font-medium "
            "text-white bg-primary rounded-md hover:bg-primary/90 "
            "focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary "
            f"{cls}"
        )
    )

def build_card(title: str, content: list, footer: str = None):
    """
    Renders a card with an optional footer.
    """
    return Div(
        Div(
            H3(title, cls="text-lg font-bold text-foreground"),
            Div(*content, cls="mt-2 text-sm"),
            cls="p-4 bg-card border border-border rounded-lg shadow"
        ),
        Footer(footer, cls="text-sm mt-4 text-muted-foreground") if footer else None,
        cls="mb-6"
    )

def build_list(items: list):
    """
    Creates a bullet list of items (strings).
    """
    return Ul(
        *(Li(item, cls="text-gray-700") for item in items),
        cls="list-disc pl-5 space-y-1 text-gray-700"
    )

def build_callout(
        title: str,
        description: str,
        variant: str = "default",
        collapsible: bool = True
):
    """
    Creates a callout box with an icon, title, and descriptive text.
    Optionally collapsible.
    """
    callout_classes = {
        "default": "bg-muted border border-border",
        "destructive": "bg-destructive/15 text-destructive border border-destructive/50",
    }

    icon_classes = {
        "default": "text-foreground",
        "destructive": "text-destructive",
    }

    icon_svg = '''
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
         fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
         stroke-linejoin="round" class="h-4 w-4">
        <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
        <path d="M12 8v4"/>
        <path d="M12 16h.01"/>
    </svg>
    '''

    return Details(
        Summary(
            Div(
                Span(NotStr(icon_svg), cls=f"mr-2 {icon_classes.get(variant, icon_classes['default'])}"),
                H5(title, cls="font-medium"),
                cls="flex items-center cursor-pointer"
            ),
            cls="flex items-center justify-between"
        ) if collapsible else Div(
            Span(icon_svg, cls=f"mr-2 {icon_classes.get(variant, icon_classes['default'])}"),
            H5(title, cls="font-medium"),
            cls="flex items-center"
        ),
        Div(
            description,
            cls="mt-2 text-sm"
        ),
        cls=f"{callout_classes.get(variant, callout_classes['default'])} p-4 rounded-lg shadow-sm",
        open=not collapsible
    )


# -- Specialized Components --

def build_pokemon_card(pokemon_name: str):
    """
    Fetches basic Pokémon data from the PokéAPI (via pokebase)
    and returns a card component.
    """
    pokemon = pb.APIResource("pokemon", pokemon_name.lower())
    species = pb.APIResource("pokemon-species", pokemon_name.lower())

    name = pokemon.name.title()
    height = pokemon.height / 10
    weight = pokemon.weight / 10
    types = ", ".join(t.type.name.title() for t in pokemon.types)
    abilities = ", ".join(a.ability.name.title() for a in pokemon.abilities)
    pokedex_number = species.id

    return build_card(
        title=f"{pokedex_number}: {name}",
        content=[
            Ul(
                Li(f"Height: {height}m"),
                Li(f"Weight: {weight}kg"),
                Li(f"Types: {types}"),
                Li(f"Abilities: {abilities}")
            )
        ],
        footer=P(
            "Data from Pokédex API wrapper, ",
            A("Pokebase", href="https://github.com/PokeAPI/pokebase", cls="underline text-primary")
        )
    )

def build_link_list(title: str, links: list):
    """
    Renders a small section with a title and a list of links.
    Each item in `links` should be a dict: {'text': str, 'href': str, 'desc': str (optional)}
    """
    list_items = []
    for link in links:
        item_text = [
            A(link["text"], href=link["href"], cls="text-primary hover:underline font-bold"),
        ]
        if link.get("desc"):
            item_text.append(f": {link['desc']}")
        list_items.append(Li(*item_text))

    return Div(
        H4(title, cls="font-medium mb-2"),
        Ul(*list_items, cls="list-disc pl-5 space-y-1 mb-4 font-bold")
    )

def build_text_section(title: str, paragraphs: list[str]):
    """
    Builds a simple text section with a heading and multiple paragraphs.
    """
    return Div(
        H3(title, cls="text-xl font-bold mb-2"),
        *(P(paragraph, cls="mb-4") for paragraph in paragraphs)
    )
