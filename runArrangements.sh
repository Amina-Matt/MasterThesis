#!/bin/bash

###################################################################
# author: Amina Matt
# date: June 2020
# Call the python script to create random arrangements on Blender
## Inputs
# txt file from MMA with the arrangements lists
# python file that do the positioning and the merge
## Output
# .stl file with the multiple indidivudal shapes merged into one structure with random arrangement
####################################################################

#Read line of arguments from .txt (created in MMA)
i=0
echo "got file"
while read fileLine; do 
#Run the python script in blender
echo "in loop"
Blender tmp.blend --background --python random.py -- -s1 $fileLine
i=$((i+1))
echo $i
mv Random_length.stl Random_length_$i.stl
done < 'arrangementsList.txt' 
