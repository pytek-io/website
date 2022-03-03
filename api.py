import reflect.utils


from docs.generate_doc import extract_api, String, Method
from reflect_html import div
from reflect_antd import Table, Typography

Title = Typography.Title


def flatten_description(description):
    if isinstance(description, String):
        yield description.content
    elif isinstance(description, list):
        for element in description:
            yield from flatten_description(element)


titles = ["name", "DefaultValue", "description"]
columns = [dict(title=title, dataIndex=title, key=title) for title in titles]


def display_method(method):
    dataSource = [
        {
            "name": argument.name,
            "DefaultValue": argument.default_value,
            "description": list(flatten_description(argument.description)),
        }
        for argument in method.arguments
    ]
    return Table(
        columns=columns, dataSource=dataSource, pagination=False, key=method.name
    )


def app():
    result = [Title("API", level=1)]
    file_path = "docs/build/antd/reflect_antd.xml"
    # file_path = "docs/build/reflect.xml"
    for obj_type, details in extract_api(file_path):
        if obj_type == "class":
            constructor, methods = details
            result.append(Title(constructor.name, level=2))
            result.append(Title("constructor", level=3))
            result.append(display_method(constructor))
            for method in methods:
                result.append(Title(method.name, level=3))
                result.append(display_method(method))
        else:
            pass
            # print(obj_type, details)
    return div(result)
