import os
from website.common import create_menu_content
from reflect_antd import Button, Image, Row, Col, Typography
from reflect_html import a, section
from reflect_prism import PrismCodeFormatter
from reflect_utils.md_parsing import parse_md_doc
from reflect_utils.common import make_editable

MENU = [
    [
        "Grid computing dashboard",
        'demos.dispatch#{ "archive": "demos/dispatch/replay.pick"}',
    ],
    ["Plotly stock chart", "demos.stocks_history"],
    ["Crypto derivatives backtester", "demos.crypto_backtester"],
    [
        "Yahoo Finance live quotes",
        'demos.yahoofinancelive#["CL=F", "^GSPC", "^FCHI", "^FTSE", "^FTMC", "^N225", "BTC-USD", "GC=F", "^HSI", "^DJI", "EURUSD=X", "GBPEUR=X"]',
    ],
    ["Ant components explorer", "demos.ant"],
    ["Todo list", "demos.todo_list#demos/todo_list/default_todo_list.json"],
    ["AG Grid example", "demos.stock_prices"],
    ["Generic dashboard", "demos.dashboard"],
    ["App explorer", "demos.app_explorer#demos"],
]

FILES_TO_ENTRIES = {file_path.split("#", 1)[0]: entry for entry, file_path in MENU}


def text(content, type="default"):
    return Typography.Text(content, type=type)


def page_creator(file_path):
    actual_path = file_path.split("#")[0].replace(".", os.sep)
    md_file_path = os.path.join(actual_path, "description.md")
    return section(
        [
            Typography.Title(FILES_TO_ENTRIES[file_path.split("#", 1)[0]], level=3),
            make_editable(parse_md_doc(open(md_file_path, "r").read()), md_file_path),
            Row(
                [
                    Col(Image(width=200, src=os.path.join(actual_path, name)))
                    for name in os.listdir(actual_path)
                    if name.endswith(".png")
                ],
                gutter=20,
            ),
            Typography.Paragraph(
                [
                    text(
                        "The button below will launch the app in a new tab (check your browser settings if nothing appears). Beware that it might "
                    ),
                    text("take a while to initialize the first time", type="danger"),
                    text(" if you are on a "),
                    text("mobile network", type="danger"),
                    text("."),
                ]
            ),
            Button(
                a(
                    "Launch app",
                    href="/app/" + file_path,
                    target="_blank",
                ),
                type="primary",
            ),
            Typography.Title("Source", level=3),
            PrismCodeFormatter(
                language="python",
                code=open(os.path.join(actual_path, "__init__.py"), "r").read(),
                theme="github",
                lineNumbers=True,
            ),
        ],
        className="markdown",
    )


def content(module_argument):
    return create_menu_content(
        MENU,
        "gallery_overview.md",
        "Demos overview",
        folder="website/reflect",
        module_argument=module_argument,
        page_creator=page_creator,
        full_menu=MENU,
        module="website.reflect.gallery",
    )
