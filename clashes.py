"""Module to calculate Energy and find Clashes of AA in pdb files in Proteins .
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


def SplitCoordinates(xyz_str):
    """
    Function to split coord. str in float list
    xyz_str: (str) a list input of "x,y,z" coordinates
    """
    xyz = []
    for i in range (len(xyz_str)):
        x_,y_,z_ = xyz_str[i].split(",")
        xyz.append([float(x_),float(y_),float(z_)])
    return(xyz)

def CalcDistance(p1, p2):
    """
    Function to calculate distance in space between two points (p)
    p1, p2: (f) lists of coordinates for point1 and point2
    """
    dist = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p2[2])**2)
    return(dist)

def LennardJones (e, s, p1, p2):
    """
    Archetype model for simple yet realistic intermolecular interactions
    e: dispersion energy
    s: distance at which the particle-particle potential energy V is zero 
    (size of the particle) TODO: add list of molecules //usual s = 0.34nm
    p1,p2: centroid coordinates of two molecules
    
    V: potential energy
    """
    r = CalcDistance(p1,p2)
    V = 4*e*((s/r)**12 - (s/r)**6)
    return V


def CheckClash(xyz_str, xyz, thold, e):
    """
    Fuction to check for clashes by calculating minimum distance between each AA
    xyz_str: (str) list of xyz coordinates for gh output
    xyz: (f) a list of xyz coordinates
    
    thold: (f) minimum distance threshold for a clash between two AA
    
    id, c: list of unique index and coordinates of clashed AA
    """
    c, id = [], []
    error = 0
    for i in range (len(xyz)):
        for j in range (i+1, len(xyz)):
            V = LennardJones (e,thold,xyz[i],xyz[j]) #TODO: replace thold with s
            if (V > thold):
                c.append(xyz_str[i])
                id.append(str(i))
                error=1
    if (error == 1):
        ErrorGh("Clash: ", id[0])
    return(set(c), set(id))


def CheckBreak(xyz_str, xyz, thold):
    """
    Function to check for bond breaks by calculating max distance between each AA
    xyz_str: (str) list of xyz coordinates for gh output
    xyz: (f) list of xyz coordinates of AA
    thold: (f) maximum distance threshold for a break between two AA
    
    id, b: list of unique index and coordinates of break bond in AA
    """
    b, id = [], []
    error = 0
    for i in range (len(xyz)):
        if (i+1 < len(xyz)):
            dist = CalcDistance(xyz[i],xyz[i+1])
            if (dist > thold):
                b.append(xyz_str[i])
                id.append(str(i))
                error=1
    if (error == 1):
        ErrorGh("Break: ", id[0])
    return (set(b), set(id))

def ErrorGh(m, d) :
    """
    Produces Grasshopper(gh) error and breaks the module
    """
    e = gh.GH_RuntimeMessageLevel.Error
    ghenv.Component.AddRuntimeMessage(e, m + str(d))

if __name__ == "__main__": 
    xyz = SplitCoordinates(CA_xyz)
    clash, cls_id = CheckClash(CA_xyz, xyz, clash_th, e)
    breakbond, brk_id = CheckBreak(CA_xyz, xyz, break_th)