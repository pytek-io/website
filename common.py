import os
from itertools import count
import anyio
from reflect.components import Callback
from reflect.value import autorun, make_observable

from reflect_antd import Layout, Menu, Affix, Button
from reflect_ant_icons import MenuOutlined, CloseOutlined
from reflect_html import article, section, a, div
from reflect_utils.md_parsing import parse_md_doc
from reflect_utils.feedback import make_editable

MENU_COL_BREAK_POINTS = dict(xs=24, sm=24, md=6, lg=6, xl=5, xxl=4)
MAIN_COL_BREAK_POINTS = dict(
    xs=24,
    # sm=24,
    md=24,
    lg=20,
    xl=19,
    xxl=20,
)


WHITE = "#FFFFFF"
GREEN = "#0da166"
LIGHT_BLUE = "#9CDCFE"
BLUE = "#0162a9"
RED = "#d13342"
GREEN = "#0ba267"
GREEN = "#4EC9B0"
WHITE = "#FFFFFF"
GREY = "#848689"
YELLOW = "#DCDCAA"
BRONZE = "#CE9178"
DARK_BLUE = "#0C2D48"
ALMOST_BLACK = "#0f1724"
BACKGROUND_COLOR = ALMOST_BLACK

LOGO_HEIGHT = 52
HOME_PAGE = "website.home"

def generate_surrounding_items(MENU):
    def generate_surrounding_items(item):
        index = next(
            (index for index, (_, _item) in enumerate(MENU) if item == _item), None
        )
        if index is None:
            return None, None
        return (
            (MENU[index - 1] if index > 0 else None),
            (MENU[index + 1] if index < len(MENU) - 1 else None),
        )

    return generate_surrounding_items


def create_menu_content(
    menu,
    overview,
    overview_name=None,
    folder=None,
    module_argument=None,
    page_creator=None,
    full_menu=None,
    module=None,
):
    scroll_states = {}
    surrounding_items = generate_surrounding_items(full_menu) if full_menu else None
    menu_keys, menu_counter = [], count()

    def set_module_argument(description):
        module_argument.set(description)
        scroll_states[description] = [0, 0]

    def create_menu(name, description):
        if isinstance(description, list):
            menu_key = f"menu_{next(menu_counter)}"
            menu_keys.append(menu_key)
            return Menu.SubMenu(
                [
                    create_menu(sub_name, sub_description)
                    for sub_name, sub_description in description
                ],
                title=name,
                key=menu_key,
            )
        else:
            return Menu.Item(
                name,
                key=description,
                onClick=lambda: set_module_argument(description),
            )

    if overview:
        overview_item = [
            Menu.Item(
                overview_name or "Overview",
                key=overview,
                onClick=lambda: set_module_argument(overview),
            )
        ]
    else:
        overview_item = []
        overview = menu[0][-1]

    def default_file_path():
        return module_argument() if module_argument() != "default" else overview

    menu = Menu(
        overview_item + [create_menu(name, item) for name, item in menu],
        mode="inline",
        selectedKeys=lambda: [default_file_path()],
        defaultOpenKeys=menu_keys,
        key="left_menu",
    )

    def actual_file_path():
        file_path = module_argument()
        return default_file_path() if file_path == "default" else file_path

    def page_content():
        if module_argument() is None:
            return
        file_path = actual_file_path()
        if page_creator and file_path != overview:
            return page_creator(file_path)
        complete_file_path = os.path.join(folder, file_path)
        return make_editable(
            section(
                parse_md_doc(open(complete_file_path, "r").read()),
                className="markdown",
            ),
            complete_file_path,
        )

    def navigation_links():
        if surrounding_items is None:
            return None
        left, right = surrounding_items(actual_file_path())
        if left:
            title, file_path = left
            left = a(f"< {title}", href=f"#{os.path.join(module, file_path)}")
        if right:
            title, file_path = right
            right = a(
                f"{title} >",
                href=f"#{os.path.join(module, file_path)}",
                style={"float": "right"},
            )
        if left or right:
            return div([left, right])

    scrolled = anyio.Event()

    def on_scroll(x):
        nonlocal scrolled
        scroll_states.__setitem__(actual_file_path(), x)
        scrolled.set()

    collapsed = make_observable(False)

    main_section = section(
        [
            article(page_content),
            navigation_links,
        ],
        className="main-container main-container-component",
        style={
            "overflow": "auto",
            "maxHeight": "85vh",
        },
        onScroll=Callback(
            on_scroll,
            args=["target.scrollLeft", "target.scrollTop"],
        ),
    )

    content = div(
        [
            Affix(
                Button(
                    lambda: MenuOutlined() if collapsed() else CloseOutlined(),
                    onClick=lambda: collapsed.set(not collapsed()),
                    id="menu-button",
                    style={"margin": 1},
                ),
                offsetTop=12,
            ),
            main_section,
        ]
    )
    # seems that we sometimes call scrollTo too early, I don't know what event I should wait for, hence this hack...
    running = False

    async def set_scroll_position():
        nonlocal scrolled, running
        if running:
            return
        running = True
        file_path = actual_file_path()
        scroll_values = scroll_states.get(file_path, [0, 0])
        for _ in range(10):
            scrolled = anyio.Event()
            await main_section.scrollTo(*scroll_values)
            with anyio.move_on_after(1) as scope:
                await scrolled.wait()
            if scope.cancel_called:
                break
            if scroll_states[file_path] == scroll_values:
                break
        running = False

    autorun(set_scroll_position)

    # return main_section
    return Layout(
        [
            Layout.Sider(
                menu,
                className="site-layout-background",
                width=220,
                style={
                    "background": WHITE,
                    "overflow": "auto",
                    "maxHeight": "100vh",
                },
                collapsed=collapsed,
                collapsedWidth=0,
                trigger=None,
                theme="light",
            ),
            Layout.Content(content),
        ],
        style=dict(
            padding="24px 0",
            background=WHITE,
        ),
    )
