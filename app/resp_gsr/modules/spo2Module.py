# SPO2 MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure
from bokeh.models.annotations import Title
from bokeh.models import HoverTool

class spo2Module:

    def __init__(self, source_num):

        # DEFINE FIGURE
        # ------------------------------------------------------------------------------
        self.Fig = figure(plot_width=150, plot_height=150)
        self.Fig.grid.grid_line_alpha = 0
        self.Fig.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
        self.Fig.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels
        self.Fig.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        self.Fig.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
        self.Fig.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        self.Fig.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
        self.Fig.border_fill_alpha = 1

        # remove toolbar and Bokeh logo
        self.Fig.toolbar.logo = None
        self.Fig.toolbar_location = None

        # add border to visualization
        self.Fig.outline_line_width = 1
        self.Fig.outline_line_alpha = 1
        self.Fig.outline_line_color = "black"

        self.Fig.add_tools(HoverTool(
        tooltips=[
            ("Normal", ">95%"),
            ("Hypoxia", "<94%")
        ]
        ))



        # DEFINE PLOT
        # ------------------------------------------------------------------------------
        self.Text = self.Fig.text(x="num_x", y="num_y", text="spo2", source=source_num,\
        text_font_size="30px", text_align="center", text_baseline="middle", text_color="#0032EC")

        # create title
        t = Title()
        t.text = 'SPO2 (%)'

        # set title
        self.Fig.title = t
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "20px"
