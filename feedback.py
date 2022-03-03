import os
import pickle

from reflect_antd import Button, Col, Input, Row, Select
from reflect_html import *


TextArea = Input.TextArea
Option = Select.Option


def create_form_item(label_tag, component):
    return Row(
        [
            Col(
                label(label_tag),
                span=4,
                className="ant-form-item-label",
            ),
            Col(
                component,
                span=20,
                className="ant-form-item-control-input-content",
            ),
        ],
        style=dict(marginTop=10),
        align="middle",
    )

def app(subject="", author="", category=""):
    feedback_nb = 0 
    file_path = os.path.join("feedbacks", "feedback_nb")
    if os.path.exists(file_path):
        default_values = pickle.loads(open(file_path, "rb").read())
    subject = Input(
        defaultValue=subject,
        placeholder="What you are writing about.",
    )
    author = Input(
        defaultValue=author, placeholder="A clue about yourself."
    )
    category = Select(
        [
            Option("General", value="general"),
            Option("Website", value="website"),
            Option("Reflect", value="reflect"),
        ],
        defaultValue=category,
    )
    feedback = TextArea(
        defaultValue="",
        autoSize=True,
        placeholder="Your feedback, much appreciated, thanks!",
    )

    def onClick():
        open(file_path, "wb").write(
            pickle.dumps(
                {
                    "category": category(),
                    "subject": subject(),
                    "author": author(),
                    "feedback": feedback(),
                }
            )
        )

    return Col(
        [
            create_form_item("Subject", subject),
            create_form_item("From", author),
            create_form_item("Category", category),
            Row(feedback, style=dict(marginTop=10)),
            Row(
                Button("Submit", type="primary", onClick=onClick),
                style=dict(marginTop=10),
                justify="center",
            ),
        ],
        style={
            "width": "80%",
            "marginLeft": "auto",
            "marginRight": "auto",
        },
    )
