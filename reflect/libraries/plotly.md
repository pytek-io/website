[Plotly python](https://github.com/plotly/plotly.py) provides an interface to [Plotly.js](https://github.com/plotly/plotly.js/) which is one the most popular open-source JavaScript charting libraries. It provides a high level API called [Plotly Express](https://plotly.com/python/plotly-express/) as well as a more low level API based on the [Figure](https://plotly.com/python/figure-structure/). Both can be easily used in Reflect by wrapping the Plotly objects within a `reflect_plotly` `Graph` object.

![plotly_figure_factory](website/plotly_figure_factory.png)

```read_file
demos.charts.plotly.figure_factory
```

One can also use plotly_express as shown below.

![plotly_express](website/plotly_express.png)

```read_file
demos.charts.plotly.scatter_plotly_express
```

You can see a more advanced use case in [Stock history](internal:website.reflect.gallery/demos.stocks_history).
