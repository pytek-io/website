### Adding control

So far, we have built simple apps in a callback free style. Although this allows us to define the app behaviour in a very concise way it does not offer any control in terms of when app updates occur. We can use a `Controller` object to specify explicitly when components are refreshed as shown below.

```load_module
tutorial.snippets.controller
```

```read_module
tutorial.snippets.controller
```

In this example the `controller` object controls all the components that are created within its scope. This means that output components will update only when we call `commit` on the controller. It also allows us to revert input components to their previous state by calling the `rollback` method. These two methods allow for the easy implementation of OK/Cancel behaviours. All `Component` can accept an explicit controller argument when a `with` statement is not suitable. Last but not least, note that `autorun` and `make_observable` can also be similarly controlled.

## Summary

- Controller object allows you to:
  - control when updates to observables are propagated to their dependents
  - revert input components to the last committed values
  - controller can be defined either by using a `with` statement, or as an explicit argument to components
