# sunburstplots
sunburst code for insects


# To run (mac M3 version):

# Set up conda
conda create -n sunburst-fix python=3.10 pandas matplotlib -c conda-forge
conda activate sunburst-fix

# Install plotly and compatible kaleido              
pip install plotly==5.17.0 kaleido==0.2.1


# Run the code 2 levels:

`python sunburst.py`

Assumes inut is called "family_subfamily.tsv"

which looks like:

"""
Ichneumonidae	Tryphoninae
Diprionidae	Diprioninae
Diprionidae	Diprioninae
Diprionidae	Diprioninae
Diprionidae	Diprioninae
Diprionidae	Diprioninae
Tenthredinidae	Allantinae
Tenthredinidae	Blennocampinae
Tenthredinidae	Tenthredininae
Tenthredinidae	Tenthredininae
"""

# Run the code as 3 levels code:

`python sunburst.3levels.3.py super_family_subfamily.tsv`

#input data (tab sep):
super_family_subfamily.tsv:

"""
Apoidea Megachilidae    Megachilinae
Apoidea Megachilidae    Megachilinae
Apoidea Megachilidae    Megachilinae
Apoidea Megachilidae    Megachilinae
Ichneumonoidae  Ichneumonidae   Tryphoninae
Ichneumonoidea  Ichneumonidae   Campopleginae
Ichneumonoidea  Ichneumonidae   Cryptinae
Ichneumonoidea  Ichneumonidae   Cryptinae
Ichneumonoidea  Ichneumonidae   Cryptinae
Ichneumonoidea  Ichneumonidae   Cryptinae
Ichneumonoidea  Ichneumonidae   Cryptinae
Tenthredinoidea Tenthredinidae  Allantinae
Tenthredinoidea Tenthredinidae  Blennocampinae
Tenthredinoidea Tenthredinidae  Tenthredininae
Tenthredinoidea Tenthredinidae  Tenthredininae
"""


