from website.common import create_menu_content

MENU = [
    [
        "General",
        [
            ["HTML", "react.md"],
            ["Ant Design", "antd.md"],
            ["RC Dock", "rc-dock.md"],
        ],
    ],
    [
        "Charts",
        [
            ["Plotly", "plotly.md"],
            ["Altair", "altair.md"],
            ["Bokeh", "bokeh.md"],
        ],
    ],
    [
        "Data grid",
        [
            ["AG Grid", "ag-grid.md"],
        ],
    ],
]


def content(module_argument):
    return create_menu_content(
        MENU,
        "overview.md",
        overview_name="Reflect libraries",
        folder="website/reflect/libraries",
        module_argument=module_argument,
    )
