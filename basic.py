from reflect_antd import Button, Checkbox, Col, Input, Row

def app():
    return Row(
        [
            Col(Checkbox("I agree.", style={"color": "white"})),
            Col(Button("Click me!")),
            Col(Input(placeholder="Your name")),
        ],
        align="middle",
        gutter=10,
    )
