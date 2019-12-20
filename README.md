# ndn-simul

# How to use this repo?

## NDN Simulation

There are two files: simul.cpp and topology file under topologies.
Put simul.cpp inside scratch/ folder and topology file as defined in simul.cpp
Run simulation. The result will be saved in /tmp folder. Retrieve the result before running other simulations.

## Visualize the Data

olaher.py is a python script to visualize the following parameter: delay, packet drop, and rate(throughput). 
Uncomment necessary section to fit your need. It will display a graph, make sure you have Xserver (linux) installed.
To run the script:
``` 
python -V   #make sure you're using python 3
pip install -r requirements.txt
python olaher.py 
```

## Saving data

To save the graph simply click on save button on the generated graph. Point to desired location and done.
