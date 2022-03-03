from website.common import create_menu_content

MENU = [
    ["Get started", "get_started.md"],
    ["Apps", "apps.md"],
    ["Components", "components.md"],
    ["Formulas", "formulas.md"],
    ["Observables", "observables.md"],
    ["Controller", "controller.md"],
    ["Deep observability", "deep_observability.md"],
    ["JavaScript callbacks", "custom_js_callbacks.md"],
    ["Async tasks", "async_tasks.md"],
    ["Hash argument", "routing.md"],
    ["Caching", "caching.md"],
    # ["Python callbacks", "custom_callbacks.md"],
]

MENU = [MENU[0]] + [
    [f"{i}. {title}", file_path] for i, (title, file_path) in enumerate(MENU[1:], 1)
]



def content(module_argument):
    return create_menu_content(
        MENU,
        None,
        None,
        folder="website/tutorial",
        module_argument=module_argument,
        full_menu=MENU,
        module="website.reflect.tutorial",
    )
