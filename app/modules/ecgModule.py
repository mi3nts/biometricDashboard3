# ECG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
<<<<<<< HEAD
from bokeh.plotting import figure
from bokeh.models import HoverTool
=======
from bokeh.plotting import figure,show
from bokeh.io import curdoc, show 
from bokeh.models import Title, Text
import random as random
import time
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
>>>>>>> 80fa93f1a876144619242e76b527441003168ca8

class ecgModule:
    def add_text(self, num):
         N = 9
         text = [str(random.randint(0, N))]
         print("called")
         self.Text = self.Fig.text(x=num, y=3500, text=text, text_font_size="200px", text_align="center", text_baseline="middle", angle=0, text_color="blue")

    def __init__(self, source, source_num):

        # DEFINE TOOLTIPS

        ry = "fasfdsfd"
        TOOLTIPS = [
            ("(x,y", ry)
        ]

        # DEFINE FIGURE
        # ----------------------------------------------------------------------
<<<<<<< HEAD
        self.Fig = figure(plot_width=900, plot_height=600, y_range = [2000, 4000])
        #tooltips=TOOLTIPS
        
        self.Fig.add_tools(HoverTool(
            tooltips=[
                ("Normal Heart Rate", "60-100 bpm"),
                ("Tachycardia", ">100 bpm"),
                ("Bradycardia", "<60 bpm")
            ],
            mode='vline'
        )) 
        
=======
        
        #creates frame for visualization 
        self.Fig = figure(plot_width=900, plot_height=600, y_range = [2000, 4000], tools="hover")
>>>>>>> 80fa93f1a876144619242e76b527441003168ca8
        self.Fig.xaxis.axis_label = 'Time Index'
        self.Fig.yaxis.axis_label = 'ECG (uV)'
<<<<<<< HEAD
        # configure visual properties on a plot's title attribute
        self.Fig.title.text = "Realtime ECG"
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "40px"
        heartRates = "Heart Rates: Normal: 60-100 bpm, Tachycardia: >100 bpm, Bradycardia: <60 bpm"
        self.Fig.add_layout(Title(text=heartRates, align="center"), "below")
        
=======

        # configure visual properties on a plot's title attribute
        self.Fig.title.text = "Realtime ECG"
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "30px"


        # DEFINE PLOT
>>>>>>> e7ef14f96a5fe4d3b75b285bef2811aa3160aec7
        # ----------------------------------------------------------------------
        
        #plot is created using source data thats passedS when class is called
        self.Plot = self.Fig.line(x='ecg_x', y='ecg_y', source=source, \
                              color='#FB9A99', line_width = 2)
<<<<<<< HEAD
   
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
        
        
        
=======


        self.Text = self.Fig.text(x="hr_x", y="hr_y", text="hr", source=source_num, \
        text_font_size="30px", text_align="center", text_baseline="middle", text_color="#FF0000")
>>>>>>> e7ef14f96a5fe4d3b75b285bef2811aa3160aec7
