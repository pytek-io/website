Fortunately lambda's survived Python 3 despite Guido's and Alex's will. Even though it does a feel arguably a bit inconsistent with the rest of Python language it is quite handy in some situations especially when writing Reflect apps. It provides an easy mean to defer computations which is one of the cornerstone of Reflect. So what is a lambda expression then? Well, simply put a python method defined using the lambda keyword, like below.

```python
double = lambda x: 2 * x
```

which is equivalent to:

```python
def double(x):
    return 2 * x
```

It is of particular interest when it "captures" surrounding variables like below.

```python
a = 2
multiplier = lambda x: a * x
```

It allows us to chain callable calls very naturally, for example.

