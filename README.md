# biometricDashboard3

## Number Visualization Module

### Quick Summary

This module dynamically displays numbers that are provided from the streaming layer. The numbers are updated every 2 seconds based on the latest data received from the streaming layer. It's implemented through python and visualization is done through bokeh, which takes care of the HTML and JS.

### How to Run

1. Send data via a streaming layer.
2. Run the following command in the directory where you have the file bokehNumber.py
    bokeh serve --show bokehNumber.py
3. After a few seconds, your browser will open a new window where you can see the live display of the numerical data.

### Documentation

#### Main function:

The main function calls the clear_plot function first to clear the bokeh plot and then immediately calls the add_text function to add the latest received number. It calls these functions through a bokeh method called add_periodic_callback which specifies to call these functions in 2 second increments.

#### clear_plot function:

This function clears the current bokeh plot by clearing the plot renderers.

#### add_text function:

This function has an inlet stream to receive the data being streamed. It then uses a text glyph to display that number on the bokeh plot dynamically.
