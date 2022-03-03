import toml

from reflect_antd import Typography, Row, Col, Layout, Checkbox, Divider, Tag
from reflect_html import section

from reflect_html import div, section, article
from reflect_utils.misc import list_all_files
from reflect_utils.md_parsing import parse_md_doc


OPTIONS = [
    {"label": "Python", "value": "python"},
    {"label": "Programming", "value": "programming"},
]

COLORS = {"python": ["cyan", "Python"], "programming": ["magenta", "Programming"]}

CSS = [
    "website/ant_site_index.css",
]


def read_post(path):
    return toml.loads(open(path, "r").read()), open(path[:-4] + "md", "r").read()


def app():
    topics = Checkbox.Group(
                    options=OPTIONS,
                    style={"marginLeft": "1rem"},
                )
    entries = sorted(
        (
            read_post(path)
            for path in list_all_files("website/blog", lambda x: x.endswith(".toml"))
        ),
        key=lambda x: x[0]["dateTime"],
    )
    posts = []
    for details, md_content in entries:
        # if set(details["topics"]).intersection(topics())
        posts.append(
            div(
                [
                    div(
                        [
                            Typography.Title(details["title"], level=4),
                            div(
                                details["dateTime"].strftime("%b %d, %Y"),
                                style={
                                    "marginLeft": "auto",
                                },
                            ),
                        ],
                        style={"display": "flex"},
                    ),
                    div(
                        parse_md_doc(
                            f"**TLDR**: {details['summary']}"
                        )
                    ),
                    section(
                        Row(
                            Col(
                                # make_editable(parse_md_doc(md_content), file_path)
                                parse_md_doc(md_content)
                                # style=dict(
                                #     marginLeft="-8px", marginRight="-8px", rowGap="0px"
                                # ),
                            ),
                            className="markdown",
                        )
                    ),
                    div([Tag(COLORS[tag][1], color=COLORS[tag][0]) for tag in details["topics"]]),
                    Divider(),
                ]
            )
        )
    return Layout(
        [
            Layout.Sider(
                topics,
                className="site-layout-background",
                width=150,
                style={"background": "#FFFFFF"},
            ),
            Layout.Content(
                [
                    section(
                        article(posts),
                        className="main-container main-container-component",
                    ),
                ],
            ),
        ],
        style=dict(padding="24px 0", background="#FFFFFF"),
    )


if __name__ == "__main__":
    app()
