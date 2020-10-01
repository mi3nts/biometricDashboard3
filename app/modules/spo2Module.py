# SPO2 MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure

class spo2Module:

    def __init__(self):

        # DEFINE FIGURE
        # ------------------------------------------------------------------------------
        self.Fig = figure(plot_width=300, plot_height=300)
        self.Fig.grid.grid_line_alpha = 0
        self.Fig.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
        self.Fig.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels
        self.Fig.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        self.Fig.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
        self.Fig.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        self.Fig.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
        self.Fig.border_fill_alpha = 1

        # DEFINE PLOT
        # ------------------------------------------------------------------------------
        self.Plot = self.Fig.text(x=[1], y=[1], text=['SPO2'], text_align='center')
