
#read OpenFoam data by python

sampleDir=u"postProcessing/sample/"
fileName1="U_vel1_U.xy"
fileName2="U_vel2_U.xy"
fileName3="U_vel3_U.xy"
NVariable=1



import os
import numpy as np
import matplotlib.pyplot as plt



def foamPlot(timeName):
    if (timeName!="0"):
    #if (timeName=="0.6"):
        destination1 = sampleDir +"/" + timeName + "/" +fileName1
        destination2 = sampleDir +"/" + timeName + "/" +fileName2
        destination3 = sampleDir +"/" + timeName + "/" +fileName3
        
        
        print(destination1)
        print(destination2)
        print(destination3)
        
        fileContent1=np.loadtxt(destination1)
        fileContent2=np.loadtxt(destination2)
        fileContent3=np.loadtxt(destination3)
        plt.figure(dpi=300)
        plt.title("Laminar incompressible flow over a canyon - icoFoam")
        
        plt.plot(fileContent1[:,1],fileContent1[:,0],label= "center of canyon")
        plt.plot(fileContent2[:,1],fileContent2[:,0],label= "before canyon")
        plt.plot(fileContent3[:,1],fileContent3[:,0],label= "after canyon")
    
    
    
for dirStr in os.listdir(sampleDir):
    foamPlot(dirStr)


plt.legend(loc="lower right")
plt.xlabel("Longitude component velocity : u(m/s)")
plt.ylabel("Height (m)")
plt.savefig("flow_over_canyon")

plt.show()