Reflect supports application routing, making the overall user experience similar to the traditional web experience in which users can navigate back and forth in their navigation journey. It also allows the creation of deep links which can be shared or bookmarked. These allow users to launch a given app with specific startup parameters.

### Using application hash value

You can pass any arbitrary string to an app by appending it to the app path using the `#` character. This string can be accessed through the `Window` hash attribute as shown below.

```read_module
tutorial.snippets.argument_hash#John
```

Calling this app at [localhost:8080/app/tutorial.snippets.argument_hash#John](http://localhost:8080/app/tutorial.snippets.argument_hash#John) will yield the following.

```load_module
tutorial.snippets.argument_hash#John
```

Note hash is an observable value which can be updated from the app itself. This allows you to make relevant parts of the app state known to the browser, replicating the usual web user experience in which user navigate from one page to the other.

```read_module
tutorial.snippets.argument_hash_update#John
```

We can't display the result in this page directly as it would clash with the website navigation logic. You can instead follow this [localhost:8080/app/tutorial.snippets.argument_hash_update#John](http://localhost:8080/app/tutorial.snippets.argument_hash_update#John) to launch this app and see how the app path is synchronized with the app content when navigating back and forth.

## Summary

- Parts of the app state can be exposed in the address bar, allowing users to create links that will launch apps with specific parameters
- It also allows users to navigate backwards and forwards
- The app path can be accessed and updated through the Window path attribute
