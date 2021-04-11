"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "Flora"
__version__ = "2021.01.18"

import rhinoscriptsyntax as rs

output=[]

for i in range(selection.BranchCount):
    subOutput=[]
    for ii in selection.Branch(i):
        number=int(ii)
        print(number)
        if number<len(Lists):
            subOutput.append(Lists[number])
    output.append(subOutput)

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


#output=list_to_tree(output)