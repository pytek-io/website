### Creating observable values

In the previous examples we created apps which state is defined by their input components values. Taking this further we can also create observable values, that is app state variables, by using the `make_observable` method as shown in the example below.

```load_module
tutorial.make_observable
```

```read_module
tutorial.make_observable
```

In this example `value` is an `int` value wrapped within an `ObservableValue` object. An `ObservableValue` is callable and observable. One can think of it as an "invisible Excel cell", that is an object whose content is automatically tracked by the components which depend on it.
Note that the `ObservableValue` content (i.e. the integer value) can only be modified through `ObservableValue` methods. We used the `set` method here for illustration purposes, but more elegantly we could have used a Python assignment operator (e.g. +=, -=) as those are supported by `ObservableValue`. Advanced readers might be reminded of [contextvars](https://docs.python.org/3/library/contextvars.html) or [React State Hook](https://reactjs.org/docs/hooks-state.html) APIs which also provide ad-hoc containers to wrap plain values describing the application state.
You probably noticed some strong similarities between `ObservableValue` and input component in that they are both callable and observable. Using the standard [terminology](https://en.wikipedia.org/wiki/Observer_pattern) we will refer to them as observables from now on.

### Creating observable collections

Representing app state can also require using collection types such as `list` or `dict`. One can also pass those to the `make_observable` method which will wrap them within `ObservableList` or `ObservableDict` respectively. Those objects have the same interface as their built-in Python counterparts but for the fact that they are observables. The example below shows a simple user list being populated and displayed.

```load_module
tutorial.make_observable_collection
```

```read_module
tutorial.make_observable_collection
```

In this example we wrapped `users` within an `ObservableList` called `user_obs`. Note that doing so implies that we only modify it through `user_obs` methods. You can still access `users` directly but in "read only" mode, to persist it, inspect it, etc.
Another interesting point to notice is that `new_user_name` observable is passed to an input component that will update it. This is handy either for separating the business logic (aka the model) from the UI representation (aka the view) or for defining inter-dependant components.
One last thing worth mentioning is the key arguments we passed to `make_observable`. These key values will be displayed in the `str` and `repr` methods to help debugging.

### Autorun

We have seen so far that components automatically track updates to the observables they depend on. This allows for an elegant callback free API. However, we might sometimes want to have arbitrary side effects to occur on observable updates. Reflect supports this through the `autorun` method as featured below.

```load_module
tutorial.autorun
```

```read_module
tutorial.autorun
```

As you probably expect you will find a log of all the inputs entered in the browser console. This is particularly useful for debugging but could also be used for auto-saving app states, triggering asynchronous tasks, etc.
Note the `key` argument passed to `name` component will appear in the printed output as well as in the [React developer tools](https://flaviocopes.com/react-developer-tools/) display.

### Summary

- Observable values can be created using `make_observable` method
- `list` and `dict` are wrapped within `ObservableList` and `ObservableDict` respectively
- Observables are callable objects which automatically notify their dependant components
- App state is defined by the values of its observables
- `autorun` automatically executes the method passed to it whenever one of the observables it depends on is updated
