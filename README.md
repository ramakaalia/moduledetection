# moduledetection

louavin.py:
Community detection using Louvain. This program calculates the modules and their node membership in an undirected network using Louvain algorithm at best modularity value out of different levels for weighted networks.

phy_ppi_sample: sample file containing ppi binary interactions to be used as input for louvain.py


How to Run:
1) Activate the virtual environment:
cd to the dir
$source ./modEnv/bin/activate

2) Run code as:
usage: louvain.py [-h] [-i INPUTFILE]

Example:
python louvain.py -i phy_ppi_sample 

('Number of communities', 25.0)

('modularity:', 0.7637618748084707)

runtime: 0.0175979137421
