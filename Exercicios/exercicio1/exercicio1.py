# Import the needed modules. Pandas is for the data-analysis and numpy for scientific calculation.
# Name these to "pd" and "np".
import pandas as pd
import numpy as np

# Create a new DataFrame structure from the file "Zmumu_Run2011A.csv". Name it as "dataset".
dataset = pd.read_csv('/Users/soeiros/Documents/MESTRADO/Mestrado-2020/notebooks-cms-opendata/data/Zmumu_Run2011A.csv')
dataset.head()
invariant_mass = np.sqrt(2*dataset.pt1*dataset.pt2*(np.cosh(dataset.eta1-dataset.eta2) - np.cos(dataset.phi1-dataset.phi2)))
print(invariant_mass)
