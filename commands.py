import os
from reflect_antd import Col, Row, Select
from reflect_html import div
from reflect_prism import PrismCodeFormatter

from reflect import WindowSize, get_window

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


def components():
    python_versions = [
        Option(f"3.{version}", value=f"3.{version}")
        for version in reversed(list(range(7, 11)))
    ]
    reflect_versions = [
        Option(version, value=version) for version in os.listdir("archives")
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


PADDING = 3


def activate_environment(is_win, add_comment=True):
    return (
        ".\\.venv\\Scripts\\activate.ps1" if is_win else "source .venv/bin/activate"
    ) + (
        " " * PADDING + "# activating the virtual environment *if not already active*"
        if add_comment
        else ""
    )


def cd_to_working_directory(is_win):
    activate_command = activate_environment(is_win)
    cd_command = "cd reflect" + folder_separator(is_win)
    return (
        cd_command
        + " " * (activate_command.index("#") - len(cd_command))
        + "# moving to the working directory *if not already there*"
    )


def folder_separator(is_win):
    return "\\" if is_win else "/"


def join_lines(lines):
    return PrismCodeFormatter(
        language="bash",
        code="\n".join(line for line in lines if line is not None),
        lineNumbers=True,
    )


def create_python_environment():
    python, _reflect, platform = components_cached()
    is_win = platform() == "win"
    return join_lines(
        [
            "mkdir reflect" + folder_separator(is_win),
            f"virtualenv --python {python()} .venv",
            activate_environment(is_win, False),
        ]
    )


def install_reflect():
    python, reflect_version, platform = components_cached()
    archive = f"reflect-{platform()}.{python()}-{reflect_version()}"
    archive_name = f"{archive}.tar.gz"
    url = f"https://pytek.io/data/archives/{reflect_version()}/{archive_name}"
    is_win = platform() == "win"

    def explicit_list():
        reflect_value = reflect_version()
        return " ".join(
            [f"reflect-{reflect_value}.tar.gz"]
            + [f"reflect_{name}-{reflect_value}.tar.gz" for name in MODULE_NAMES]
        )

    return join_lines(
        [
            cd_to_working_directory(is_win),
            activate_environment(is_win),
            f'Start-BitsTransfer -Source "{url}"'
            if is_win
            else f"curl {url} -o {archive_name}",
            f"tar xvf {archive_name}",
        ]
        + (
            [
                f"cd {archive}{folder_separator(is_win)}packages",
                "pip install " + (explicit_list() if is_win else "*.tar.gz"),
                f"cd ..{folder_separator(is_win)}..",
            ]
            if is_win
            else [f"pip install {archive}/packages/*.tar.gz"]
        )
    )


def launch_server():
    python, reflect_version, platform = components_cached()
    archive = f"reflect-{platform()}.{python()}-{reflect_version()}"
    is_win = platform() == "win"
    return join_lines(
        [
            cd_to_working_directory(is_win),
            activate_environment(is_win),
            f".{folder_separator(is_win)}{archive}{folder_separator(is_win)}reflect"
            + (".exe" if is_win else ""),
        ]
    )


def app():
    python, reflect_version, platform = components_cached()
    return Row(
        create_col(
            [
                create_box_title("Configuration"),
                create_row(
                    [
                        label("Platform"),
                        platform,
                        label("Python"),
                        python,
                        label("Version"),
                        reflect_version,
                    ],
                    f"repeat({6 if is_xs_display() else 2}, 1fr)",
                ),
            ],
            style={"paddingTop": "20px", "paddingRight": "20px"},
        ),
        style={"border": "1px solid #f0f0f0"},
    )
