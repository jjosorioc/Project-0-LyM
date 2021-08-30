"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano0)
"""


##################################### SETTINGS #####################################


import os
FILE_NAME = "commands.txt" #Name of the text file 


##################################### CONSTANTS ##################################### 


BASE_TEN_NUMBERS_ALPHABET = "0123456789" #An alphabet with all the possible symbols that can be found in a base ten number.
LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz" #An alphabet with all the possible symbols that can be found in a base ten number.


##################################### DATA #####################################


VARIABLE_DICTIONARY = {} #Python dictionary of all posible user created variables

COMMAND_DICTIONARY = {
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
        "NOP": None, #Robot ain't doin' shit
        "BLOCK": [], #All the possible commands that can be after a "BLOCK" statement
        "REPEAT": ['int', []], # tuple -> (int, COMMAND_LIST)
        "IF": ("BLOCKEDP",'!BLOCKEDP'), # tuple -> (bool,bool)
        "DEFINE": ('variable_name', 'int'), # tuple -> (str, int)
        'TO': ('f',) 
}

COMMAND_DICTIONARY["BLOCK"] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands
COMMAND_DICTIONARY["REPEAT"][1] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands


##################################### FUNCTIONS #####################################


def openFile(file_name: str)->list[str]:
    """Function to read the text file.
    
    Args:
        file_name: String with the name of the text file.

    Returns:
        lines (list[str]): Method readlines() for the text file.
    """
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name, "r") as cmdFile:
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



def verifyNameIsNotRestricted(name):
    """Function to verify a name for a variable or a command is not an already used name.
    
    Args:
        name: Name of the variable.

    Returns:
        (bool): Is the name for the variable allowed? True or False.
    """
    if name not in list(VARIABLE_DICTIONARY.keys()) + list(COMMAND_DICTIONARY.keys()):
        return True
    
    else:
        raise Exception("ERROR: " + name + " is a restricted name")


def addCommand(name,parameters):
    """Function to add or replace a command and its parameters.

    Args:
        name: The name of a command.
        parameters: The parameters of the command.

    Returns:
        (None)
    """
    
    COMMAND_DICTIONARY[name]=parameters
    COMMAND_DICTIONARY["BLOCK"] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands
    COMMAND_DICTIONARY["REPEAT"][1] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands


def addVariableIfInteger(name, value):
    """Function to save an integer as a variable, if value is an integer.

    Args:
        name: The name of a variable.
        value: A base ten integer.
        base_ten_numbers_alphabet: An alphabet with all the possible symbols that can be found in a base ten number.

    Returns:
        (None)
    """
    if verifyNameIsNotRestricted(name): 
        VARIABLE_DICTIONARY[name]=value
    else: raise Exception("ERROR: " + name + " is not an integer base 10")


#####def defineFunction():


##################################### EXECUTION #####################################
luchoNoSabeEscribirCodigo = True

if __name__ == "__main__" and luchoNoSabeEscribirCodigo:
    inputTxt = openFile(FILE_NAME)
    commandsInputFile = filterByCommand(inputTxt)


# DEBUG


for juan_jo_es_marica_si_borra_esto in commandsInputFile:
    print(juan_jo_es_marica_si_borra_esto)



#TODO:
#   Verificar recursión
#   Sistema Try Except para encontrar errores
#   Variable names lower case 
#   Variables no pueden tener nombres de comandos
#   Parametros temporales para las funciones ?? PREGUNTAR

# ERRORES : RESTRICTED NAME, NOT AN INTEGER BASE TEN, 

