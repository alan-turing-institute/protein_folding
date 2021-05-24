"""Script to filter PDB files.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a P variable"""

__author__ = "Flora"
__version__ = "2020.10.23"

import rhinoscriptsyntax as rs

PDB = PDB.replace("            ",",")
PDB = PDB.replace("           ",",")
PDB = PDB.replace("          ",",")
PDB = PDB.replace("         ",",")
PDB = PDB.replace("        ",",")
PDB = PDB.replace("       ",",")
PDB = PDB.replace("      ",",")
PDB = PDB.replace("     ",",")
PDB = PDB.replace("    ",",")
PDB = PDB.replace("   ",",")
PDB = PDB.replace("  ",",")
PDB = PDB.replace(" ",",")
#PDB = PDB.replace("TER,","")

if PDB.find("TER"):
    P = PDB