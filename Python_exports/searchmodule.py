"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "Flora"
__version__ = "2020.10.27"

import rhinoscriptsyntax as rs

output=[]

for i in range(len(input)):
    if input[i] == search: #.find(search)!=-1:
        #print (input[i])
        output.append(i)