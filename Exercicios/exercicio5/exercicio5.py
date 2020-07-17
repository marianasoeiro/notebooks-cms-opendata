# Import the needed modules. Pandas is for the data-analysis, numpy for scientific calculation
# and matplotlib.pyplot for making plots. Modules are named as pd, np and plt.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a new DataFrame structure from the file "Zmumu_Run2011A_masses.csv"
dataset = pd.read_csv('Zmumu_Run2011A_masses.csv')

# Create a Series structure (basically a list) and name it to "invariant_mass".
# Save the column "M" from the "dataset" to the variable "invariant_mass".
invariant_mass = dataset['M']

# Create an empty list "selected", where the selected amount of invariant masses will be saved.
selected = []

# Ask user to enter the number of events wanted. Save the number to variable "amount".
amount = int(input('Enter the amount of events wanted: '))

# Check if user have selected more events than there are available.
# If not select that amount of invariant masses from the variable "invariant_mass".
# Masses will be selected in order.
if amount > 10851:
    print('''You have tried to select more data than there are available in the file.
The histogram couldn't be drawn. The maximum amount of the data is 10851.''')
else:
    for f in range(amount):
        M = invariant_mass[f]
        selected.append(M)
    print('\n You selected {} invariant mass values from the whole data.'.format(amount))

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#%matplotlib inline

# Create the histogram from data in variable "selected". Set bins and range to histogram.
plt.hist(selected, bins=120, range=(60,120))

# Set y-axis from 0 to 800.
axes = plt.gca()
axes.set_ylim([0,800])

# Name the axises and give the title.
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('Histogram of invariant masses of two muons\n')

# Empty the variable "selected" for the next run.
selected = []

# Loop where a new histogram is plotted after 1000 events until 10000 events have reached.
for a in range(0,10851,1000):
    T = invariant_mass[0:a]
    #%matplotlib inline
    plt.hist(T, bins=120, range=(60,120))
    
    # Set y-axis from 0 to 800.
    axes = plt.gca()
    axes.set_ylim([0,800])
    
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('Histogram of invariant masses of two muons for {} events\n'.format(len(T)))
    plt.show()
