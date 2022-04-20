### Defining asynchronous callbacks

Reflect offers strong support for asynchronous task execution. It is particularly useful when your app needs to wait for the completion of any external tasks while still being responsive. The example below shows how to fetch data asynchronously using http requests.

```load_module
tutorial.snippets.async_callback
```

```read_module
tutorial.snippets.async_callback
```

In this example we use [httpx](https://www.python-httpx.org/) which is an [asyncio](https://docs.python.org/3/library/asyncio.html) compatible http client. The key point to notice here is that `on_click` callback is async. You can also make pass async methods to `autorun` or even define `app` as async.
Reflect relies on [anyio](https://anyio.readthedocs.io) which runs on top of [asyncio](https://docs.python.org/3/library/asyncio.html). You can therefore choose to leverage anyio's [structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency) API or use asyncio directly.

### Updating app state asynchronously

Being intrinsically asynchronous, Reflect also allows you to design full blown asynchronous apps. The following example features realtime Bitcoin automatic updates.

```load_module
tutorial.snippets.async_task
```

```read_module
tutorial.snippets.async_task
```

In this example, we use the auxiliary method `ws_connection_manager` which is a thin wrapper around an asyncio `Websocket` object, making it slightly more user friendly.

Notice that we called `get_window` which returned a `Window` instance. This object is the main entry point to advanced functionalities such as spawning async tasks. `start_soon` is a method which calls [anyio start_soon](https://anyio.readthedocs.io/en/stable/tasks.html#starting-and-initializing-tasks), the main difference being the former catches exceptions and reports them to the user automatically. One last thing to be aware of with asynchronous updates is that the web client needs to consume them as they are produced otherwise the connection is automatically reset. In practice this means that if the server cannot send updates to a client device which is in sleep mode.

### Evaluating child asynchronously

In some order to keep an app responsive one should always use asynchronous API when evaluating something that can take a significant amount of time (eg: database query, heavy computation, etc). Component children can accept async formulas those will return `None` until the underlying computation has finished. One can fine tune the expected behaviour by wrapping an async formula using `async_formula` as featured in the example below.

```load_module
tutorial.snippets.async_formula
```

```read_module
tutorial.snippets.async_formula
```

## Summary

- Advanced functionalities are accessible through `get_window` which return a `Window` instance
- You can use any asyncio/trio compatible libraries
- Callbacks, `autorun` methods, `app` can be asynchronous
- Apps can spawn asynchronous tasks running in the background
- Automatic updates requires the web client to be running
