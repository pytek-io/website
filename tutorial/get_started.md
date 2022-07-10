#### Install Reflect modules

Reflect can be installed using any Python package manager tool. Below is an example showing how to install Reflect and all available reflect modules using [pip](https://pypi.org/project/pip/).

```load_module_no_frame
website.install_reflect
```

#### Launch Reflect server

Activate the virtual environment in which you installed Reflect. Start the Reflect server using the following command.

```load_module_no_frame
website.launch_server
```

By default, Reflect server will serve apps under [localhost:8080](http://localhost:8080) (you can specify another port using `--port` argument). The default page will be the server dashboard which gives you an overview of the server activity. 

![Reflect dash board](/website/reflect_dashboard.png)

You will be able to open apps located within the working directory by either by clicking the `Launch app` button or by typing their names in the address bar (more on this in the next section). You can change the default app using `--default-app` argument and a different app directory using `--app-folder` argument.


### Show me the code

Those who prefer to dive straight into the code first (and read carefully the tutorial later on... ;-) can clone the code snippets from the [tutorial](https://github.com/pytek-io/tutorial) and [demos](https://github.com/pytek-io/tutorial) inside the working directory and browse them using [/app/demos.app_explorer#tutorial/snippets](http://localhost:8080/app/demos.app_explorer#tutorial/snippets).

![App explorer](/website/app_explorer.png)
