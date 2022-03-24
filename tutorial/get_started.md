Below, you will find the relevant commands to setup a Reflect environment. You can also use the links to download the relevant files and install Reflect manually. 

```load_module_no_frame
website.cheat_sheet
```

### Setup a Python environment

We highly recommend creating a dedicated Python environment using [venv](https://docs.python.org/3/tutorial/venv.html) or any alternatives. The `virtualenv` command will create a copy of your Python environment (aka: virtual environment) under `.venv`. This virtual environment can be uninstalled by simply deleting its folder. 

### Install Python modules

The `activate` command ensures that the local virtual environment is active so that Reflect packages will be installed `:mark:in the local virtual environment`. You can use `which python` on \*.nix|Mac and `where.exe python` on windows to double check which Python environment is active before installing Reflect packages. You can also check that Reflect packages are correctly installed afterwards by using `python -c "import reflect"` command.

### Launch Reflect server

Reflect app server must also be launched from `:mark: the local virtual environment`. By default, the Reflect app server will serve your apps on port 8080. You will see the server dashboard under [localhost:8080](http://localhost:8080) as this is the default application. You can open apps by clicking the `Launch app` button or by typing their names in the address bar.

![Reflect dash board](/website/reflect_dashboard.png)

### Open apps
One can download demos and code snippets from this tutorial on [github](https://github.com/pytek-io). If you would prefer to dive straight into the code first (then reading the explanations carefully ;-), you can see the code snippets using [http://localhost:8080/app/tutorial/app_explorer#tutorial/snippets](http://localhost:8080/app/tutorial/app_explorer#tutorial/snippets). 

![App explorer](/website/app_explorer.png)