"""Module to calculate Energy Clashes of AA in pdb files in Proteins .
    Inputs:
        CA_xyz: list (str) of xyz cooridnates of CA
        clash_th: (float) clash threshhold
        break_th: (float) break threshold
        TODO: AA_name: list(str) of AA

    Output:
        clash: a list of AA coord of clashes
        breakbond: a list of AA coord of breaks"""

__author__ = "Flora"
__version__ = "2021.04.28"

import rhinoscriptsyntax as rs
import math 
import Grasshopper.Kernel as gh


x,y,z = [],[],[]
clash, breakbond = [],[]
#clash_th = 3.75
#break_th = 2.7

def SplitCoordinates(xyz):
    for i in range (len(xyz)):
        x1,y1,z1 = xyz[i].split(",")
        x.append(float(x1))
        y.append(float(y1))
        z.append(float(z1))

def CheckClash(xyz,x,y,z):
    for i in range (len(CA_xyz)):
        for j in range (len(CA_xyz)):
            if (i != j):
                dist = math.sqrt((x[j]-x[i])**2 + (y[j]-y[i])**2 + (z[j]-z[i])**2)
                if (dist < clash_th):
                    clash.append(CA_xyz[i])
                    Error1("Clash: ", CA_xyz[i])

def CheckBreak(xyz,x,y,z):
    for i in range (len(xyz)):
        if (i+1 < len(xyz)):
            dist = math.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2 + (z[i+1]-z[i])**2)
            if (dist < break_th):
                breakbond.append(CA_xyz[i])
                Error1("Break: ", CA_xyz[i])

def Error1(m, d) :
    e= gh.GH_RuntimeMessageLevel.Error
    ghenv.Component.AddRuntimeMessage(e, m + str(d))


if __name__ == "__main__": 
    SplitCoordinates(CA_xyz)
    CheckClash(CA_xyz,x,y,z)
    CheckBreak(CA_xyz,x,y,z)





