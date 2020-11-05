"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "Flora"
__version__ = "2020.10.28"

import rhinoscriptsyntax as rs

counter=-1
aminoxea=[]
aminoxi=[]
atomo=[]
amino_name=[]
atoma=[]


"""
        if amino_name[i] == "HIS":
            start=[]
            end=[]
            ##TODO: PROVLIMA>>> DEN KLEINEI I LOUPA... 
            GLN_start = ["C","C","CA","CA","CB","CG","CG","CD2","CE1","ND1"]
            GLN_end =   ["O","CA","N","CB","CG","ND1","CD2","NE2","NE2", "CE1"]
            #list of points in space for the starting points of lines of the GLN topology
            for x in range (len(GLN_start)):
                for y in range(len(atoma[i])):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                    if (GLN_end[x]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)


"""

# store list of atoms per aminoacid
for i in range (len(AA)):
    if AA[i]!=counter: #a new aminoacid
        if aminoxi != []:
            aminoxea.append(aminoxi) #store list of atoms per AA
            atoma.append(atomo)
        counter=AA[i]
        aminoxi=[]
        atomo=[]
        aminoxi.append(xyz[i])
        atomo.append(atoms[i])

        amino_name.append(AA_name[i]) #stores name per chain of AA
    else: # existing aminoacid
        aminoxi.append(xyz[i])
        atomo.append(atoms[i])

aminoxea.append(aminoxi) #store list of atoms of final AA
atoma.append(atomo)#store list of atoms names of final AA


amino_start =[]
amino_end=[]

def sidechain(aminoxea, amino_name, atoma):
    start=[]
    end=[]

    for i in range (len(amino_name)):

        #GLN
        if amino_name[i] == "GLN":
            GLN_start = ["C","C","CA","CA","CB","CG","CD","CD"]
            GLN_end = ["O","CA","N","CB","CG","CD","NE2","OE1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]


        #GLU
        if amino_name[i] == "GLU":
            GLN_start = ["C","C","CA","CA","CB","CG","CD","CD"]
            GLN_end = ["O","CA","N","CB","CG","CD","OE2","OE1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]
        
        #LYS
        if amino_name[i] == "LYS":
            GLN_start = ["C","C","CA","CA","CB","CG","CD","CE"]
            GLN_end = ["O","CA","N","CB","CG","CD","CE","NZ"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]
        
                #LYS
        if amino_name[i] == "ARG":
            GLN_start = ["C","C","CA","CA","CB","CG","CD","NE","CZ","CZ"]
            GLN_end = ["O","CA","N","CB","CG","CD","NE","CZ","NH1","NH2"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]
            
        if amino_name[i] == "ILE":
            GLN_start = ["C","C","CA","CA","CB","CB","CG1"]
            GLN_end = ["O","CA","N","CB","CG1","CG2","CD1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "SER":
            GLN_start = ["C","C","CA","CA","CB"]
            GLN_end = ["O","CA","N","CB","OG"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]
            
        if amino_name[i] == "VAL":
            GLN_start = ["C","C","CA","CA","CB","CB"]
            GLN_end = ["O","CA","N","CB","CG2","CG1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "HIS":
            start=[]
            end=[]
            ##TODO: PROVLIMA>>> DEN KLEINEI I LOUPA... 
            GLN_start = ["C","C","CA","CA","CB","CG","CG","CD2","CE1","ND1"]
            GLN_end =   ["O","CA","N","CB","CG","ND1","CD2","NE2","NE2", "CE1"]
            #list of points in space for the starting points of lines of the GLN topology
            for x in range (len(GLN_start)):
                for y in range(len(atoma[i])):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                    if (GLN_end[x]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)



        if amino_name[i] == "GLY":
            GLN_start = ["C","C","CA"]
            GLN_end = ["O","CA","N"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]
            
            
        if amino_name[i] == "LEU":
            GLN_start = ["C","C","CA","CA","CB","CG","CG"]
            GLN_end = ["O","CA","N","CB","CG","CD1","CD2"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "ALA":
            GLN_start = ["C","C","CA","CA"]
            GLN_end = ["O","CA","N","CB"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "ASN":
            GLN_start = ["C","C","CA","CA","CB","CG","CG"]
            GLN_end = ["O","CA","N","CB","CG","OD1","ND2"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "THR":
            GLN_start = ["C","C","CA","CA","CB","CB"]
            GLN_end = ["O","CA","N","CB","CG2","OG1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "THR":
            GLN_start = ["C","C","CA","CA","CB","CB"]
            GLN_end = ["O","CA","N","CB","CG2","OG1"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "PRO":
            
            #--> TODO it doesnt close. 
            GLN_start = ["C","C","CA","CA","CB","CG","CD"]
            GLN_end = ["O","CA","N","CB","CG","CD","N"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]

        if amino_name[i] == "ASP":
            
            GLN_start = ["C","C","CA","CA","CB","CG","CG"]
            GLN_end = ["O","CA","N","CB","CG","OD1","OD2"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]



        if amino_name[i] == "TYR":
            
            ##TODO: PROVLIMA>>> DEN KLEINEI I LOUPA... 
            GLN_start = ["C","C","CA","CA","CB","CG","CG","CD1","CD2","CE1","CE2","CZ"]
            GLN_end =   ["O","CA","N","CB","CG","CD1","CD2","CE1","CE2","CZ","CZ","OH"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]


        if amino_name[i] == "PHE":
            
            ##TODO: PROVLIMA>>> EDO KLEINEI I LOUPA... 
            GLN_start = ["C","C","CA","CA","CB","CG","CG","CD1","CD2","CE1","CE2"]
            GLN_end =   ["O","CA","N","CB","CG","CD1","CD2","CE1","CE2","CZ","CZ"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]


        if amino_name[i] == "TRP":
            
            ##TODO: PROVLIMA>>> DEN KLEINEI I LOUPA... 
            GLN_start = ["C","C","CA","CA","CB","CG","CG","CD1","CD2","NE1","CD2","CE2","CE3","CZ3","CH2"]
            GLN_end =   ["O","CA","N","CB","CG","CD2","CD1","NE1","CE2","CE2","CE3","CZ2","CZ3","CH2","CZ2"]
            #list of points in space for the starting points of lines of the GLN topology
            for y in range(len(atoma[i])):
                for x in range (len(GLN_start)):
                    if (GLN_start[x]==atoma[i][y]):
                        start.append(aminoxea[i][y])
                for x1 in range (len(GLN_end)):
                    if (GLN_end[x1]==atoma[i][y]):
                        end.append(aminoxea[i][y])
            amino_start.append(start)
            amino_end.append(end)
            start=[]
            end=[]


            #start=[aminoxea[i][2],aminoxea[i][2],aminoxea[i][1],aminoxea[i][1],aminoxea[i][4],aminoxea[i][5],aminoxea[i][6],aminoxea[i][6]]
            #end=  [aminoxea[i][3],aminoxea[i][1],aminoxea[i][0],aminoxea[i][4],aminoxea[i][5],aminoxea[i][6],aminoxea[i][7],aminoxea[i][8]]
            #amino_start.append(start)
            #amino_end.append(end)
            #for j in range (len (atoma)):
                
            #start.append()
            #print (atoma[i])
            #print (aminoxea[i])
            #print (amino_name[i])
            #print (amino_start)
            #print(amino_end)
    #        .....


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

#print (aminoxea)
sidechain(aminoxea, amino_name, atoma)
a= list_to_tree(aminoxea)
start= list_to_tree(amino_start)
end=list_to_tree(amino_end)

#a= aminoxea
#print (aminoxea)