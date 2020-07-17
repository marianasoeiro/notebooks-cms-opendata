# Import the needed modules. Pandas is for the data-analysis, numpy for scientific calculation
# and matplotlib.pyplot for making plots. Modules are named as pd, np and plt.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a new DataFrame structure from the file "Zmumu_Run2011A_masses.csv"
dataset = pd.read_csv('Zmumu_Run2011A_masses.csv')

# Set the conditions to large and small etas. These can be changed, but it has to be taken
# care that about the same amount of events are selected in both groups.
cond1 = 1.52
cond2 = 0.45

# Create two DataFrames. Select to "large_etas" events where the pseudorapidities
# of the both muons are larger than "cond1". Select to "small_etas" events where
# the pseudorapidities of the both muons are smaller than "cond2".
large_etas = dataset[(np.absolute(dataset.eta1) > cond1) & (np.absolute(dataset.eta2) > cond1)]
small_etas = dataset[(np.absolute(dataset.eta1) < cond2) & (np.absolute(dataset.eta2) < cond2)]

# Print two empty lines for better design.
print('\n' * 2)

print('The amount of all events = %d' % len(dataset))
print('The amount of events where the pseudorapidity of both muons has been large = %d' %len(large_etas))
print('The amount of events where the pseudorapidity of both muons has been small = %d' %len(small_etas))

# Save the invariant masses to variable "inv_mass1".
inv_mass1 = large_etas['M']

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#% matplotlib inline

# Create the histogram from data in variable "inv_mass1". Set bins and range.
plt.hist(inv_mass1, bins=120, range=(60,120))

# Set y-axis range from 0 to 60.
axes = plt.gca()
axes.set_ylim([0,60])

# Name the axises and give a title.
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events per bin')
plt.title('Histogram of invariant masses for the events where the\n pseudorapidity of both of the muons has been large\n')
plt.show()

# Save the invariant masses to variable "inv_mass2".
inv_mass2 = small_etas['M']

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#% matplotlib inline

# Create the histogram from data in variable "inv_mass1". Set bins and range.
plt.hist(inv_mass2, bins=120, range=(60,120))

# Set y-axis range from 0 to 60.
axes = plt.gca()
axes.set_ylim([0,60])

# Name the axises and give a title.
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events per bin')
plt.title('Histogram of invariant masses for the events where the\n pseudorapidity of both of the muons has been small\n')
plt.show()
