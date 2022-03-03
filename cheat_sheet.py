from reflect_antd import Col, Row, Select, Checkbox
from reflect_prism import PrismCodeFormatter
from reflect_html import div
from reflect import get_window, WindowSize
from reflect_utils.md_parsing import parse_md_doc

Option = Select.Option

STEPS = ["setup", "install", "launch"]


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
        Option(human_name, value=platform)
        for human_name, platform in [
            ("Mac", "mac"),
            ("Windows", "win"),
            ("Linux", "lin"),
        ]
    ]
    platform = Select(platforms, defaultValue=platforms[0].value, style={"width": 90})
    steps = Checkbox.Group(options=STEPS, defaultValue=STEPS)

    def content():
        archive = f"reflect-{platform()}.{python()}-{reflect()}.tar.gz"
        url = f"https://pytek.io/data/archives/{archive}"
        is_win = platform() == "win"
        explicit_list = lambda: f"packages/reflect-{reflect()}.tar.gz packages/reflect_aggrid-{reflect()}.tar.gz packages/reflect_altair-{reflect()}.tar.gz packages/reflect_antd-{reflect()}.tar.gz packages/reflect_ant_icons-{reflect()}.tar.gz packages/reflect_bokeh-{reflect()}.tar.gz packages/reflect_html-{reflect()}.tar.gz packages/reflect_monaco-{reflect()}.tar.gz packages/reflect_plotly-{reflect()}.tar.gz packages/reflect_prism-{reflect()}.tar.gz packages/reflect_rcdock-{reflect()}.tar.gz packages/reflect_spectacle-{reflect()}.tar.gz packages/reflect_swiper-{reflect()}.tar.gz packages/reflect_utils-{reflect()}.tar.gz"

        def script():
            lines = []
            activated_environment = False
            activate_environment = (
                ".\\.venv\\Scripts\\activate.ps1"
                if is_win
                else "source .venv/bin/activate"
            )
            if "setup" in steps():
                lines.append(f"virtualenv --python {python()} .venv")
            if "install" in steps():
                lines.extend(
                    [
                        f'Start-BitsTransfer -Source "{url}"'
                        if is_win
                        else f"wget --no-check-certificate {url}",
                        f"tar xvf {archive}",
                        activate_environment,
                        "pip install " + explicit_list() if is_win else f"packages/*-{reflect()}.tar.gz",
                    ]
                )
                activated_environment = True
            if "launch" in steps():
                if not activated_environment:
                    lines.append(activate_environment)
                lines.append(".\\reflect.exe" if is_win else "./reflect")
            return "\n".join(line for line in lines if line is not None)

        return script

    def create_setting_row(name, component):
        return Row(
            [
                Col(
                    label(name),
                    className="ant-form-item-label",
                    span=12,
                ),
                Col(
                    component,
                    className="ant-form-item-control-input-content",
                ),
            ],
            justify="start",
            align="middle",
            style=dict(marginBottom=10),
        )

    def create_link(extension=""):
        name = f"reflect-{platform()}.{python()}-{reflect()}.tar.gz{extension}"
        return f'[{name}](download:{"/data/archives/" + name})'

    def label(content):
        return div(content, style={"textAlign": "right"})

    def create_col(content):
        return Col(
            content,
            xs=24,
            xl=18,
        )

    return Col(
        [
            Row(
                create_col(
                    [
                        div(style={"height": 10}),
                        create_row(
                            [
                                label("Platform"),
                                platform,
                                label("Python"),
                                python,
                                label("Version"),
                                reflect,
                            ],
                            f"repeat({6 if get_window().size() > WindowSize.xs else 2}, 1fr)",
                        ),
                    ]
                )
            ),
            Row(
                PrismCodeFormatter(
                    language="bash",
                    code=content,
                    lineNumbers=True,
                ),
            ),
            Row(create_col(Row(Col([steps]), justify="center"))),
            lambda: parse_md_doc(
                f'You can also download the archives manually ({create_link()}, {create_link(".sig")}). Our public signature can be obtained by [mail](mailto:contact@pytek.io).'
            ),
        ]
    )
