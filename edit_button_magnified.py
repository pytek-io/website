import imp
from reflect import js
from reflect_antd.icon import Icon
from reflect_html import div
from reflect_antd import Row, Col
from reflect_utils.feedback import make_editable
import os


def app():
    return Row(
        Col(
            make_editable(
                div(""), __name__, dict(fontSize="1500%")
            )
        ),
        justify="center",
    )
