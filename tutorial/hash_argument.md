Reflect exposes to the [browser location hash](https://www.w3schools.com/jsref/prop_loc_hash.asp) through an observable value called hash. This is useful to make the overall user experience similar to the traditional web experience. In particular it allows users to navigate back and forth from one state to another using the navigation keys. It also allows to pass startup arguments to apps. This allows to define ad'hoc as regular web links which can be shared or bookmarked.

### Reading the application hash argument

You can pass a hash argument to an app by appending a string at the end of the path using the `#` character as separator. For example invoking the code below at `app/tutorial.snippets.hash#John` will yield the following.

```read_module
tutorial.snippets.hash#John
```

```load_module
tutorial.snippets.hash#John
```

Note `hash` is an observable value which can be updated from the app itself. This allows to record parts of the app state in the browser history, closely replicating a more usual web user experience.

```read_module
tutorial.snippets.hash_update#John
```

We can't display the result in this page directly as it would clash with the website navigation logic. You can instead follow this [link](tutorial.snippets.hash_update#John) to launch this app and see how the app path is synchronized with the app content when navigating back and forth.

## Summary

- Parts of the app state can be exposed in the address bar, allowing users to create links that will launch apps with specific parameters
- It also allows users to navigate backwards and forwards
- App path can be accessed and updated through the Window path attribute
