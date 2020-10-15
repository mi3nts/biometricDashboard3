# ECG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure,show
from bokeh.models import Title, Text
import random as random
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

class ecgModule:

    def __init__(self, source):

        # DEFINE FIGURE
        # ----------------------------------------------------------------------
        
        #creates frame for visualization 
        self.Fig = figure(plot_width=900, plot_height=600, y_range = [2000, 4000], tools="hover")
        self.Fig.xaxis.axis_label = 'Time Index'
        self.Fig.yaxis.axis_label = 'ECG (uV)'
        # configure visual properties on a plot's title attribute
        self.Fig.title.text = "Realtime ECG"
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "40px"
        heartRates = "Heart Rates: Normal: 60-100 bpm, Tachycardia: >100 bpm, Bradycardia: <60 bpm"
        self.Fig.add_layout(Title(text=heartRates, align="center"), "below")
        N = 9
        text = [str(random.randint(0, N))]
        #source2 = ColumnDataSource(dict(x=x, y=y, text=text))
        #glyph = Text(x="x", y="y", text="text", text_font_size="100px", text_align="center", text_baseline="middle", angle=0, text_color="#96deb3")
        #self.Plot = self.Fig.text(x=300, y=300, text="text", text_font_size="100px", text_align="center", text_baseline="middle", angle=0, text_color="#96deb3")
        #print("plotted")
        #self.Plot = self.Fig.add_glyph(Text(x=200, y=200, text=text, text_font_size="20px", text_align="right", text_baseline="middle", angle=0, text_color="#96deb3"))
        # DEFINE PLOT
        # ----------------------------------------------------------------------
        
        #plot is created using source data thats passedS when class is called
        self.Plot = self.Fig.line(x='ecg_x', y='ecg_y', source=source, \
                              color='#FB9A99', line_width = 2)
        print("line")
        self.Plot = self.Fig.text(x=300, y=300, text="text", text_font_size="200px", text_align="center", text_baseline="middle", angle=0, text_color="blue")
        print("plotted")
        
        