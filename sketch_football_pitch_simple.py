# Copyright   : Twitter: @TacticsBadger, TacticsNotAntics: https://tacticsnotantics.org
# Version 1.0 : July 17, 2022
# Last Updated: January 16, 2023
'''
Brief: Create a football pitch with zones established through Wyscout
'''
from matplotlib.patches import Arc
from matplotlib import transforms
from PIL import Image
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Create figure
fig=plt.figure()
fig.set_size_inches(14,10)
ax=fig.add_subplot(1,1,1)

#Pitch Outline & Centre Line
plt.plot([0,0],[0,90], color="darkgrey")
plt.plot([0,108],[90,90], color="darkgrey")
plt.plot([108,108],[90,0], color="darkgrey")
plt.plot([108,0],[0,0], color="darkgrey")
plt.plot([54,54],[0,90], color="darkgrey")

#Left Penalty Area
plt.plot([18,18],[65,25],color="darkgrey")
plt.plot([0,18],[65,65],color="darkgrey")
plt.plot([18,0],[25,25],color="darkgrey")

#Right Penalty Area
plt.plot([108,90],[65,65],color="darkgrey")
plt.plot([90,90],[65,25],color="darkgrey")
plt.plot([90,108],[25,25],color="darkgrey")

#Left 6-yard Box
plt.plot([0,6],[54,54],color="darkgrey")
plt.plot([6,6],[54,36],color="darkgrey")
plt.plot([6,0],[36,36],color="darkgrey")

#Right 6-yard Box
plt.plot([108,102],[54,54],color="darkgrey")
plt.plot([102,102],[54,36],color="darkgrey")
plt.plot([102,108],[36,36],color="darkgrey")

#Prepare Circles
centreCircle = plt.Circle((54,45),9.15,color="darkgrey",fill=False)
centreSpot = plt.Circle((54,45),0.8,color="darkgrey")
leftPenSpot = plt.Circle((11,45),0.8,color="darkgrey")
rightPenSpot = plt.Circle((97,45),0.8,color="darkgrey")

#Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

#Prepare Arcs
leftArc = Arc((12,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="darkgrey")
rightArc = Arc((96,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="darkgrey")

#Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)

# add arrow showing the direction of play
plt.arrow(x=0, y=95, dx=15, dy=0, width=1)

plt.annotate('Direction of Play', xy = (0, 92), weight="bold")
plt.annotate('Pitch Dimensions: 108m x 65m', xy = (40, 92), weight="bold")
plt.annotate('Zone assignment based on Wyscout', xy = (77, 92), weight="bold")

output_file = "pitch-with-assigned-zones-transparent.png"  

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

#Zones - using Wyscout zonal delimitation

#vertical zones
plt.plot([0,0],[0,90], color="tab:blue", linestyle='dashed')
plt.plot([32,32],[0,90], color="tab:blue", linestyle='dashed')
plt.plot([83,83],[0,90], color="tab:blue", linestyle='dashed')
plt.plot([76,76],[25,65], color="tab:blue", linestyle='dashed')
plt.plot([108,108],[0,90], color="tab:blue", linestyle='dashed')

#horizontal zones
plt.plot([0,108],[0,0], color="tab:blue", linestyle='dashed')
plt.plot([0,108],[25,25], color="tab:blue", linestyle='dashed')
plt.plot([0,108],[65,65], color="tab:blue", linestyle='dashed')
plt.plot([0,108],[90,90], color="tab:blue", linestyle='dashed')

#add Zone labels
ax.text(0.05, 0.885, "Zone 3", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)    
ax.text(0.0475, 0.55, "Zone 1", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.2675, 0.6525, "Zone 2", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.05, 0.2750, "Zone 4", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.4775, 0.6525, "Zone 5", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.6925, 0.885, "Zone 6", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.6925, 0.2750, "Zone 7", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.6925, 0.6525, "Zone 8", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.905, 0.885, "Zone 9", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.8975, 0.2750, "Zone 10", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
ax.text(0.8975, 0.6525, "Zone 11", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

#Tidy Axes
plt.axis('off')

#Display Pitch
plt.savefig(output_file, format='png', dpi=1200, bbox_inches='tight')
