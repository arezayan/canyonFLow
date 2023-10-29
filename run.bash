

#------------------------------------------------------------------------------


foamCleanTutorials


echo -en " First part: BlockMesh "
blockMesh #creating geometry with blockMesh

echo -e "\n  second part: checkMesh (saved in Log) \n "
checkMesh >log  #creating geometry with blockMesh

echo -e "\n  solution started: wait ....\n "


echo -en "
----------------------------------------------
 Contributor: Amirreza Rezayan
 Updated on:  27 October 2023               
----------------------------------------------
 Topic:       flow in channel                    
 OpenFOAM:    version 9 (Foundation) 
       
 Email:       arezayan87@gmail.com     
----------------------------------------------"


icoFoam > log

pyFoamPlotWatcher.py log

postProcess -func sample -latestTime

python3 dataExtract_2DLaminar.py