The technologies below have been originally built by and for the scientific community. They are mostly used for exploratory work, and to some extent also used to build simple business apps.
Thanks to its agnostic architecture, Reflect overlaps significantly with these frameworks. This allows for a seamless integration of existing prototypes or simple dashboards into full blown business apps at scale.

## Plotly

[Plotly](https://plotly.com/) is a world leader in data visualization solutions for scientific and business purposes. It allows you to build simple data visualization web apps with mininmal coding effort thanks to its vast collection of precanned templates, which can be automatically converted to nice looking pdf reports.

#### Plotly strengths

- Widely used within the scientific community
- Beautiful dashboards and reports at your fingertips

#### How Reflect compares

- Exposes the most popular graph libraries including [Plotly JS](https://plotly.com/javascript/) and [Altair](https://altair-viz.github.io/#)
- Strong support for realtime display thanks to its asynchronous design
- Allows to define advanced behaviours in a callback free style
- No out of the box report generation

## Streamlit

[Streamlit](https://streamlit.io/) has mainly been designed for interactive scientific data visualization, in particular AI models. This is the perfect solution for users who want to render AI results with very little effort.

#### Streamlit strengths

- Extremely terse API allowing for a linear construction of apps laid out in a predefined fashion making it easy to create ad hoc apps by developers of all levels
- Strong support for medical and AI model visualization

#### How Reflect compares

- Reflect provides a similar callback free API but within a much more composable and structured paradigm making for a much more versatile app framework
- Strong support for realtime display thanks to its asynchronous design
- Provides developers with much more control over advanced business app design

## Jupyter

[Jupyter](https://jupyter.org/) provides a rather unique way to share scientific results. It is very popular among the scientific community as well as in finance. It is rather unique in that it allows to execute code and display the results alongside extra content making for highly interactive scientific papers (aka Notebook). It is now being extended and commercially supported by a few companies such as [DeepNote](https://deepnote.com), [Hex](https://deepnote.com), [Colab](https://colab.research.google.com).

#### Jupyter strengths

- Very convenient for data exploration, scientific research and publication
- Notebooks can be exported to a variety of formats
- Parallel computing support

#### How Reflect compares

- Relies on a similar Python kernel approach
- Allows to build very powerful and interactive data exploration tools at an industrial scale

## Bokeh
[Bokeh](https://bokeh.org) is a Python visualization library which provides functionalities allowing to build simple "Data applications", dashboards, streaming applications, etc. 

#### Bokeh strengths

- Extremely simple to use, build data apps in a few lines of code
- Allows to define customized dashboards easily.
- Supports large data set streaming

#### How Reflect compares

- Allows to define much more complex layouts/behaviours
- Does not support large data set streaming

## Panel
[Panel](https://panel.holoviz.org) extends Bokeh backend to support the most common Python charting libraries (Plotly, Altair, etc). 

