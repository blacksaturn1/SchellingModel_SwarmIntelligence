# SchellingModel_SwarmIntelligence
# Installation
pip install pygame

# Run the Simulation
## To run the program with p=.6 and t=3:
python main.py -populationDensity .6 -happinessCount {\"1\":3}
## p=.6 and t=4:
python main.py -populationDensity .6 -happinessCount {\"1\":4}
## For P=.6 and t=3 80% of the time and t=5 20% of the time:
python main.py -happinessCount \{\".8\":3,\".2\":5\} -populationDensity .6
## To run with .8 density:
python main.py -populationDensity .8 -happinessCount {\"1\":3}
python main.py -populationDensity .8 -happinessCount {\"1\":4}
python main.py -happinessCount \{\".8\":3,\".2\":5\} -populationDensity .8
