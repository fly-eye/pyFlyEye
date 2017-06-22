
# coding: utf-8

# #### This notebook measures the error of an .swc output and a marker file with manually labeled corners.



import matplotlib.pyplot as plt




# In[2]:

import pandas as pd


# In[48]:

GTMarkerFile = "~/projects/cornea project/DATA_example_Holco_praire_Scan29/marker files/Holco_Scan29_Landmark.marker"


# In[49]:

import os
#GTMarkerFile = os.path.join(os.getcwd()+".."+"cornea project"+"DATA_example_Holco_praire_Scan29"+"marker files"+"Holco_Scan29_Landmark.csv")


# In[51]:

SWCFile = "~/projects/cornea project/DATA_example_Holco_praire_Scan29/processed/C3-Holco_Scan29_scaled_0.3.tif_SIGEN.swc"



### read .swc file
SWCMarkers = pd.read_csv(SWCFile, skiprows = 3,sep = " ",header = None)
SWCMarkers.columns = ["n","type","x","y","z","radius","parent"]

### read .marker file with corners
GTMarkers = pd.read_csv(GTMarkerFile)
GTMarkers = GTMarkers.rename(columns = {'##x':'x'})

def calculate_error(SWCMarkers,GTMarkers):

    # get roots
    roots = SWCMarkers[SWCMarkers.parent==-1]


    # remove roots with big radius
    small_roots = roots[roots.radius<2]

    # seems none of the roots has a big radius???












## for each create ROI based on marker file


    from sklearn.metrics.pairwise import pairwise_distances as pdist




    GTMarkers[['x',"y","z"]]
    roots[["x","y","z"]]



    ## for the branching points in .swc create a distance matrix
    #from scipy.spatial.distance import pdist
    res = pdist(GTMarkers[["x","y","z"]],roots[["x","y","z"]])

    ## calculate error
    error = sum(res.min(axis = 1))

    return(error)



    # Need to come up with a way to deal with missing points?


if __name__=="__main__":

    import sys
    #WCFile = sys.argv[1]
    # MarkerFile = sys.argv[2]

    SWCMarkers = pd.read_csv(SWCFile, skiprows = 3,sep = " ",header = None)
    SWCMarkers.columns = ["n","type","x","y","z","radius","parent"]

    ### read .marker file with corners
    GTMarkers = pd.read_csv(GTMarkerFile)
    GTMarkers = GTMarkers.rename(columns = {'##x':'x'})

    error = calculate_error(SWCMarkers,GTMarkers)
    print(error)





# create a file
