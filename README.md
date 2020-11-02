# biometricDashboard3
# What is the ECG Module?
The Electrocardiography(ECG) module shows the electrical signals in the heart over time. It provides information about heart rate and rhythm, and shows if there is enlargement of the heart due to high blood pressure (hypertension) or evidence of a previous heart attack (myocardial infarction). An ECG can also detect arrhythmias, which is when a heart beats too slowly, quickly, or irregularly. Additionally, the ECG can determine whether there's inadequate blood and oxygen supply to the heart. The module also will show the heart rate over time in a numerical fashion above the electrical signals line. 

# What does the ECG Module show?
An ECG can be analyzed by studying the components of the waveform. The first initial upward tracing is the p wave, which indicates atrial contraction. The QRS complex, which begins with a small downward deflection,Q, followed by an upward deflection, which is called an R peak, and then a downward deflection S. The QRS complex indicates ventricular depolarization and contraction. Finally, the T wave, which is normally a smaller upwards waveform, representing ventricular repolarization.

# Heart Rate Info
- Maximum heart rate = 220 – age
- Moderate exercise intensity: 50% to about 70% of your maximum heart rate
- Vigorous exercise intensity: 70% to about 85% of your maximum heart rate
  -Sleep: 40-50 bpm
  -Rest: 60-100 bpm
  -Walking: 110-120 bpm
- Exercise is the best way to both lower your resting heart rate and increase your maximum heart rate and aerobic capacity
-Heart Rate Conditions 
  -Normal: 60-100 bpm
  -Tachycardia: > 100 bpm
  -Bradycardia: < 60 bpm
  
# How does the ECG Module work?
It's initially called upon in the main.py with the parameter source which is a columnDataSource that continuously updates the x & y values of the ecg plot. In addition, there's another columnDataSource source_num that continuously updates the x,y, and actual value of heart rate so it's kept in the right corner of the plot.  The main plot is outlined with the Bokeh object Figure, which has attributes like title and axis labeling to make a complete visualization. The ECG line is placed on the graph by using the bokeh class Plot, which takes in parameters ‘ecg_x’, ‘ecg_y’, and source. The heart rate is added in a similar fashion by using the bokeh class glyph, which takes in the parameters ‘hr_x’, ‘hr_y’ and ‘hr’ and source_num. 


