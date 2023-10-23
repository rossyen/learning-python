# molecular-weight.py
#   A program that calculates the molecular weight of a carbohydrate
#   in grams per mole, based on the number of hydrogens,
#   carbon, and oxygen atoms in the molecule.

# define function
def molecule_weight():

# print about program
    print('This is a program that calculates the weight of a carbohydrate based on ')
    print('the number of hydrogen, carbon, and oxygen atoms in the molecule.')

# receive input on number of carbohydrates
    hydrogen = int(input('Enter number of hydrogens: '))
    carbon = int(input('Enter number of carbon: '))
    oxygen = int(input('Enter number of oxygen: '))
    
# define weight on hydrogen, carbon and oxygen
    hydrogen = hydrogen * 1.00794
    carbon = carbon * 12.0107
    oxygen = oxygen * 15.9994

# calculate weight of input
    total_weight = hydrogen + carbon + oxygen
# print total combined molecular weight of all atoms
    print(f'The total combined molecular weight of all the atoms based on input is: {total_weight:.4f}.')

molecule_weight()