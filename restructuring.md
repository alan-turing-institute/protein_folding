# Moving more of the content from Grasshopper to Python

# Read the PDBs
Review options for reading and writing PDB files - either 3rd party, or roll our own

# New feature - Remove the hydrogen atoms
** ALl `H` are invalid. (In the final column).

# New feature - Test whether two .pdb files are *chemically* the same.

Add an unique ID, consisting of:
* Name of Atom (column 3)
* Chain ID (column 5)
* Number of Amino Acid (column 6)

* If there is the same set of UIDs (in any order) then the two .pdbs are chemically the same (but might be geometrically different)
* If there are different UIDs, then they are different chemically.



Test Cases:
----------
Develop some tests cases for error checking inout and output PDB files.

Assumed functions:
-----------------
def are_proteins_chemically_equivilent(pdb_1, pdb_2):
    pass

def are_proteins_geometrically_equivilent(pdb_1, pdb_2):
    pass

def load_pdb(f_path):
    """
    Returns a Protein object
    """
    pass


# "Happy valley" of passing cases:

# Case 01; Using the same file as state_1 and state_2
pdb_1 = load_pdb("GlyP_AMP.pdb")
pdb_2 = load_pdb("GlyP_AMP.pdb")

assert are_proteins_chemically_equivilent(pdb_1, pdb_2)
assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)

# Case 02; Example files, with two identical chains. The order fo the chains in the files is swapped between the two files.
pdb_1 = load_pdb("two_short_chains_forward.pdb")
pdb_2 = load_pdb("two_short_chains_reverse.pdb")

assert are_proteins_chemically_equivilent(pdb_1, pdb_2)
assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)

# Different Geometries

# Case 10; Single chain, different geometry
pdb_1 = load_pdb("single_short_chain_geom_real.pdb")
pdb_2 = load_pdb("single_short_chain_geom_fake.pdb")

assert are_proteins_chemically_equivilent(pdb_1, pdb_2)

error_msg = "An informative RegEx about _where_ the difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=error_msg):
    assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)


# Case 11; Two chains, different geometry in one chain only
pdb_1 = load_pdb("two_short_chains_geom_real.pdb")
pdb_2 = load_pdb("two_short_chains_geom_fake.pdb")

assert are_proteins_chemically_equivilent(pdb_1, pdb_2)

error_msg = "An informative RegEx about _where_ the difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=error_msg):
    assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)


# Chemically Different Proteins

# Case 20; Two chains, one of which has different Atom/Amino Acid combos
pdb_1 = load_pdb("two_short_chains_forward.pdb")
pdb_2 = load_pdb("two_short_chains_diff_atoms.pdb")

chem_error_msg = "An informative RegEx about the _chemical_ difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=chem_error_msg):
    assert are_proteins_chemically_equivilent(pdb_1, pdb_2)

# TBC: what is the correct, meaningful error message in this case?
geom_error_msg = "An informative RegEx about the _geometrical_ difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=error_msg):
    assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)


# Case 21; Two chains, one of which has extra hydrogen atoms
pdb_1 = load_pdb("two_short_chains_forward.pdb")
pdb_2 = load_pdb("two_short_chains_extra_hydrogen.pdb")

chem_error_msg = "An informative RegEx about the _chemical_ difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=chem_error_msg):
    assert are_proteins_chemically_equivilent(pdb_1, pdb_2)

# TBC: what is the correct, meaningful error message in this case?
geom_error_msg = "An informative RegEx about the _geometrical_ difference occurs (eg line numbers)"
with pytest.raises(ValueError, match=error_msg):
    assert are_proteins_geometrically_equivilent(pdb_1, pdb_2)


# Parameter order
# All of the tests above should be indifferent to the order of the two files (except where the error message
# points to a line-number of a specifc file). There should be tests to confirm this behaviour.ß
TBC...


# How to generate the test files
# Create two individual short chains
pdb_tidy GlyP_AMP.pdb | pdb_selchain -A | pdb_head -10 | pdb_tidy -strict > chain_a.pdb
pdb_tidy GlyP_AMP.pdb | pdb_selchain -B | pdb_head -10 | pdb_tidy -strict > chain_b.pdb

# Merge the two short chains together
pdb_merge chain_a.pdb chain_b.pdb | pdb_tidy -strict > two_short_chains_forward.pdb 
pdb_merge chain_b.pdb chain_a.pdb | pdb_tidy -strict > two_short_chains_reverse.pdb 


# Create single chain with fake geometry
# Takes chemical data from `chain_a.pdb` and geometry from `chain_b.pdb` and outputs a new file:
python create_fake_geom.py chain_a.pdb chain_b.pdb | pdb_tidy -strict > single_short_chain_geom_fake.pdb 
pdb_tidy -strict chain_a.pdb > single_short_chain_geom_real.pdb 


# Create a new chain (by arbitarily removing oxygen from chain-a).
pdb_tidy GlyP_AMP.pdb | pdb_selchain -B | pdb_delelem -O | pdb_head -10 | pdb_tidy -strict > chain_c.pdb
pdb_merge chain_a.pdb chain_c.pdb | pdb_tidy -strict > two_short_chains_diff_atoms.pdb


# Create files each with two chains. One chain in one file has extra hydrogens
pdb_tidy -strict GlyP_AMP_extra_hydrogens.pdb | pdb_selchain -A | pdb_delelem -H | pdb_head -20 | pdb_tidy -strict > chain_ha1.pdb
pdb_tidy -strict GlyP_AMP_extra_hydrogens.pdb | pdb_selchain -A | pdb_head -35 | pdb_tidy -strict > chain_ha2.pdb
pdb_tidy -strict GlyP_AMP_extra_hydrogens.pdb | pdb_selchain -B | pdb_head -20 | pdb_tidy -strict > chain_hb.pdb
pdb_tidy -strict GlyP_AMP_extra_hydrogens.pdb | pdb_selchain -B | pdb_delelem -H | pdb_head -20 | pdb_tidy -strict > chain_hb.pdb
pdb_merge chain_ha1.pdb chain_hb.pdb | pdb_tidy -strict > two_chains.pdb
pdb_merge chain_ha2.pdb chain_hb.pdb | pdb_tidy -strict > two_chains_extra_hydrogen.pdb


