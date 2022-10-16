#!/usr/bin/env python
# coding: utf-8

# # Feeling attracted
#
# An interactive vizualization for some cool attractors.

# #### Import some packages

# In[1]:


import numpy as np
from ipywidgets import (
    Dropdown,
    FloatSlider,
    VBox,
    AppLayout,
    HTMLMath,
    interactive_output
)
import bqplot.pyplot as plt


# #### Create the figure and the attractor selector

# In[108]:


figure = plt.figure(
    layout={'width': '100%', 'height': '100%'},
    animation_duration=1000,
    fig_margin={
        'top': 40,
        'bottom': 0,
        'left': 0,
        'right': 0
    }
)

attractor_selector = Dropdown(
    options=['Clifford'],
    index=0,
    value='Clifford',
    lavel='Select Attractor Model'
)


# ## Clifford Attractor

# #### Widgets

# In[106]:


clifford_a = FloatSlider(
        value=1.9, min=.1, max=2.0, step=.1, layout={'width': '99%'})
clifford_b = FloatSlider(
        value=1.9, min=.1, max=2.0, step=.1, layout={'width': '99%'})
clifford_c = FloatSlider(
        value=1.9, min=.1, max=2.0, step=.1, layout={'width': '99%'})
clifford_d = FloatSlider(
        value=.8, min=0, max=2.0, step=.1, layout={'width': '99%'})
clifford_wids = VBox([
    clifford_a,
    clifford_b,
    clifford_c,
    clifford_d,
])
clifford_formula = HTMLMath("""
        <h2>Clifford Attractor (Fractral Dream)</h1>
        $$
        x_{n+1} = sin(ay_n) + c.cos(ax_n)\\\\
        y_{n+1} = sin(bx_n) + d.cos(by_n)
        $$""")


# ### Updading clifford figure

# In[109]:


def clifford_trajectory(a, b, c, d, n=25000):
    xs, ys = np.zeros(n), np.zeros(n)
    for i in np.arange(n-1):
        xs[i+1] = np.sin(a * ys[i]) + c * np.cos(a * xs[i])
        ys[i+1] = np.sin(b * xs[i]) + d * np.cos(b * ys[i])
    return xs, ys


xs, ys = clifford_trajectory(1.9, 1.9, 1.9, 0.8)
plt.scatter(
        xs, ys, stroke=None, default_size=1, colors=['white'], opacities=[.2])
figure.axes[0].grid_lines = 'none'
figure.axes[1].grid_lines = 'none'


def clifford_plot(a=1.9, b=1.9, c=1.9, d=0.8):
    xs, ys = clifford_trajectory(a, b, c, d)
    figure.marks[0].x = xs
    figure.marks[0].y = ys


update_clifford = interactive_output(clifford_plot, {
    'a': clifford_a,
    'b': clifford_b,
    'c': clifford_c,
    'd': clifford_d,
}),


# ## UI

# In[110]:


panel = VBox([
    HTMLMath("<Br>"),
    attractor_selector,
    HTMLMath("<Br><Br>"),
    clifford_wids,
    HTMLMath("<Br><Br>"),
    clifford_formula,
])

ui = AppLayout(
    header=None,
    left_sidebar=panel,
    center=figure,
    right_sidebar=None,
    footer=None,
    layout={
        'width': '100%',
        'height': '90vh',
        'overflow_x': 'hidden',
        'overflow_y': 'hidden',
    }
)
ui
