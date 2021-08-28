"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano)
"""
# SETTINGS

file_name = "commands.txt" #Name of the text file 

# CONSTANTS 

base_ten_numbers_alphabet = "0123456789" #An alphabet with all the possible symbols that can be found in a base ten number.
global variables #Python dictionary of all posible user created variables

# FUNCTIONS

def openFile(file_name: str)->list[str]:
    """Function to read the text file.
    
    Args:
        file_name: String with the name of the text file.

    Returns:
        lines (list[str]): Method readlines() for the text file.
    """
    with open("commands.txt", "r") as cmdFile:
        lines = cmdFile.readlines()
        lines.append("\n")
    return lines


def filterByCommand(lines: list[str])->list[str]:
    """Function to separate each command in the text file.
    
    Args:
        lines (list[str]): Method readlines() for the text file.

    Returns:
        list[str]: Each index is its own command.
    """
    indice = 0 # First index of 'lines'
    indiceDelComando = indice + 1 # Second index of 'lines' // It's the last index of each command.
    nuevaLista = [] # List the function will return
    while (indiceDelComando < len(lines)):

        if (lines[indiceDelComando] == "\n"):
            cadenaDelComando = "" #String that will be appended to the list. It's a string with the command.

            for numero in range(indice, indiceDelComando):  #Iterates to get all words in the command.
                cadenaDelComando = cadenaDelComando + lines[numero]

            if cadenaDelComando != '':
                nuevaLista.append(" ".join(cadenaDelComando.split()))

            indice = indiceDelComando
            indiceDelComando = indice + 1

        
        if (indiceDelComando < len(lines) and lines[indice]=="\n" and lines[indiceDelComando] == "\n"):
            indice += 2
            indiceDelComando += 2

        
        else:
            indiceDelComando += 1
        
    return nuevaLista


def VerifyIsInAlphabet(sequence_of_symbols, alphabet)->bool:
    """Function to verify a sequence of symbols is over a given alphabet.
    
    Args:
        sequence_of_symbols: An arbitrary sequence of symbols.
        alphabet: An alphabet

    Returns:
        (bool): Is the sequence of symbols over the alphabet? True or False.
    """
    for i in sequence_of_symbols: 
        if i not in alphabet: return False
    return True 


def addIntegerVariable(name, value, base_ten_numbers_alphabet):
    """Function to save an integer as a variable, if value is an integer.

    Args:
        name: The name of a variable.
        value: A base ten integer.
        base_ten_numbers_alphabet: An alphabet with all the possible symbols that can be found in a base ten number.

    Returns:
        (None)
    """
    if VerifyIsInAlphabet(value, base_ten_numbers_alphabet)==True: variables[name]=value
    else: raise Exception("ERROR: " + name + " is not an integer base 10")

#####def defineFunction():

# DATA STRUCTURES

variables = {} #Python dictionary of all posible user created variables

command_dictionary = {
        'MOVE': 'int',
        'RIGHT': 'int',
        'LEFT': 'int',
        'ROTATE': 'int',
        'LOOK': [ # Coordinate list north east south west
            'N',
            'E',
            'W',
            'S'
        ],
        "DROP": 'int',
        "FREE": 'int',
        "PICK": 'int',
        "POP": 'int',
        "CHECK": (['C', 'B'], 'int'), # tuple -> (list, int)
        "BLOCKEDP": None, #bool
        '!BLOCKEDP': None, #bool
        "NOP": None, #Robot doesn't do shit
        "BLOCK": [], #All the possible commands that can be after a "BLOCK" statement
        "REPEAT": ('int', []), # tuple -> (int, command_list)
        "IF": ("BLOCKEDP",'!BLOCKEDP'), # tuple -> (bool,bool)
        "DEFINE": ('variable_name', 'int'), # tuple -> (str, int)
        'TO': ('f',) #????

}
command_list = list(command_dictionary.keys()) #Python list of all the posible commands
command_dictionary["BLOCK"]=command_list
command_dictionary["REPEAT"][1]=command_list






# EXECUTION
lines = openFile(file_name)
print(lines)




# DEV COMMENTS
    ##########Verificar recursión
    ########## Sistema Try Except para encontrar errores
    ########## Variable names lower case