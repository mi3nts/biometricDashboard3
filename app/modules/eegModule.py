# EEG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure


class eegModule:

    def __init__(self):

        # DEFINE FIGURES
        # ------------------------------------------------------------------------------
        self.DeltaFig = figure(plot_width=300, plot_height=300)
        self.ThetaFig = figure(plot_width=300, plot_height=300)
        self.AlphaFig = figure(plot_width=300, plot_height=300)
        self.TotalFig = figure(plot_width=300, plot_height=300)

        # DEFINE PLOTS
        # ------------------------------------------------------------------------------
        self.DeltaPlot = self.DeltaFig.circle(\
        x=[0,1,2,3,4,5], y=[1,2,1,0,2,1], \
        color='#eb3434', fill_alpha=0.2, size=10)

        self.ThetaPlot = self.ThetaFig.circle(\
        x=[0,1,2,3,4,5], y=[1,2,1,0,2,1], \
        color='#4937d4', fill_alpha=0.2, size=10)

        self.AlphaPlot = self.AlphaFig.circle(\
        x=[0,1,2,3,4,5], y=[1,2,1,0,2,1], \
        color='#5be605', fill_alpha=0.2, size=10)

        self.TotalPlot = self.TotalFig.circle(\
        x=[0,1,2,3,4,5], y=[1,2,1,0,2,1], \
        color='#a424b3', fill_alpha=0.2, size=10)
