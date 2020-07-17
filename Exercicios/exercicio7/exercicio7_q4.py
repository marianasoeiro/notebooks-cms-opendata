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

# Let's limit the fit near to the peak of the histogram.
lowerlimit = 70
upperlimit = 110
bins = 100

# Let's select the invariant mass values that are inside the limitations.
limitedmasses = inv_mass1[(inv_mass1 > lowerlimit) & (inv_mass1 < upperlimit)]

#Let's create a histogram of the selected values.
histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
y = histogram[0]
x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )

# Let's define a function that describes Breit-Wigner distribution for the fit.
# E is the energy, gamma is the decay width, M the maximum of the distribution
# and a, b and A different parameters that are used for noticing the effect of
# the background events for the fit.
def breitwigner(E, gamma, M, a, b, A):
    return a*E+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)

# Initial values for the optimization in the following order:
# gamma (the full width at half maximum (FWHM) of the distribution)
# M (the maximum of the distribution)
# a (the slope that is used for noticing the effect of the background)
# b (the y intercept that is used for noticing the effect of the background)
# A (the "height" of the Breit-Wigner distribution)
initials = [gamma, inv_mass1, -2, 200, 13000]

# Let's import the module that is used in the optimization, run the optimization
# and calculate the uncertainties of the optimized parameters.
from scipy.optimize import curve_fit
best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
error = np.sqrt(np.diag(covariance))
    
# Let's print the values and uncertainties that are got from the optimization.
print("The values and the uncertainties from the optimization")
print("")
first = "The value of the decay width (gamma) = {} +- {}".format(best[0], error[0])
second = "The value of the maximum of the distribution (M) = {} +- {}".format(best[1], error[1])
third = "a = {} +- {}".format(best[2], error[2])
fourth = "b = {} +- {}".format(best[3], error[3])
fifth = "A = {} +- {}".format(best[4], error[4])
print(first)
print(second)
print(third)
print(fourth)
print(fifth)

plt.plot(x, breitwigner(x, *best), 'r-', label='gamma = {}, M = {}'.format(best[0], best[1]))
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of event')
plt.title('The Breit-Wigner fit')
plt.legend()
plt.show()
