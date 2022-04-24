[Bokeh](https://bokeh.org) is another popular Python + JavaScript charting solution. Reflect exposes the full python API but not the streaming functionality (We will support this in a more general way soon). To use Bokeh in Reflect you need to wrap your bokeh `Figure` in a reflect_bokeh `Figure` as shown below.

![bokeh](website/bokeh.png)

```read_file
demos/charts/bokeh/buble.py
```

You can also easily use [holoviews](https://holoviews.org) to easily generate advanced graphs as shown below.

![Verhulst Mandelbrot](website/bokeh_mandelbrot.png)

```read_file
demos/charts/bokeh/verhulst_mandelbrot.py
```
