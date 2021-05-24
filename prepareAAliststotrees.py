__author__ = "Flora"
__version__ = "2020.10.28"

"""
This module reads PDB output lists and creates double lists of AA coordinates and 
properties per AA atom, ready to be converted to trees.
eg. [['75.814,-34.543,47.16', '74.639,-34.529,48.079'...],[...]]
    Inputs:
        AA: Amino Acid id number (int list)
        AA_name: Amino Acid name (string list)
        xyz: coordinates in 3Dspace per atom (3d point rhino item)
        atoms: atom names (string list)
    Output:
        a: xyz coordinates for debug
        start: list of coordinates of all atoms per AA (for starting points 
        of lines)
        end: list of coordinates of all atoms per AA (for ending poins of lines)
"""


import rhinoscriptsyntax as rs

counter=-1

amino_list=[]

atom_xyz_list=[]
atoms_xyz_list=[]
atom_name_list=[]
atoms_name_list=[]

temp = []


#TODO: seperate per protein ("TER") 

# store list of atoms per aminoacid
for i in range (len(xyz)):
    if AA[i]!=counter: #a new aminoacid
        if atom_xyz_list != []:
            atoms_xyz_list.append(atom_xyz_list) #store list of atoms per AA
            atoms_name_list.append(atom_name_list)
        counter=AA[i]
        atom_xyz_list=[]
        atom_name_list=[]
        atom_xyz_list.append(xyz[i])
        atom_name_list.append(atoms[i])

        amino_list.append(AA_name[i]) #stores name per chain of AA
    else: # existing aminoacid
        atom_xyz_list.append(xyz[i])
        atom_name_list.append(atoms[i])

atoms_xyz_list.append(atom_xyz_list) #store list of atoms of final AA
atoms_name_list.append(atom_name_list)#store list of atoms names of final AA


if (mask!= None) :

    atoms_xyz_list = atoms_xyz_list[int(mask[0]):int(mask[1])]
    #print (atoms_xyz_list)
    atoms_name_list=atoms_name_list[int(mask[0]):int(mask[1])]
    amino_list=amino_list [int(mask[0]):int(mask[1])]

else: 
    None