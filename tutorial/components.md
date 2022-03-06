### General principles

Reflect exposes all native html components in `reflect_html` module as well as [many](internal:website.reflect.libraries) of the most popular React libraries. We will mostly use components from the [Ant Design](internal:website.reflect.libraries/antd.md) library throughout this tutorial as it provides many basic components well suited for simple tutorial.snippets.

One of the key features of Reflect design is that it exposes React components [API](https://reactjs.org/docs/introducing-jsx.html) as Python objects. These objects are created by passing their content (aka children) as first argument then their properties as named arguments.

### Component children

Children elements are components or values included within another parent component. Children can either be other components or "displayable" types such as `str`, `int`, `float` as shown in the example below.

```load_module
tutorial.snippets.component_children
```

```read_module
tutorial.snippets.component_children
```

As you can see the `parent` div takes a list of children, whereas each child takes a single value. As a general rule children must be passed as a list if there is more than one. You can also create dynamic content (i.e. children) by passing Python [callables](https://medium.com/swlh/callables-in-python-how-to-make-custom-instance-objects-callable-too-516d6eaf0c8d) instead of values, more on this [later](internal:website.reflect.tutorial/creating_inputs.md).

### Component properties

Components properties are attributes that control the aspect and behaviour of UI components, they can be either:

- literal values
- components
- Python [callables](https://medium.com/swlh/callables-in-python-how-to-make-custom-instance-objects-callable-too-516d6eaf0c8d)

#### Literal values

Components properties can be defined as literal values as shown below.

```load_module
tutorial.snippets.component_property_as_literal
```

```read_module
tutorial.snippets.component_property_as_literal
```

In this example you can see how the property `type` affects the aspect of the buttons. Literal values can be any scalar data type such as `str`, `int`, `float`, `bool`, etc. They can also be any arbitrarily nested combination of `list`, `tuple` and `dict` containing scalar types.

#### Components

Components properties can also be other components as shown below.

```load_module
tutorial.snippets.component_property_as_component
```

```read_module
tutorial.snippets.component_property_as_component
```

Note that in this example the child is a literal value, whereas the `icon` property is a component.

#### Python callables

The next - slightly spooky - example features a callback property value, that is, a method to be invoked when an event is triggered.

```load_module
tutorial.snippets.component_property_as_callback
```

```read_module
tutorial.snippets.component_property_as_callback
```

If you were daring enough to press the button you will see a popup message telling you not to do it again. You will also see a log of your naughtiness in the [browser console](https://updraftplus.com/faqs/how-do-i-open-my-browsers-developer-tools/) `Logs` tab, as all Python outputs are forwarded there. Note that callbacks can be [async](https://towardsdatascience.com/why-you-should-use-async-in-python-6ab53740077e) when needed. They can also receive data related to the event which fired them (more on this [later](internal:website.reflect.tutorial/custom_callbacks.md)).

### Summary

- Components always take content (aka: children) as first argument
- Component children and properties can be:
  - other UI components
  - literal values
  - callables
- Python output streams (`stdout`, `stderr`) are redirected to the browser console
