# ECG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI AND RYAN RAHMAN
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure
from bokeh.models import HoverTool

class ecgModule:

    def __init__(self, source, source_num):

        # DEFINE FIGURE
        # ----------------------------------------------------------------------
        self.Fig = figure(plot_width=1050, plot_height=600, y_range = [2000, 4000])
        self.Fig.xaxis.axis_label = 'Time Index'
        self.Fig.yaxis.axis_label = 'ECG (uV)'

        # configure visual properties on a plot's title attribute
        self.Fig.title.text = "Realtime ECG"
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "30px"

        # remove toolbar and Bokeh logo
        self.Fig.toolbar.logo = None
        self.Fig.toolbar_location = None

        # add tooltip
        self.Fig.add_tools(HoverTool(
            tooltips=[
                ("Normal Heart Rate", "60-100 bpm"),
                ("Tachycardia", ">100 bpm"),
                ("Bradycardia", "<60 bpm")
            ],
            mode='vline'
        ))


        # DEFINE PLOT
        # ----------------------------------------------------------------------
        self.Plot = self.Fig.line(x='ecg_x', y='ecg_y', source=source, \
                              color='#FB9A99', line_width = 2)

        self.Text = self.Fig.text(x="hr_x", y="hr_y", text="hr", source=source_num, \
        text_font_size="30px", text_align="center", text_baseline="middle", text_color="#FF0000")
