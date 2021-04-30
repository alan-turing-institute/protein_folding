__author__ = "Flora"
__version__ = "2020.10.28"

"""
This componment gets the x,y,z list and creates seperate x,y,z, lists per AA 
atom.
    Inputs:
        AA: Amino Acid id number (int list)
        AA_name: Amino Acid name (string list)
        xyz: coordinates in 3Dspace per atom (3d point rhino item)
        atoms: atom names (string list)
    Output:
        a: xyz coordinates for debug
        start: list of coordinates of all atoms per AA (for starting points of lines) 
        end: list of coordinates of all atoms per AA (for ending poins of lines)
"""


import rhinoscriptsyntax as rs


x_list,y_list,z_list=[],[],[]

def create_xyz_list():

    for i in range (len(xyz)):
        x1,y1,z1=[],[],[]
        for j in range (len(xyz[i])):
            if (xyz[i][j]!=None):
                xyz_str= str(xyz[i][j])
                x,y,z= xyz_str.split(",")
                x1.append(x)
                y1.append(y)
                z1.append(z)
            else:
                x1.append("Ter")
                y1.append("Ter")
                z1.append("Ter")
        x_list.append(x1)
        y_list.append(y1)
        z_list.append(z1)


create_xyz_list()


