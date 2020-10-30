# EEG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# EEG MODULE

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import bokeh module
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import numpy as np
import scipy.signal as sps
import mne
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt

class eegModule:

    def __init__(self):
        
        # DEFINE FIGURES
        # ------------------------------------------------------------------------------
        self.DeltaFig = figure(plot_width=350, plot_height=350)
        self.ThetaFig = figure(plot_width=350, plot_height=350)
        self.AlphaFig = figure(plot_width=350, plot_height=350)
        self.TotalFig = figure(plot_width=350, plot_height=350)

        # remove toolbars and Bokeh logo
        self.DeltaFig.toolbar.logo = None
        self.DeltaFig.toolbar_location = None
        self.ThetaFig.toolbar.logo = None
        self.ThetaFig.toolbar_location = None
        self.AlphaFig.toolbar.logo = None
        self.AlphaFig.toolbar_location = None
        self.TotalFig.toolbar.logo = None
        self.TotalFig.toolbar_location = None

        # add border to visualizations
        self.DeltaFig.outline_line_width = 1
        self.DeltaFig.outline_line_alpha = 1
        self.DeltaFig.outline_line_color = "black"

        self.ThetaFig.outline_line_width = 1
        self.ThetaFig.outline_line_alpha = 1
        self.ThetaFig.outline_line_color = "black"

        self.AlphaFig.outline_line_width = 1
        self.AlphaFig.outline_line_alpha = 1
        self.AlphaFig.outline_line_color = "black"

        self.TotalFig.outline_line_width = 1
        self.TotalFig.outline_line_alpha = 1
        self.TotalFig.outline_line_color = "black"
        
        # DEFINE VARIABLES
        # ------------------------------------------------------------------------------
        self.eeg_data = np.zeros((64, 64), float)
        
        self.global_max = 1
        
        # variables for mne evoked structure
        self.ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T7', 'T8', 
            'P7', 'P8', 'Fz', 'Cz', 'Pz', 'Oz', 'FC1', 'FC2', 'CP1', 'CP2', 'FC5', 'FC6', 
            'CP5', 'CP6', 'FT9', 'FT10', 'FCz', 'AFz', 'F1', 'F2', 'C1', 'C2', 'P1', 'P2', 
            'AF3', 'AF4', 'FC3', 'FC4', 'CP3', 'CP4', 'PO3', 'PO4', 'F5', 'F6', 'C5', 'C6', 
            'P5', 'P6', 'AF7', 'AF8', 'FT7', 'FT8', 'TP7', 'TP8', 'PO7', 'PO8', 'Fpz', 'CPz', 'POz', 'TP10']
        
        
        self.ch_types = ['eeg' for j in range(64)]
        
        self.info = mne.create_info(ch_names=self.ch_names, sfreq=500, ch_types=self.ch_types)
        self.info.set_montage("standard_1020") # for sensor locations
        self.evoked = mne.EvokedArray(self.eeg_data, self.info) # evoked structure for plotting topomaps
        
        # column data source for updating document
        self.source_images = ColumnDataSource({'delta_array': [], 
                                        'theta_array': [],
                                        'alpha_array': [], 
                                        'total_array': []})
        
        self.DeltaFig.image_rgba(image='delta_array', x=0, y=0, dw=350, dh=350, source=self.source_images)
        self.ThetaFig.image_rgba(image='theta_array', x=0, y=0, dw=350, dh=350, source=self.source_images)
        self.AlphaFig.image_rgba(image='alpha_array', x=0, y=0, dw=350, dh=350, source=self.source_images)
        self.TotalFig.image_rgba(image='total_array', x=0, y=0, dw=350, dh=350, source=self.source_images)
    
    def getFreqBandOrValue(self, data, new_data, freq_value, global_max):
        # delete first row
        data = np.delete(data, 0, 0)
        
        # add new_data as a row at the end of data. columns=electrodes rows=timestep
        data = np.vstack([data, new_data])
        
        # transpose the data numpy array
        data = np.transpose(data)
        
        # compute power spectrum of data
        f, ps = sps.welch(data, fs=26, nperseg=64)
        # print the power spectrum
        #print("ps", ps)
        # print the frequency
        #print("f", f)
        
        extract_amplitude = []
        # delta freq band
        if freq_value == -1:
            extract_amplitude = self.getAmplitudesByFrequencyBand(ps, 0)
        # theta freq band
        elif freq_value == -2:
            extract_amplitude = self.getAmplitudesByFrequencyBand(ps, 1)
        # alpha freq band
        elif freq_value == -3:
            extract_amplitude = self.getAmplitudesByFrequencyBand(ps, 2)
        # specific freq value wanted
        else:
            interval = [freq_value - 0.5, freq_value + 0.5]
            start_index = -1
            end_index = -1
            for i in range(len(f)):
                if interval[0] <= f[i] <= interval[1]:
                    if start_index == -1:
                        start_index = i
                    else:
                        end_index = i
    
            print("start ", start_index, f[start_index],
                  "end ", end_index, f[end_index])
            extract_amplitude = ps[:, start_index:end_index]
            
        # create a numpy array called temp
        temp = np.asarray(extract_amplitude)
        
        # temp holds mean of each row in extractAmplitude
        temp = np.mean(temp, axis=1)
            
        # calculate the maximum of the two values - called local_max
        local_max = max(np.amax(temp), global_max)
    
        # traverse through elements in the temp nuumpy array
        for i in range(len(temp)):
            # normalize all amplitudes by the global max
            temp[i] = temp[i] / local_max
        # return the temp, local_max, and data numpy arrays
        return [temp, local_max, data]


    def getAmplitudesByFrequencyBand(self, ps, x):
        # if delta freq wanted
        if x == 0:
            return ps[:, 3:9]
        # if theta freq wanted
        elif x == 1:
            return ps[:, 10:19]
        # if alpha freq wanted
        elif x == 2:
            return ps[:, 20:29]

    def getImageArray(self, figure): # get the array from the matplotlib figure passed in
        canvas = FigureCanvasAgg(figure)

        canvas.draw()
    
        buf = canvas.buffer_rgba()
    
        # ... convert to a NumPy array ...
        X = np.asarray(buf, dtype=np.uint8)

        return X
        
    def visualize(self, i, source):
        # get sample data from column data source
        sample_data = [source.data['eeg_1'][0], source.data['eeg_2'][0], source.data['eeg_3'][0],
                       source.data['eeg_4'][0], source.data['eeg_5'][0], source.data['eeg_6'][0],
                       source.data['eeg_7'][0], source.data['eeg_8'][0], source.data['eeg_9'][0],
                       source.data['eeg_10'][0], source.data['eeg_11'][0], source.data['eeg_12'][0],
                       source.data['eeg_13'][0], source.data['eeg_14'][0], source.data['eeg_15'][0],
                       source.data['eeg_16'][0], source.data['eeg_17'][0], source.data['eeg_18'][0],
                       source.data['eeg_19'][0], source.data['eeg_20'][0], source.data['eeg_21'][0],
                       source.data['eeg_22'][0], source.data['eeg_23'][0], source.data['eeg_24'][0],
                       source.data['eeg_25'][0], source.data['eeg_26'][0], source.data['eeg_27'][0],
                       source.data['eeg_28'][0], source.data['eeg_29'][0], source.data['eeg_30'][0],
                       source.data['eeg_31'][0], source.data['eeg_32'][0], source.data['eeg_33'][0],
                       source.data['eeg_34'][0], source.data['eeg_35'][0], source.data['eeg_36'][0],
                       source.data['eeg_37'][0], source.data['eeg_38'][0], source.data['eeg_39'][0],
                       source.data['eeg_40'][0], source.data['eeg_41'][0], source.data['eeg_42'][0],
                       source.data['eeg_43'][0], source.data['eeg_44'][0], source.data['eeg_45'][0],
                       source.data['eeg_46'][0], source.data['eeg_47'][0], source.data['eeg_48'][0],
                       source.data['eeg_49'][0], source.data['eeg_50'][0], source.data['eeg_51'][0],
                       source.data['eeg_52'][0], source.data['eeg_53'][0], source.data['eeg_54'][0],
                       source.data['eeg_55'][0], source.data['eeg_56'][0], source.data['eeg_57'][0],
                       source.data['eeg_58'][0], source.data['eeg_59'][0], source.data['eeg_60'][0],
                       source.data['eeg_61'][0], source.data['eeg_62'][0], source.data['eeg_63'][0],
                       source.data['eeg_64'][0] ]

        if i < 64: # add eeg data to array
            self.eeg_data[i] = sample_data
        else: # start plotting 
            #store in temp so we can get the updated data and max for later use
            temp = self.getFreqBandOrValue(self.eeg_data, sample_data, -1, self.global_max) 

            delta_band = temp[0]   
            theta_band = self.getFreqBandOrValue(self.eeg_data, sample_data, -2, self.global_max)[0]
            alpha_band = self.getFreqBandOrValue(self.eeg_data, sample_data, -3, self.global_max)[0]
            
            # get total band
            total_band = np.add(delta_band, theta_band)
            total_band = np.add(total_band, alpha_band)
            
            self.evoked.data = np.transpose([delta_band]) # set evoked's data to delta band
            # plot delta band topo map and store result which is a matplotlib figure
            figure_delta = self.evoked.plot_topomap(times=[0], ch_type='eeg', time_format ='', extrapolate='head',
                                              cmap='jet', colorbar=False, size = 3, sensors='kX', show=False)
            
            delta_array = self.getImageArray(figure_delta) # get figure as image array to plot

            self.evoked.data = np.transpose([theta_band])  # set evoked's data to theta band
            # plot theta band topo map and store result which is a matplotlib figure
            figure_theta = self.evoked.plot_topomap(times=[0], ch_type='eeg', time_format='', extrapolate='head', 
                                              cmap='jet', colorbar=False, size=3, sensors='kX', show=False)
            
            theta_array = self.getImageArray(figure_theta) # get figure as image array to plot
            
            self.evoked.data = np.transpose([alpha_band]) # set evoked's data to alpha band
            # plot alpha band topo map and store result which is a matplotlib figure
            figure_alpha = self.evoked.plot_topomap(times=[0], ch_type='eeg', time_format='', extrapolate='head',
                                              cmap='jet', colorbar=False, size=3, sensors='kX', show=False)
            
            alpha_array = self.getImageArray(figure_alpha) # get figure as image array to plot
            
            self.evoked.data = np.transpose([total_band]) # set evoked's data to total band
            # plot alpha band topo map and store result which is a matplotlib figure
            figure_total = self.evoked.plot_topomap(times=[0], ch_type='eeg', time_format='', extrapolate='head',
                                              cmap='jet', colorbar=False, size=3, sensors='kX', show=False)
            
            total_array = self.getImageArray(figure_total) # get figure as image array to plot
            
            # update column data source with updated image arrays for plots on document
            self.source_images.data['delta_array'] = [np.flipud(delta_array)]
            self.source_images.data['theta_array'] = [np.flipud(theta_array)]
            self.source_images.data['alpha_array'] = [np.flipud(alpha_array)]
            self.source_images.data['total_array'] = [np.flipud(total_array)]
            
            # close matplotlib figure
            plt.close(figure_delta)
            # close matplotlib figure
            plt.close(figure_theta)
            # close matplotlib figure)
            plt.close(figure_alpha)
            # close matplotlib figure
            plt.close(figure_total)
            
            self.eeg_data = np.transpose(temp[2]) # update eeg array to get new data

            m = temp[1] # get max to compare with global max

            if self.global_max < m: # check to see if global max needs to be updated
                self.global_max = m
                
