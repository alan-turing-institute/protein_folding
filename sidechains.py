"""Script that create the sidechains of the AA from PDB files
    Inputs:
        AA: Amino Acid names
        AA_name: The y script variable
        xyz:
        atoms:
    Output:
        a: The a output variable
        start:
        end:
            """

__author__ = "Flora"
__version__ = "2020.10.28"

import rhinoscriptsyntax as rs

counter=-1

amino_list=[]

atom_xyz_list=[]
atom_name_list=[]
atoms_name_list=[]
atoms_xyz_list=[]


sidechains_dict = {
"GLN":{"A": ["C","C","CA","CA","CB","CG","CD","CD"],
    "B":["O","CA","N","CB","CG","CD","NE2","OE1"]},
"GLU":{"A": ["C","C","CA","CA","CB","CG","CD","CD"],
    "B":["O","CA","N","CB","CG","CD","OE2","OE1"]},
"LYS":{"A": ["C","C","CA","CA","CB","CG","CD","CE"],
    "B": ["O","CA","N","CB","CG","CD","CE","NZ"]},
"ARG":{"A":["C","C","CA","CA","CB","CG","CD","NE","CZ","CZ"],
    "B": ["O","CA","N","CB","CG","CD","NE","CZ","NH1","NH2"]},
"ILE":{"A": ["C","C","CA","CA","CB","CB","CG1"],
    "B": ["O","CA","N","CB","CG1","CG2","CD1"]},
"SER":{"A": ["C","C","CA","CA","CB"],
    "B": ["O","CA","N","CB","OG"]},
"VAL":{"A": ["C","C","CA","CA","CB","CB"],
    "B": ["O","CA","N","CB","CG2","CG1"]},
"HIS": {"A": ["C","C","CA","CA","CB","CG","CG","CD2","CE1","ND1"], 
    "B": ["O","CA","N","CB","CG","ND1","CD2","NE2","NE2","CE1"]},
"GLY":{"A":["C","C","CA"],
    "B": ["O","CA","N"]},
"LEU":{"A": ["C","C","CA","CA","CB","CG","CG"],
    "B": ["O","CA","N","CB","CG","CD1","CD2"]},
"ALA":{"A": ["C","C","CA","CA"],
    "B": ["O","CA","N","CB"]},
"ASN":{"A": ["C","C","CA","CA","CB","CG","CG"],
    "B": ["O","CA","N","CB","CG","OD1","ND2"]},
"THR":{"A": ["C","C","CA","CA","CB","CB"],
    "B": ["O","CA","N","CB","CG2","OG1"]},
"PRO":{"A": ["C","C","CA","CA","CB","CG","CD"],
    "B": ["O","CA","N","CB","CG","CD","N"]},
"ASP":{"A":["C","C","CA","CA","CB","CG","CG"],
    "B": ["O","CA","N","CB","CG","OD1","OD2"]},
"TYR":{"A": ["C","C","CA","CA","CB","CG","CG","CD1","CD2","CE1","CE2","CZ"],
    "B": ["O","CA","N","CB","CG","CD1","CD2","CE1","CE2","CZ","CZ","OH"]},
"PHE":{"A": ["C","C","CA","CA","CB","CG","CG","CD1","CD2","CE1","CE2"],
    "B": ["O","CA","N","CB","CG","CD1","CD2","CE1","CE2","CZ","CZ"]},
"TRP":{"A": ["C","C","CA","CA","CB","CG","CG","CD1","CD2","NE1","CD2","CE2","CE3","CZ3","CH2"], 
    "B": ["O","CA","N","CB","CG","CD2","CD1","NE1","CE2","CE2","CE3","CZ2","CZ3","CH2","CZ2"]},
}


# store list of atoms per aminoacid
for i in range (len(AA)):
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



def sidechain1(atoms_xyz_list,atoms_name_list):
    start=[]
    end=[]
    """
    A = sidechains_dict.get(amino_list[i],{}).get('A') #get the list of the first points of the AA
    B = sidechains_dict.get(amino_list[i],{}).get('B')
        for x in range (len(A)):
            for y in range(len(atoms_name_list[i])):
                if (A[x]==atoms_name_list[i][y]):
                    start.append(atoms_xyz_list[i][y])
                if (B[x]==atoms_name_list[i][y]):
                    end.append(atoms_xyz_list[i][y])
                    """

amino_start =[]
amino_end=[]

def sidechain(amino_acid,A,B,atom_list,xyz_list):
    start, end=[],[]
    for x in range (len(A)):
        for y in range(len(atom_list)):
            if (A[x]==atom_list[y]):
                start.append(xyz_list[y])
            if (B[x]==atom_list[y]):
                end.append(xyz_list[y])
    return (start,end)

def construct_sidechains(amino_list,atoms_name_list,atoms_xyz_list):

    for i in range (len(amino_list)):
        amino_acid = sidechains_dict.get(amino_list[i])
        if(amino_acid != None): #if the amino acid exists in the pdb exists in the current dictionary
            A = amino_acid.get('A') #get the list of the first points of the AA
            B = amino_acid.get('B') #get the list of the second points of the AA
            atom_list = atoms_name_list[i]
            xyz_list = atoms_xyz_list[i]

            start, end= sidechain(amino_acid,A,B,atom_list,xyz_list)

            amino_start.append(start)
            amino_end.append(end)
        else: error = "Amino Acid doesnt exist"



#Created By piac
#from https://gist.github.com/piac/ef91ac83cb5ee92a1294
def list_to_tree(input, none_and_holes=True, source=[0]):
    """Transforms nestings of lists or tuples to a Grasshopper DataTree"""
    from Grasshopper import DataTree as Tree
    from Grasshopper.Kernel.Data import GH_Path as Path
    from System import Array
    def proc(input,tree,track):
        path = Path(Array[int](track))
        if len(input) == 0 and none_and_holes: tree.EnsurePath(path); return
        for i,item in enumerate(input):
            if hasattr(item, '__iter__'): #if list or tuple
                track.append(i); proc(item,tree,track); track.pop()
            else:
                if none_and_holes: tree.Insert(item,path,i)
                elif item is not None: tree.Add(item,path)
    if input is not None: t=Tree[object]();proc(input,t,source[:]);return t

#print (atoms_xyz_list)
#sidechain(atoms_xyz_list, amino_names, atoms_name_list)
construct_sidechains(amino_list,atoms_name_list,atoms_xyz_list)
a= list_to_tree(atoms_xyz_list)
start= list_to_tree(amino_start)
end=list_to_tree(amino_end)

#a= atoms_xyz_list
#print (atoms_xyz_list)
