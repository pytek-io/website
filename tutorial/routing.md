Reflect supports application routing making the overall user experience similar to the traditional web experience in which users can navigate back and forth in their navigation journey. It also allows to create deep links which can be shared or bookmarked. These will allow them to launch a given app with specific startup parameters.

### Using application hash value

You can pass any arbitrary string to an app by appending it to the app path using the `#` character. This string can be accessed through the `Window` hash attribute as shown below.

```read_module
tutorial.argument_hash#John
```

Calling this app at `app/tutorial.argument_hash#John` will yield the following.

```load_module
tutorial.argument_hash#John
```

Note hash is an observable value which can be updated from the app itself. This allows to make relevant parts of the app state known to the browser, closely replicating a more usual web user experience.

```read_module
tutorial.argument_hash_update#John
```

We can't display the result in this page directly as it would clash with the website navigation logic. You can instead follow this [link](tutorial.argument_hash_update#John) to launch this app and see how the app path is synchronized with the app content when navigating back and forth.

## Summary

- Parts of the app state can be exposed in the address bar, allowing users to create links that will launch apps with specific parameters
- It also allows users to navigate backwards and forwards
- App path can be accessed and updated through the Window path attribute
