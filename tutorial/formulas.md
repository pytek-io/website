### Using input components

Roughly speaking, one can distinguish two main types of UI components. Output components which are mainly used to render apps, and input components that allow users to interact with apps, as shown in the example below.

```load_module
tutorial.snippets.formula_as_lambda
```

```read_module
tutorial.snippets.formula_as_lambda
```

The fundamental feature to point out here is that the input component `name` is callable. As one would expect, calling it returns the value that has been last entered by the user. We then define `greeting`, which is also callable as it is a [lambda function](https://www.w3schools.com/python/python_lambda.asp). Notice that we created a callable chain as `greeting` calls `name` in its formula. We then pass `greeting` as a child to `greeting_component` which will automatically evaluate it whenever `name` changes.

### Creating formulas

In the previous example we showed how to define dynamic behaviour by passing a callable child. This dynamic behaviour is fairly similar to Excel formulas, however it is much more general. In Reflect we call **_formula_** any Python callable which depends either directly or indirectly on input component values.
There are a few ways one can create callables in Python. We used a lambda function in the previous example as it is the simplest way to create a callable. For slightly more complex computations, one can use [closures](https://www.programiz.com/python-programming/closure) as shown in the example below.

```load_module
tutorial.snippets.formula_as_closure
```

```read_module
tutorial.snippets.formula_as_closure
```

Notice how the displayed result automatically updates whenever `a`, `b` or `operation` are changed. You can also create callables - therefore formulas - using [functools partial](https://www.learnpython.org/en/Partial_functions) or [bound methods](https://www.geeksforgeeks.org/bound-methods-python/) for more complex apps. One thing to realize is that despite the strongly functional nature of its API, Reflect does not force you to use any particular programming style. Below is the same example implemented in an object oriented style.

```read_module
tutorial.snippets.formula_as_bound_method
```

### Defining properties as formulas

We have demonstrated formulas as children so far, but formulas can also be used to define dynamic properties. The example below features a property value defined as a formula.

```load_module
tutorial.snippets.component_property_as_formula
```

```read_module
tutorial.snippets.component_property_as_formula
```

Note that callables are interpreted as either dynamic property values or [callbacks](http://localhost:8080/website.main#website.reflect.tutorial/creating_components.md), depending on the type of the property.

### Summary

- Input components are callable, returning their content when invoked
- A formula is any Python callable which depends either directly or indirectly on input components
- Content (i.e. children) and component properties can be passed as formulas to generate dynamic behaviour
