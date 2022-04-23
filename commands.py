from reflect_antd import Col, Row, Select
from reflect_html import div, blockquote

from reflect import WindowSize, get_window

Option = Select.Option

PLATFORMS = {
    "MacOS": "mac",
    "Windows": "win",
    "Linux": "lin",
}


def components():
    python_versions = [
        Option(f"3.{version}", value=f"3.{version}")
        for version in reversed(list(range(7, 11)))
    ]
    reflect_versions = [
        Option(f"0.{version}", value=f"0.{version}")
        for version in reversed(list(range(1, 2)))
    ]
    python = Select(
        python_versions, defaultValue=python_versions[0].value, style={"width": 80}
    )
    reflect = Select(
        reflect_versions, defaultValue=reflect_versions[0].value, style={"width": 80}
    )
    platforms = [
        Option(human_name, value=platform) for human_name, platform in PLATFORMS.items()
    ]
    platform = Select(
        platforms,
        defaultValue=PLATFORMS.get(
            get_window().browser_details["platform"], PLATFORMS["Linux"]
        ),
        style={"width": 90},
    )
    return python, reflect, platform


def components_cached():
    window = get_window()
    settings = window.user_data.get("reflect_settings", None)
    if not settings:
        settings = components()
        window.user_data["reflect_settings"] = settings
    return settings


def create_row(content, template):
    content = [
        div(
            element,
            style=dict(paddingLeft=10 if i % 2 == 1 else None, paddingBottom=10),
        )
        for i, element in enumerate(content)
    ]
    return div(
        content,
        style={
            "display": "grid",
            "alignItems": "center",
            "gridTemplateColumns": template,
        },
    )


def create_col(content, style=None):
    return Col(content, xs=24, xl=18, style=style)


def label(content):
    return div(content, style={"textAlign": "right"})


def is_xs_display():
    return get_window().size() > WindowSize.xs


def create_box_title(title):
    return div(
        title,
        style={
            "position": "absolute",
            "top": "-14px",
            "marginLeft": "16px",
            "padding": "1px 8px",
            "color": "#777",
            "background": "#fff",
            "borderRadius": "2px 2px 0 0",
            "transition": "background-color 0.4s",
        },
    )


def app():
    python, reflect, platform = components_cached()
    return Row(
        create_col(
            [
                create_box_title("Configuration"),
                blockquote("fs"),
                create_row(
                    [
                        label("Platform"),
                        platform,
                        label("Python"),
                        python,
                        label("Version"),
                        reflect,
                    ],
                    f"repeat({6 if is_xs_display() else 2}, 1fr)",
                ),
            ],
            style={"paddingTop": "20px", "paddingRight": "20px"},
        ),
        style={"border": "1px solid #f0f0f0"},
    )
