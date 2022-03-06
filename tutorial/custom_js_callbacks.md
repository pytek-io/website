### Defining javascript callbacks

Although Reflect allows you to build apps entirely in Python, there are a few edge cases where it is necessary to write some short callbacks in JavaScript. These cases typically arise when one needs to define customized display formats or even customize component behaviour. The following example demonstrates how to customize a number format.

```load_module
tutorial.snippets.js_method
```

```read_module
tutorial.snippets.js_method
```

Notice how the input is nicely formatted in the UI input component, while the output displays the raw number. A `JSMethod` constructor takes a unique tag as first argument allowing us to identify any errors related to this function. The second argument is the JavaScript method body, the remaining ones are the JavaScript argument names.
You may have noticed in that example that we displayed the raw number by calling `amount_input` from a lambda expression. We need to do that in order for the framework to display the actual `amount_input` value.

### Currying javascript callbacks

We can spice things up a bit by currying custom java script methods. The example below shows how to prevent users from selecting dates landing either in the past, on weekends, or within an arbitrary list of dates that we display next to the input.

```load_module
tutorial.snippets.js_method_curried
```

```read_module
tutorial.snippets.js_method_curried
```

You can notice that the `filter_dates` callback takes two arguments. The first one (i.e. holidays) is passed when we partially apply the callback. The remaining one will then be passed on the client side. Another interesting point to notice is the fact that we convert `holidays` dates into timestamps. This is usually not necessary as Python data are automatically converted to their Javascript counterparts. In this example, however, we convert Python dates to timestamps as object JavaScript don't support operators (equality, etc).

Taking this further you can define more complex behaviours. In the example below we show how to restrict the date range a user can choose.

```load_module
tutorial.snippets.js_method_curried_advanced
```

```read_module
tutorial.snippets.js_method_curried_advanced
```

You will notice how we pass observables as a value argument to input components which they control. It would be impossible to define these two interdependent components otherwise.

## Summary

- `JSMethod` allows you to refine UI components when required

- `JSMethod` can be partially applied on the server side and then evaluated on the client side

- Standard Python data are automatically converted to JavaScript equivalents

