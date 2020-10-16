# ECG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure,show
from bokeh.io import curdoc, show 
from bokeh.models import Title, Text
import random as random
import time
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

class ecgModule:
    def add_text(self, num):
         N = 9
         text = [str(random.randint(0, N))]
         print("called")
         self.Text = self.Fig.text(x=num, y=3500, text=text, text_font_size="200px", text_align="center", text_baseline="middle", angle=0, text_color="blue")

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
        
        # ----------------------------------------------------------------------
        
        #plot is created using source data thats passedS when class is called
        self.Plot = self.Fig.line(x='ecg_x', y='ecg_y', source=source, \
                              color='#FB9A99', line_width = 2)
   
        num = 300
        N = 9
        text = [str(random.randint(0, N))]
        #self.Text = self.Fig.text(x=num, y=3500, text=text, text_font_size="200px", text_align="center", text_baseline="middle", angle=0, text_color="blue")
        curdoc().add_periodic_callback(self.add_text(num), 2000)
        #num = num + 100

        """
        self.add_text(num)
        num = num + 200
        self.add_text(num)
        """
        """
        while True:
            self.add_text(num)
            time.sleep(60)
            num = num + 100
        """    
        
        
        