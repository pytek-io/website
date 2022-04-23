Below are the main steps to get Reflect up and running within a couple of minutes.

```load_module_no_frame
website.commands
```

#### Create a Python environment

As it is now standard practice, we highly recommend using a dedicated Python environment. We show how to do so with [virtualenv](https://docs.python.org/3/tutorial/venv.html) but any other alternatives (eg: [Miniconda](https://docs.conda.io/en/latest/miniconda.html), [poetry](https://python-poetry.org/)) will work just as well.
Create a working directory (you can use the name of your choice) then move to it. From this directory create dedicated (aka: virtual) Python environment using the `virtualenv` command. This will create a standalone Python environment inside a hidden local folder called `.venv`.

```load_module_no_frame
website.create_environment
```

> Once created a virtual environment `:mark:must` be activated using the `activate` script at the start of every terminal session. This is usually done for you transparently by most modern IDEs. You can use `which python` on \*.nix|Mac and `where.exe python` on Windows to confirm your local virtual environment is active.

#### Install Reflect modules

Download and decompress the Reflect archive file locally. Activate the virtual environment then install the Reflect packages located inside packages folder. You can double check that the installation was successful by using `python -c "import reflect"` command.

```load_module_no_frame
website.install_reflect
```

#### Launch Reflect server

Activate the virtual environment (so that Python kernel will use it) before launching Reflect app server using `reflect `command. By default, the server will serve apps under [localhost:8080](http://localhost:8080). It will display the server dashboard which gives you an overview of the server activity. You can change the default app using `--default-app` argument. You will be able to open apps `:mark:located within the working directory` either by clicking the `Launch app` button or by typing their names in the address bar (more on this in the next section).

```load_module_no_frame
website.launch_server
```

![Reflect dash board](/website/reflect_dashboard.png)

### Show me the code

Those who prefer to dive straight into the code first (and read carefully the manually later on... ;-) can clone the code snippets from the [tutorial](https://github.com/pytek-io/tutorial) and [demos](https://github.com/pytek-io/tutorial) inside the working directory and browse them using [/app/demos/app_explorer/main#tutorial/snippets](http://localhost:8080/app/demos/app_explorer/main#tutorial/snippets).

![App explorer](/website/app_explorer.png)
