#!/bin/bash
alias vaa3d_build='~/projects/Vaa3dbuild_new/v3d_external/bin/vaa3d64.app/Contents/MacOS/vaa3d64'


inputFilename="/Users/valentina/projects/cornea project/DATA_example_Holco_praire_Scan29/C3-Holco_Scan29_scaled_0.3.tif"
outputFilename=`echo "$inputFilename"|cut -d'.' -f1`
outputFilename="$outputFilename.swc"
echo "$outputFilename"
vaa3d_build -x  SIGEN -f trace -i "$inputFilename" -o "$outputFilename"
