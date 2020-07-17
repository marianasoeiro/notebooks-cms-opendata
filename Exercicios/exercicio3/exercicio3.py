# Import the needed modules. Pandas is for the data-analysis, numpy for scientific calculation
# and matplotlib.pyplot for making plots. Modules are named as pd, np and plt.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#%matplotlib inline

# Create a new DataFrame structure from the file "Jpsimumu_Run2011A.csv"
dataset = pd.read_csv('Jpsimumu_Run2011A.csv')

# Create a Series structure (basically a list) and name it to "inv_mass".
# Save the column "M" from the "dataset" to the variable "inv_mass".
inv_mass = dataset['M']

plt.hist(inv_mass, bins=500)
plt.show()

peakdata = dataset[(inv_mass>3.0) & (inv_mass<3.2)]
peak_invmass = peakdata['M']
plt.hist(peak_invmass, bins=200)
plt.show()
peakdata = dataset[(inv_mass>3.0) & (inv_mass<3.2)]
peak_invmass = peakdata['M']
plt.hist(peak_invmass, bins=200)
plt.show()

mean_masses = np.mean(inv_mass)
print(mean_masses)

mean_peakmasses = np.mean(peak_invmass)
print(mean_peakmasses)

variance = np.var(inv_mass)
print(variance)

peak_variance = np.var(peak_invmass)
print(peak_variance)

sd = np.sqrt(variance)
print(sd)

sd_peak = np.sqrt(peak_variance)
print(sd_peak)
