import pandas
import matplotlib.pyplot as plt
#%matplotlib inline

dataset = pandas.read_csv('Dimuon_DoubleMu.csv')
dataset.head()

invariant_mass = dataset['M']
plt.hist(invariant_mass, bins=50, range=(0,200))
plt.show()

plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('The histogram of the invariant masses of two muons \n')

plt.hist(invariant_mass, bins=50, range=(0,200))
plt.show()

newsethighE = dataset[dataset.E1+dataset.E2>250]
newsetlowE = dataset[dataset.E1+dataset.E2<250]

plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('The invariant masses of two muons comparing high and low energy\n')
plt.hist(newsetlowE ['M'], bins=50, range=(80,100),alpha=0.5, label='Low E')
plt.hist(newsethighE ['M'], bins=50, range=(80,100),alpha=0.5, label='High E')
plt.legend (loc='upper right')
plt.show()
