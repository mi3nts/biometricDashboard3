import numpy as np
import random as random
from bokeh.io import curdoc, show
from bokeh.io.state import *
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, Text
from bokeh.core import enums
from bokeh.core.properties import Enum

def clear_plot():
    reset(plot)
    '''source2 = ColumnDataSource(dict(x=[], y=[], text=[]))
    glyph2 = Text(x="x", y="y", text="text", text_font_size="200px", text_align="center", text_baseline="middle",
                 angle=0, text_color="#96deb3")
    plot.add_glyph(source2, glyph2)
    print("Cleared")'''

def add_text():
    N = 9
    x = [1]
    y = [1]
    text = [str(random.randint(0, N))]
    source = ColumnDataSource(dict(x=x, y=y, text=text))
    glyph = Text(x="x", y="y", text="text", text_font_size="200px", text_align="center", text_baseline="middle", angle=0, text_color="#96deb3")
    plot.add_glyph(source, glyph)
    print("Printed " + str(text[0]))

plot = Plot(
    title=None, plot_width=900, plot_height=600,
    min_border=0, toolbar_location=None, reset_policy="standard")

curdoc().add_root(plot)
curdoc().add_periodic_callback(clear_plot, 2000)
curdoc().add_periodic_callback(add_text, 2000)

show(plot)