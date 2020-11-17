+++
title = "Text Visualizations"
weight = 4
bg = "bg-gradient-white"
+++
<!-- : .wrap -->

### **Text Visualizations**
##### HRV
The HRV module leverages open source QRS detection code that uses the Pan-Tompkins QRS peak detection algorithm. The algorithm calculates beat-to-beat (RR) intervals and uses these intervals to calculate HRV values. Calculation is done for the rMSSD, SDNN, and SDSD, but the visualization shows the rMSSD value. 
##### RR
With the RR interval calculated from the HRV module, the RR module calculates the respiration rate using one of two methods: Welch's (default) and Fourier transformation. Welch's alrogithm gives the number of seconds per breathing cycle (in Hz) and this number is then used to calculate breaths per minute.
##### GSR
Skin conductance is captured using skin electrodes which are easy to apply. GSR devices typically consist of two electrodes, an amplifier (to boost signal amplitude), and a digitizer (to transfer the analog raw signal into binary data streams).
##### Sp02
Sp02 is measured using pulse oximeters that use light sensors to record how much blood is carrying oxygen and how much blood is not. Oxygen-saturated hemoglobin is darker than non-oxygen saturated hemoglobin, which allows the pulse oximeter to detect minute variations in the blood and translate that into a reading. 

{{< div class="bg-custom2 shadow" >}}
<!--: .flexblock gallery1 -->
- {{< gallery title="HRV" src="images/text-vis/hrv.gif" >}}<h2>Heart Rate Variability</h2><p>(measured in milliseconds)</p>{{< /gallery >}}
- {{< gallery title="RR" src="images/text-vis/rr.gif" >}}<h2>Respiration Rate</h2><p>(measured by breaths per minute)</p>{{< /gallery >}}
- {{< gallery title="GSR" src="images/text-vis/gsr.gif" >}}<h2>GSR</h2><p>(measured in micro-Siemens)</p>{{< /gallery >}}
- {{< gallery title="Sp02" src="images/text-vis/spo2.gif" >}}<h2>Sp02</h2><p>(measured as percentage of haemoglobin)</p>{{< /gallery >}}
{{< /div >}}