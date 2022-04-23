### Basics

Creating an app is as simple as defining a method called `app` which returns a UI component within a Python module. For example you can create a file named `hello_world.py` under your working directory, with the following content.

```read_module
demos.hello_world
```

You should find the same greeting as in the frame below at [localhost:8080/app/hello_world](http://localhost:8080/app/hello_world). Note that the `app` folder corresponds by default to the folder from which you launched the Reflect server (even though they have a different name). The app folder can be changed using the `--app-folder` command line argument.

```load_module
demos.hello_world
```

### Folder organization

We recommend you to store your app scripts inside dedicated subfolders. You can launch them using `.` as folder separator. For example an app located as shown below would be accessible from [localhost:8080/app/my_first_app.main](http://localhost:8080/app/my_first_app.main)

```read_file
website.folder_hierarchy
```

### Styling

You can customize component look and feel by passing a `style` argument. Note that you need to use [React camelCased](https://reactjs.org/docs/dom-elements.html) attribute names and not the original html attribute names.

```read_module
demos.hello_world_argument
```

```load_module
demos.hello_world_argument
```

You can also stylize apps using regular [CSS](https://www.w3schools.com/css/) style sheets. For example, create a `hello_world.css` file with the following content.

```read_file
demos/hello_world.css
```

Update the previous example as shown below.

```read_module
demos.hello_world_css
```

This will produce the following.

[comment]: # "loading greeting_argument instead as a workaround for the fact that CSS don't seem to be applied to embedded apps"

```load_module
demos.hello_world_argument
```

We would recommend using CSS for common style properties and customize specific components directly in the code.

### Summary

- An app is defined by a module implementing a method called `app` returning a UI component
- An app can be launched by entering its corresponding Python module path in the browser address bar (i.e. its relative path delimited with dots)
- Apps can be styled using:
  - css style sheets
  - explicit style arguments
