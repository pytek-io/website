from reflect_antd import Col, Row, Select, Checkbox
from reflect_prism import PrismCodeFormatter
from reflect_html import div
from reflect import get_window, WindowSize
from reflect_utils.md_parsing import parse_md_doc

Option = Select.Option

CREATE_PYTHON_ENV = "Create a Python environment"
INSTALL_PYTHON_MODULES = "Install Reflect modules"
LAUNCH_SERVER = "Launch Reflect server"

STEPS = [
    CREATE_PYTHON_ENV,
    INSTALL_PYTHON_MODULES,
    LAUNCH_SERVER,
]
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


def app():
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
    browser_platform = get_window().browser_details["platform"]
    print(browser_platform)
    platform = Select(
        platforms,
        defaultValue=PLATFORMS.get(browser_platform, PLATFORMS["Linux"]),
        style={"width": 90},
    )
    create_python_environment = Checkbox(CREATE_PYTHON_ENV, defaultChecked=True)
    install_python_modules = Checkbox(INSTALL_PYTHON_MODULES, defaultChecked=True)
    launch_server = Checkbox(LAUNCH_SERVER, defaultChecked=True)

    def content():
        archive = f"reflect-{platform()}.{python()}-{reflect()}"
        url = f"https://pytek.io/data/archives/{archive}.tar.gz"
        is_win = platform() == "win"

        def explicit_list():
            reflect_value = reflect()
            return " ".join(
                [f"reflect-{reflect_value}.tar.gz"]
                + [f"reflect_{name}-{reflect_value}.tar.gz" for name in MODULE_NAMES]
            )

        def script():
            folder_seperator = "\\" if is_win else "/"
            commands = ["mkdir reflect"]
            activated_environment = False
            activate_environment = (
                ".\\.venv\\Scripts\\activate.ps1"
                if is_win
                else "source .venv/bin/activate"
            )
            if create_python_environment():
                commands.extend(
                    [
                        "cd reflect" + folder_seperator,
                        f"virtualenv --python {python()} .venv",
                    ]
                )
            if install_python_modules():
                commands.extend(
                    [
                        f'Start-BitsTransfer -Source "{url}"'
                        if is_win
                        else f"wget --no-check-certificate {url}",
                        f"tar xvf {archive}.tar.gz",
                        activate_environment,
                        f"cd {archive}{folder_seperator}packages",
                        "pip install " + (explicit_list() if is_win else "*.tar.gz"),
                        f"cd ..{folder_seperator}..",
                    ]
                )
                activated_environment = True
            if launch_server():
                if not activated_environment:
                    commands.append(activate_environment)
                commands.append(
                    f".{folder_seperator}{archive}{folder_seperator}reflect"
                    + (".exe" if is_win else "")
                )
            return "\n".join(line for line in commands if line is not None)

        return script

    def create_link(extension=""):
        name = f"reflect-{platform()}.{python()}-{reflect()}.tar.gz{extension}"
        return f'[{name}](download:{"/data/archives/" + name})'

    def label(content):
        return div(content, style={"textAlign": "right"})

    def create_col(content, style=None):
        return Col(content, xs=24, xl=18, style=style)

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

    def is_xs_display():
        return get_window().size() > WindowSize.xs

    return Col(
        [
            Row(
                create_col(
                    [
                        create_box_title("Steps"),
                        Row(
                            Col(
                                [
                                    div(create_python_environment),
                                    div(install_python_modules),
                                    div(launch_server),
                                ]
                            ),
                            justify="center",
                        ),
                    ],
                    style={"padding": "20px"},
                ),
                style={"border": "1px solid #f0f0f0", "marginBottom": "20px"},
            ),
            Row(
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
                                reflect,
                            ],
                            f"repeat({6 if is_xs_display() else 2}, 1fr)",
                        ),
                    ],
                    style={"paddingTop": "20px", "paddingRight": "20px"},
                ),
                style={"border": "1px solid #f0f0f0"},
            ),
            Row(
                PrismCodeFormatter(
                    language="bash",
                    code=content,
                    lineNumbers=True,
                ),
            ),
            lambda: parse_md_doc(
                f"""You can also use the links to download the relevant files and install Reflect as you see fit.
* {create_link()}
* {create_link(".sig")}

Our public signature can be obtained by [mail](mailto:contact@pytek.io)."""
            ),
        ]
    )
