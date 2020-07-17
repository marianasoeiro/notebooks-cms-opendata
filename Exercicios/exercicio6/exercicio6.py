# Import the needed modules. Pandas is for the data-analysis, numpy for scientific calculation
# and matplotlib.pyplot for making plots. Modules are named as pd, np and plt.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#% matplotlib inline

# Create a new DataFrame structure from the file "DoubleMuRun2011A.csv"
dataset = pd.read_csv('DoubleMuRun2011A.csv')

# Create a Series structure (basically a list) and name it to "invariant_mass".
# Save the column "M" from the "dataset" to the variable "invariant_mass".
invariant_mass = dataset['M']

# Set the amount of bins to the histogram.
nr_bins = 500

# Get the better division operator for Python 2. If not imported, the division operator
# in Python 2 will give only integers.
#from __future__ import division

# Make the weights to the histogram.
weights = []
for a in invariant_mass:
    weights.append(nr_bins/np.log(10)/a)

# Take log10 from all of the values in "invariant_mass".
invariant_mass_log = np.log10(invariant_mass)

# Plot the histogram with the plt.hist()-function of the matplotlib.pyplot module.
# "bins" determines the nubmer of bins used, "range" determines the limits of the x-axis
# and "weights" determines the weights to the histogram.
plt.hist(invariant_mass_log, bins=nr_bins, range=(-0.5,2.5), weights=weights)

# Set y-axis to logarithmic.
plt.yscale('log')
plt.show()

plt.hist(invariant_mass_log, bins=nr_bins, range=(-0.5,2.5))

plt.yscale('log')
plt.show()
