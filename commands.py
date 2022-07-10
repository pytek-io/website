import os
from reflect_antd import Col, Row, Select
from reflect_html import div
from reflect_prism import PrismCodeFormatter

from reflect import WindowSize, get_window

REFLECT_MODULES = [
    "reflect",
    "reflect_antd",
    "reflect_utils",
    "reflect_html",
    "reflect_aggrid",
    "reflect_plotly",
    "reflect_altair",
    "reflect_prism",
    "reflect_ant_icons",
    "reflect_rcdock",
    "reflect_bokeh",
    "reflect_spectacle",
    "reflect_swiper",
    "reflect_monaco",
]

Option = Select.Option
MODULE_NAMES = [
    "aggrid",
    "altair",
    "antd",
    "ant_icons",
    "bokeh",
    "html",
    "monaco",
    "plotly",
    "prism",
    "rcdock",
    "spectacle",
    "swiper",
    "utils",
]
PLATFORMS = {
    "MacOS": "mac",
    "Windows": "win",
    "Linux": "lin",
}
COMMENT_PADDING = 3


def extract_version(wheel_name: str):
    return wheel_name.split("-")[1]


def convert_to_int_tuple(version_as_string: str):
    return tuple(int(element) for element in version_as_string.split("."))


def components():
    python_versions = [
        Option(f"3.{version}", value=f"3.{version}")
        for version in reversed(list(range(7, 11)))
    ]
    reflect_versions = [
        Option(version, value=version)
        for version in sorted(
            set(extract_version(element) for element in os.listdir("packages")),
            key=convert_to_int_tuple,
            reverse=True,
        )
    ]
    python = Select(
        python_versions, defaultValue=python_versions[0].value, style={"width": 80}
    )
    reflect_version = Select(
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
    return python, reflect_version, platform


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


def display_commands(lines):
    return PrismCodeFormatter(
        code="\n".join(line for line in lines if line is not None),
    )


def install_reflect():
    modules_list = f" ".join(REFLECT_MODULES)
    return display_commands(
        [
            f"pip install --trusted-host pytek.io --index-url https://pytek.io/simple {modules_list}",
        ]
    )


def launch_server():
    return display_commands(["reflect"])
