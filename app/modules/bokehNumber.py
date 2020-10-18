import numpy as np
import random as random
from bokeh.io import curdoc, show
from bokeh.io.state import *
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, Text
from bokeh.core import enums
from bokeh.core.properties import Enum
from pylsl import StreamInlet, resolve_stream


def clear_plot():
    plot.renderers = []

def add_text():
    N = 9
    x = [1]
    y = [1]

    streams = resolve_stream()
    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    sample, timestamp = inlet.pull_sample()
    sample_data = sample[len(sample) - 9]

    text = [str(sample_data)]
    source = ColumnDataSource(dict(x=x, y=y, text=text))
    glyph = Text(x="x", y="y", text="text", text_font_size="100px", text_align="center", text_baseline="middle", angle=0, text_color="#96deb3")
    plot.add_glyph(source, glyph)
    print("Printed " + str(text[0]))

plot = Plot(
    title=None, plot_width=900, plot_height=600,
    min_border=0, toolbar_location=None, reset_policy="standard")

curdoc().add_root(plot)
curdoc().add_periodic_callback(clear_plot, 3000)
curdoc().add_periodic_callback(add_text, 3000)

show(plot)