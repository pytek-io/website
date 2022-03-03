from reflect_antd import Button, Checkbox, Input, create_row


def app():
    return create_row(
        [
            Checkbox("I agree.", style={"color": "white"}),
            Button("Click me!"),
            Input(placeholder="Your name"),
        ],
        col_kwargs=dict(xs=24, xl=8, style=dict(paddingTop="1em")),
        style=dict(paddingRight="1em", paddingLeft="1em", paddingBottom="1em"),
    )
