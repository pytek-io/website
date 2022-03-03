from reflect_antd import InputNumber, Space
from reflect_html import div

WHITE = "#FFFFFF"


def app():
    a = InputNumber(defaultValue=2, style={"width": 70})
    b = InputNumber(defaultValue=3, style={"width": 70})
    # a and b return none when empty
    formula = lambda: a() and b() and a() + b()
    return Space(
        [
            a,
            div("+", style={"color": WHITE, "textAalign": "center"}),
            b,
            div("=", style={"color": WHITE, "textAlign": "center"}),
            div(formula, style={"color": WHITE, "width": 30, "textAlign": "center"}),
        ],
    )
