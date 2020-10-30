# biometricDashboard3

## Number Visualization Module

### Quick Summary

This module dynamically displays numbers that are provided from the streaming layer. The numbers are updated every 3 seconds based on the latest data received from the streaming layer. It's implemented through python and visualization is done through bokeh, which takes care of the HTML and JS.

### How to Run

1. Send data via a streaming layer.
2. Run the following command in the directory where you have the file bokehNumber.py
    bokeh serve --show bokehNumber.py
3. After a few seconds, your browser will open a new window where you can see the live display of the numerical data.

### Documentation

#### Main function:

The main function calls the clear_plot function first to clear the bokeh plot and then immediately calls the add_text function to add the latest received number. It calls these functions through a bokeh method called add_periodic_callback which specifies to call these functions in 3 second increments.

#### clear_plot function:

This function clears the current bokeh plot by clearing the plot renderers.

#### add_text function:

This function has an inlet stream to receive the data being streamed. It then uses a text glyph to display that number on the bokeh plot dynamically.

## GSR Module

### Quick Summary

The galvanic skin response (GSR) refers to changes in sweat gland activity that are reflective of the intensity of our emotional state, otherwise known as emotional arousal. Our level of emotional arousal changes in response to the environment we’re in – if something is scary, threatening, joyful, or otherwise emotionally relevant, then the subsequent change in emotional response that we experience also increases eccrine sweat gland activity.

### Why do we care?

Skin conductance is not under conscious control. Instead, it is modulated autonomously by sympathetic activity which drives aspects of human behavior, as well as cognitive and emotional states. Skin conductance therefore offers direct insights into autonomous emotional regulation. It can be used as an additional source of insight to validate self-reports, surveys, or interviews of participants within a study.

### How do you measure GSR?

The amount of sweat glands varies across the human body, but is the highest in hand and foot regions (200–600 sweat glands per cm2), where the GSR signal is typically collected from. Skin conductance is captured using skin electrodes which are easy to apply. GSR devices typically consist of two electrodes, an amplifier (to boost signal amplitude), and a digitizer (to transfer the analog raw signal into binary data streams). Wireless GSR devices further contain data transmission modules for communication with the recording computer. Data is acquired with sampling rates between 1 – 10 Hz and is measured in units of micro-Siemens (μS). They typically range from 10 - 50 μS. 

## SPO2 Module

### Quick Summary

Oxygen saturation is the fraction of oxygen-saturated hemoglobin relative to total hemoglobin (unsaturated + saturated) in the blood. The human body requires and regulates a very precise and specific balance of oxygen in the blood. Normal arterial blood oxygen saturation levels in humans are 95–100 percent. If the level is below 90 percent, it is considered low and called hypoxemia.

### Why do we care?

Arterial blood oxygen levels below 80 percent may compromise organ function, such as the brain and heart, and should be promptly addressed. Continued low oxygen levels may lead to respiratory or cardiac arrest. There is also a visible effect on the skin, known as cyanosis due to the blue (cyan) tint the skin takes on.

### How do you measure SPO2?

Through pulse oximeters, which function by using light sensors to record how much blood is carrying oxygen and how much blood is not. Oxygen-saturated hemoglobin is darker to the naked eye than non-oxygen saturated hemoglobin, and this phenomenon allows the highly sensitive sensors of the pulse oximeter to detect minute variations in the blood and translate that into a reading. Normal ranges are between 95–100 percent.


