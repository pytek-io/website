from os import path
from typing import Dict
from itertools import chain

from reflect import ResponsiveValue, get_window, WindowSize
from reflect_antd import Col, Row, Typography
from reflect_html import a, div, img, svg, path as path_component
from reflect_prism import PrismCodeFormatter
from reflect_swiper import Swiper, SwiperSlide
from reflect_utils.common import responsive_margins, load_module

from .reflect.gallery import MENU as GALLERY_MENU
from .reflect.libraries import MENU as LIBRARY_MENU
from .common import LIGHT_BLUE, GREEN, BACKGROUND_COLOR

Title = Typography.Title

EDIT = "M257.7 752c2 0 4-.2 6-.5L431.9 722c2-.4 3.9-1.3 5.3-2.8l423.9-423.9a9.96 9.96 0 000-14.1L694.9 114.9c-1.9-1.9-4.4-2.9-7.1-2.9s-5.2 1-7.1 2.9L256.8 538.8c-1.5 1.5-2.4 3.3-2.8 5.3l-29.5 168.2a33.5 33.5 0 009.4 29.8c6.6 6.4 14.9 9.9 23.8 9.9zm67.4-174.4L687.8 215l73.3 73.3-362.7 362.6-88.9 15.7 15.6-89zM880 836H144c-17.7 0-32 14.3-32 32v36c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-36c0-17.7-14.3-32-32-32z"

MAIN_COL_BREAK_POINTS = dict(xs=24, sm=4)
JS_PYTHON_RESULT_BREAK_POINTS = dict(xs=24, md=19, lg=16, xl=12)
SIMPLE_FORMULA_BREAKPOINTS = dict(xs=24, sm=20, md=17, lg=16, xl=12)
FONT_FAMILY = "Nanum Pen Script, cursive"
FONT_FAMILY = "Permanent Marker, cursive"

MAIN_TITLE_STYLE = dict(
    fontSize="32px",
    margin="3.2vw",
    textAlign="center",
    color=LIGHT_BLUE,
    fontFamily=FONT_FAMILY,
)

SUB_TITLE_WITHOUT_MARGINS = dict(
    fontSize="24px",
    textAlign="center",
    color=LIGHT_BLUE,
    fontFamily=FONT_FAMILY,
)

TITLE_STYLE = dict(
    textAlign="center",
    color=LIGHT_BLUE,
    fontFamily=FONT_FAMILY,
)

SUB_TITLE_STYLE = dict(
    marginTop="min(6.4vh, 6.4vw)",
    marginBottom="1.6vh",
    marginLeft="3.2vh",
    marginRight="3.2vh",
    **SUB_TITLE_WITHOUT_MARGINS,
)


DISPLAY_EDITOR_LINE_NUMBERS = False


def add_dashed_frame(style={}):
    result = style.copy()
    result.update(
        borderColor=GREEN,
        borderStyle="dashed",
        padding=10,
    )
    return result


CODE_EDITOR_STYLE = {
    "backgroundColor": BACKGROUND_COLOR,
    "fontSize": "14px",
    "margin": 0,
    "padding": 0,
}


def clone_and_update(base: Dict, **updates):
    result = base.copy()
    result.update(**updates)
    return result


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx : min(ndx + n, l)]


def find_file_extension(file_path):
    for extension in ["png", "svg", "jpg"]:
        maybe_path = f"{file_path}.{extension}"
        if path.exists(maybe_path):
            return maybe_path


LIBRARY_ICONS_AND_MODULES = [
    (
        category,
        [
            (
                human_readable_name,
                file_name,
                find_file_extension(path.join("website", "logos", file_name[:-3]))
                or path.join("website", "logos", "github.png"),
            )
            for human_readable_name, file_name in libraries
        ],
    )
    for category, libraries in LIBRARY_MENU
]


def create_code_editor_raw(file_name, language):
    return PrismCodeFormatter(
        language=language,
        code=open(file_name, "r").read(),
        theme="vsDark",
        lineNumbers=DISPLAY_EDITOR_LINE_NUMBERS,
        style=CODE_EDITOR_STYLE,
    )


def frame_box(content):
    return div(
        content,
        style=add_dashed_frame(
            dict(
                color=LIGHT_BLUE,
                margin=20,
                textAlign="justify",
                height="fit-content",
            )
        ),
    )


def text_column(content):
    return responsive_margins(
        frame_box(content),
        md=2,
        lg=3,
        xl=4,
        xxl=5,
    )


def title(content):
    return div(content, style=SUB_TITLE_STYLE)


def subtitle(content, **kwargs):
    return div(content, style=clone_and_update(SUB_TITLE_STYLE, color=GREEN, **kwargs))


def responsive_columns_with_title(contents, breakpoints, frames=None):
    frames = [True] * len(contents) if not frames else frames
    return Row(
        [
            Col(
                [
                    subtitle(title),
                    frame_box(content) if frame else content,
                ],
                **breakpoints,
            )
            for frame, (title, content) in zip(frames, contents)
        ],
        justify="space-around",
    )


def create_grid(rows):
    assert len(set(map(len, rows))) == 1, rows
    return div(
        list(chain.from_iterable(rows)),
        style={
            "display": "grid",
            "gridTemplateColumns": f"repeat({len(rows[0])}, 1fr)",
        },
    )


def centered(content):
    return Row(
        content,
        justify="space-around",
        align="middle",
    )


def content(*args):
    demo_apps_carousel = Swiper(
        [
            SwiperSlide(
                [
                    img(
                        dataSrc=path.join(
                            path.split(app_path.split("#")[0])[0], "default.png"
                        ),
                        style={"width": "100%"},
                        className="swiper-lazy",
                    ),
                    div(className="swiper-lazy-preloader-white"),
                ]
            )
            for name, app_path in GALLERY_MENU[:-1]  # excluding presentation
        ],
        navigation=True,
        style={
            "width": "100%",
        },
    )
    current_demo_name = lambda: GALLERY_MENU[demo_apps_carousel() or 0][0]
    main_title = Title(
        "Turn your Python scripts into web apps",
        level=1,
        style=clone_and_update(
            TITLE_STYLE,
            marginBottom="2em",
            marginTop="2em",
        ),
    )

    story = [
        (
            "The full stack approach",
            "Full stack solutions are complex to setup and operate, developing web apps within them requires multiple technical skills.",
        ),
        (
            "A turn key solution",
            "Reflect is a fully integrated web framework allowing you to write interactive web apps all in Python. It can be setup instantly, and allows users of all technical levels to develop apps.",
        ),
        (
            "Go full Python!",
            "Leverage the power of Python and React combined together inside a rock solid framework. Build prototypes in no time, turn them into industrial applications effortlessly.",
        ),
    ]
    story = [(subtitle(title), frame_box(content)) for title, content in story]

    def story_section():
        return (
            chain.from_iterable(story)
            if get_window().size() <= WindowSize.sm
            else create_grid(list(zip(*story)))
        )

    library_logos = div(
        [
            Row(
                [
                    Col(
                        div(
                            name + ":",
                            style=clone_and_update(
                                SUB_TITLE_WITHOUT_MARGINS,
                                color=GREEN,
                                textAlign="center",
                            ),
                        ),
                        **dict(xs=24, sm=8),
                    ),
                    Col(
                        Row(
                            [
                                Col(
                                    a(
                                        img(
                                            src=logo_path,
                                            alt=file_name,
                                            className="markdown-inline-image",
                                            style={
                                                "display": "block",
                                                "marginLeft": 10,
                                                "marginRight": 10,
                                                "marginTop": "10px"
                                                if name == "General"
                                                else None,
                                                "height": "max(5vh, 5vw)"
                                                if file_name != "plotly.md"
                                                else None,
                                                "maxWidth": "max(12vh, 12vw)",
                                            },
                                        ),
                                        title=f"Go to {human_readable_name} description",
                                        href=f"#website.reflect.libraries/{file_name}",
                                    ),
                                    # **MAIN_COL_BREAK_POINTS,
                                )
                                for human_readable_name, file_name, logo_path in libraries
                            ],
                            justify=ResponsiveValue("space-around", sm="left"),
                            align="middle",
                        ),
                        **dict(xs=24, sm=16),
                    ),
                ],
                align="middle",
                justify="left",
                style={
                    "marginTop": "max(3vh, 3vw)",
                },
            )
            for name, libraries in LIBRARY_ICONS_AND_MODULES
        ]
    )
    simple_formula_editor = PrismCodeFormatter(
        language="python",
        code=open("website/simple_formula.py", "r").read(),
        theme="vsDark",
        lineNumbers=DISPLAY_EDITOR_LINE_NUMBERS,
        style=CODE_EDITOR_STYLE,
    )
    return div(
        responsive_margins(
            [
                responsive_margins(main_title, lg=1, xxl=2),
                responsive_margins(demo_apps_carousel, xs=2, md=0),
                a(
                    subtitle(current_demo_name),
                    title=lambda: f"Open {current_demo_name()} demo page",
                    href=lambda: f"#website.reflect.gallery/{GALLERY_MENU[demo_apps_carousel() or 0][1]}",
                ),
                story_section,
                Row(
                    load_module("website.python_and_react"),
                    justify="space-around",
                    style=clone_and_update(SUB_TITLE_STYLE, color=GREEN),
                ),
                title(
                    "No advanced skills required, just code your apps like spreadsheets"
                ),
                text_column(
                    "Reflect comes with a dependency tracking engine allowing to design apps in a declarative way. This means that the application behaviour is implicitly inferred from the code structure, no callback needed!"
                ),
                responsive_columns_with_title(
                    [
                        ("This code:", simple_formula_editor),
                        (
                            "will produce:",
                            centered(
                                frame_box(load_module("website.simple_formula_actual"))
                            ),
                        ),
                    ],
                    SIMPLE_FORMULA_BREAKPOINTS,
                    [True, False],
                ),
                title("Use React JSX API directly in Python"),
                text_column(
                    'React components original APIs have been "reflected" in Python. As a result you don\'t need to learn any new API and can use the original documentation.'
                ),
                responsive_columns_with_title(
                    [
                        ("jsx:", create_code_editor_raw("website/basic.jsx", "jsx")),
                        (
                            "python:",
                            create_code_editor_raw("website/basic.py", "python"),
                        ),
                        (
                            "will both produce:",
                            centered(frame_box(load_module("website.basic_actual"))),
                        ),
                    ],
                    JS_PYTHON_RESULT_BREAK_POINTS,
                    [True, True, False],
                ),
                title("Batteries included"),
                text_column(
                    "Reflect let you use the most popular React libraries out of the box. See a list of the most well known ones below."
                ),
                library_logos,
                title("A framework for everyone"),
                text_column(
                    "We worked hard to make simple things trivial. As a result developing simple apps is within the reach of anyone with basic programming skills. Experienced programmers can easily go much further by leveraging powerfull features to develop arbitrarily complex apps. Take a look at our interactive tutorial and write your first app in no time."
                ),
                responsive_margins(
                    a(
                        img(
                            "website/tutorial.png",
                            width="100%",
                        ),
                        title=f"Check tutorial",
                        href=f"#website.reflect.tutorial",
                    ),
                    xs=12,
                ),
                title("Feedback!"),
                text_column(
                    "Please feel free to give us your feedback on any aspect of the Reflect project. Click on the icon below to visit the feedback page."
                ),
                Row(
                    Col(
                        a(
                            svg(
                                path_component(EDIT),
                                width=100,
                                height=100,
                                viewBox="0 0 896 896",
                                fill=LIGHT_BLUE,
                            ),
                            title="Go to feedback page",
                            href=f"#website.reflect.presentation/information/feedback.md",
                        ),
                        className="anticon anticon-edit",
                        style=dict(width=100, height=100),
                    ),
                    justify="center",
                ),
            ]
        ),
        style={
            "marginBottom": "5%",
        },
    )
