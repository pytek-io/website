from reflect_html import div, img
from reflect_antd import Col, Row


def app():
    return Row(
        [
            Col(
                div(
                    "Reflect",
                    style={
                        "fontSize": "24px",
                        "fontWeight": "bold",
                    },
                )
            ),
            Col(
                div(
                    "=",
                    style={
                        "fontSize": "24px",
                        "fontWeight": "bold",
                    },
                )
            ),
            Col(
                img(
                    src="website/static/python.svg",
                    alt="python",
                    style={"width": "10vw"},
                )
            ),
            Col(
                div(
                    "+",
                    style={
                        "fontSize": "24px",
                        "fontWeight": "bold",
                    },
                )
            ),
            Col(
                img(
                    src="website/static/react.svg",
                    alt="react",
                    style={"width": "10vw"},
                )
            ),
        ],
        align="middle",
        justify="space-around",
        gutter=15,
    )
