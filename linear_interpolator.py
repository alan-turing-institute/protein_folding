"""Simple Linear Interpolator.
    Inputs:
        x: The x script variable
        y: The y script variable
        z: The z script variable
    Output:
        xyz_list: new xyz coordinates"""

__author__ = "Flora"
__version__ = "2020.11.12"

import rhinoscriptsyntax as rs

x,y,z=[],[],[]
#x=p*(x2-x1)+x1
for i in range(len(x1)):
    xyz_temp=[]
    for j in range (len(x1[i])):
        if x1[i][j]!= "Ter":
            x1f= float(x1[i][j])+a
            x2f= float(x2[i][j])+a
            x_new=p*(x2f-x1f)+x1f

            y1f= float(y1[i][j])
            y2f= float(y2[i][j])
            y_new=p*(y2f-y1f)+y1f
            
            z1f= float(z1[i][j])
            z2f= float(z2[i][j])
            z_new=p*(z2f-z1f)+z1f
            
            xyz_temp.append("%s,%s,%s" %(x_new,y_new,z_new))
        else:
            x.append("Ter")
    x.append(xyz_temp)


#Originally Created By piac
#from https://gist.github.com/piac/ef91ac83cb5ee92a1294
#NOTE: for later use
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

xyz_list=x

#list_to_tree(x)