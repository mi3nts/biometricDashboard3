# ECG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure

class ecgModule:

    def __init__(self, source, source_num):

        # DEFINE FIGURE
        # ----------------------------------------------------------------------
        self.Fig = figure(plot_width=900, plot_height=600, y_range = [2000, 4000])
        self.Fig.xaxis.axis_label = 'Time Index'
        self.Fig.yaxis.axis_label = 'ECG (uV)'

        # configure visual properties on a plot's title attribute
        self.Fig.title.text = "Realtime ECG"
        self.Fig.title.align = "center"
        self.Fig.title.text_font_size = "30px"

        # DEFINE PLOT
        # ----------------------------------------------------------------------
        self.Plot = self.Fig.line(x='ecg_x', y='ecg_y', source=source, \
                              color='#FB9A99', line_width = 2)

        self.Text = self.Fig.text(x="hr_x", y="hr_y", text="hr", source=source_num, \
        text_font_size="30px", text_align="center", text_baseline="middle", text_color="#FF0000")
