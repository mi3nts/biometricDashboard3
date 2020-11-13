# biometricDashboard3

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Modules](#modules)
    * [EEG Module](#eeg-module)
    * [ECG Module](#ecg-module)
    * [HRV Module](#hrv-module)
    * [RR Module](#rr-module)
    * [GSR Module](#gsr-module)
    * [Sp02 Module](#sp02-module)
- [Attribution](#attribution)
- [Authors](#authors)
- [License](#license)

    
## Introduction


## Installation

## Modules

### EEG Module

#### What is an EEG and how is it measured?
The Electroencephologram (EEG) evaluates brain activity. Electrodes are placed on the scalp and measure the electrical impulses that occur in the brain and record the results. The results are in the form of wave patterns that can be evaluated at different frequency bands. The frequency bands we focused on for this project are the delta band (around 1-4 Hz), the theta band (around 4-8 Hz), the alpha band (around 8-12 Hz), and the total band (which is the sum of the delta, theta, and alpha bands). The delta band is usually associated with low brain activity and usually the frequency band where deep sleep and depth of sleep are studied. The theta band is usually assoicated with slow activity such as intuition or daydreaming, but the activity is faster than the delta band. The alpha band is usually associated with high activity such as deep thought, concentration, or confusion. Certain brain disorders such as seizures, brain tumors, and head injuries can be detected from studying the results of an EEG.

#### What does the EEG Module Show
The EEG module shows the different heatmaps of the brain and the activity occurring for the different frequency bands. There are 64 electrode sensors placed on the subject and the data is gathered from the electrical impulses that the electrodes measure. The goal for the EEG visualization is to plot the heatmaps for the delta band, theta band, alpha band, and total band, and show the electrical activity that is being picked up by the different sensors. To do this, data is continuously read in from a streaming layer and part of this data contains the voltages measured by the 64 different EEG sensors. The voltages for the 64 different sensors are then retrieved, and the voltages collected over time from the streaming layer are converted to frequencies using welch's method, which converts the voltages in the time domain to their corresponding power at the corresponding frequency. After this, the power spectrum for the delta band, theta band, alpha band, and total band are retreived from the output of the welch function, and are then plotted on the heatmaps at their respective frequency bands. The heatmaps are then updated each time new data is gathered from the streaming layer. From the heatmaps, the frequency of brain activity can be seen for the different frequency bands, along with the location of activity in the brain as the 64 different sensors are plotted. The heatmaps can then be studied to get information on brain activity at that frequency band and to diagnose any brain disorders.

The code for the EEG visualization is found under the modules directory and is in the file eegModule.py. The MNE library is used to plot the heatmaps, and several strucutures such as ColumnDataSource and Figure are used from Bokeh to plot the heatmaps and update them continuously.

### ECG Module

#### What is the ECG Module?
The Electrocardiography (ECG) module shows electrical signals in the heart over time. It provides information about heart rate and rhythm, and shows if there is enlargement of the heart due to high blood pressure (hypertension) or evidence of a previous heart attack (myocardial infarction). An ECG can also detect arrhythmias, which is when a heart beats too slowly, quickly, or irregularly. Additionally, ECG can determine whether there is inadequate blood and oxygen supply to the heart. The module also will show the heart rate over time in a numerical fashion above the electrical signal. 

#### What does the ECG Module show?
ECG can be analyzed by studying the components of the waveform. The first initial upward tracing is the P wave, which indicates atrial contraction. The QRS complex, which begins with a small downward deflection, Q, followed by an upward deflection, which is called an R peak, and then a downward deflection, S. The QRS complex indicates ventricular depolarization and contraction. Finally, the T wave, which is normally a smaller upwards waveform, representing ventricular repolarization.

#### Heart Rate Info
- Exercise is the best way to both lower your resting heart rate and increase your maximum heart rate and aerobic capacity
- Maximum Heart Rate = 220 – age
- Heart Rates During Activites: 
  * Moderate exercise intensity: 50% to about 70% of your maximum heart rate
  * Vigorous exercise intensity: 70% to about 85% of your maximum heart rate
  * Sleep: 40-50 bpm
  * Rest: 60-100 bpm
  * Walking: 110-120 bpm
- Heart Rate Conditions: 
  * Normal: 60-100 bpm
  * Tachycardia: > 100 bpm
  * Bradycardia: < 60 bpm
  
#### How does the ECG Module work?
It's initially called upon in the main.py with the parameter source which is a columnDataSource that continuously updates the x & y values of the ecg plot. In addition, there's another columnDataSource source_num that continuously updates the x,y, and actual value of heart rate so it's kept in the right corner of the plot.  The main plot is outlined with the Bokeh object Figure, which has attributes like title and axis labeling to make a complete visualization. The ECG line is placed on the graph by using the bokeh class Plot, which takes in parameters ‘ecg_x’, ‘ecg_y’, and source. The heart rate is added in a similar fashion by using the bokeh class glyph, which takes in the parameters ‘hr_x’, ‘hr_y’ and ‘hr’ and source_num. 




### HRV Module

### RR Module

### GSR Module

#### Quick Summary

The galvanic skin response (GSR) refers to changes in sweat gland activity that are reflective of the intensity of our emotional state, otherwise known as emotional arousal. Our level of emotional arousal changes in response to the environment we’re in – if something is scary, threatening, joyful, or otherwise emotionally relevant, then the subsequent change in emotional response that we experience also increases eccrine sweat gland activity.

#### Why do we care?

Skin conductance is not under conscious control. Instead, it is modulated autonomously by sympathetic activity which drives aspects of human behavior, as well as cognitive and emotional states. Skin conductance therefore offers direct insights into autonomous emotional regulation. It can be used as an additional source of insight to validate self-reports, surveys, or interviews of participants within a study.

#### How do you measure GSR?

The amount of sweat glands varies across the human body, but is the highest in hand and foot regions (200–600 sweat glands per cm2), where the GSR signal is typically collected from. Skin conductance is captured using skin electrodes which are easy to apply. GSR devices typically consist of two electrodes, an amplifier (to boost signal amplitude), and a digitizer (to transfer the analog raw signal into binary data streams). Wireless GSR devices further contain data transmission modules for communication with the recording computer. Data is acquired with sampling rates between 1 – 10 Hz and is measured in units of micro-Siemens (μS). They typically range from 10 - 50 μS. 

### Sp02 Module

#### Quick Summary

Oxygen saturation is the fraction of oxygen-saturated hemoglobin relative to total hemoglobin (unsaturated + saturated) in the blood. The human body requires and regulates a very precise and specific balance of oxygen in the blood. Normal arterial blood oxygen saturation levels in humans are 95–100 percent. If the level is below 90 percent, it is considered low and called hypoxemia.

#### Why do we care?

Arterial blood oxygen levels below 80 percent may compromise organ function, such as the brain and heart, and should be promptly addressed. Continued low oxygen levels may lead to respiratory or cardiac arrest. There is also a visible effect on the skin, known as cyanosis due to the blue (cyan) tint the skin takes on.

#### How do you measure SPO2?

Through pulse oximeters, which function by using light sensors to record how much blood is carrying oxygen and how much blood is not. Oxygen-saturated hemoglobin is darker to the naked eye than non-oxygen saturated hemoglobin, and this phenomenon allows the highly sensitive sensors of the pulse oximeter to detect minute variations in the blood and translate that into a reading. Normal ranges are between 95–100 percent.

## Attribution


## Authors


## License
=======



