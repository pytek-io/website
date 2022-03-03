from reflect_antd import InputNumber, Space

def app():
    a = InputNumber(defaultValue=2)
    b = InputNumber(defaultValue=3)
    result = lambda: a() + b()
    return Space([a, "+", b, "=", result])
