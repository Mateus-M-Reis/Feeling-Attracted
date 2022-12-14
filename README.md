# Feeling Attracted

This is a simple attractor visualization made with [numpy](), [bqplot](), and [ipywidgets]().

[![Video](https://img.youtube.com/vi/tdsQpVRW67w/0.jpg)](https://www.youtube.com/watch?v=tdsQpVRW67w)

## Run it

Just create a virtualenvironment and run:

`pip install jupyterlab voila ipycanvas`

or, with conda:

`conda install -c conda-forge jupyterlab voila ipycanvas`.

I've run into problems with my [ipywidgets]() version. It may be fixed soon, but if your widgets are not appearing, run:

`pip install ipywidgets==7.6.3`

or, with conda:

`conda install -c conda-forge ipywidgets==7.6.3`.

You can run the notebook without even installing [voila](), but if you want to run the notebook as a instandalone web application, run it with:

`voila --enable_nbextensions=True --theme=Dark app.ipynb`

## Available Attractors right now:

- Clifford Attractor (fractral dream attractor)
