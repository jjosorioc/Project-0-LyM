"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano0)
"""


##################################### SETTINGS #####################################


import os
from posixpath import split
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
        'TO': ['f' , ':param' ,'OUTPUT', [], 'END']
}

COMMAND_DICTIONARY["BLOCK"] = COMMAND_DICTIONARY["REPEAT"][1] = COMMAND_DICTIONARY["TO"][3] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands


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


def verifyIsInAlphabet(sequence_of_symbols, alphabet)->bool:
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
        return False


def addCommand(name,parameters):
    """Function to add or replace a command and its parameters.

    Args:
        name: The name of a command.
        parameters: The parameters of the command.

    Returns:
        (None)
    """
    COMMAND_DICTIONARY[name]=parameters
    COMMAND_DICTIONARY["BLOCK"] = COMMAND_DICTIONARY["REPEAT"][1] = COMMAND_DICTIONARY["TO"][3] = list(COMMAND_DICTIONARY.keys()) #Python list of all the posible commands


def addVariableIfInteger(name, value):
    """Function to save an integer as a variable, if value is an integer.

    Args:
        name: The name of a variable.
        value: A base ten integer.

    Returns:
        (None)
    """
    if verifyIsInAlphabet(value, BASE_TEN_NUMBERS_ALPHABET) and verifyNameIsNotRestricted(name) and verifyIsInAlphabet(name, LOWERCASE_ALPHABET): 
        VARIABLE_DICTIONARY[name]=value
    else: raise Exception("ERROR: Grammar error regarding " + name + " varkable")


def defineFunction(TO_command):
    """Function to define a new TO command.

    Args:
        TO_command: Python string with the whole TO function.

    Returns:
        (None)
    """
    split_list = TO_command.split(" ")
    name = split_list[1]
    if not (split_list[0]=="TO" and split_list[-1]=="END" and ("OUTPUT" in split_list)):
        raise Exception("ERROR: Wrong grammar for the function: " + name)
    if not (verifyIsInAlphabet(name, BASE_TEN_NUMBERS_ALPHABET) and verifyNameIsNotRestricted(name)): 
        raise Exception("ERROR: Wrong name for the function: " + name)
    pass

##################################### EXECUTION #####################################


luchoNoSabeEscribirCodigo = True

if __name__ == "__main__" and luchoNoSabeEscribirCodigo:
    inputTxt = openFile(FILE_NAME)
    commandsInputFile = filterByCommand(inputTxt)


##################################### DEBUG #####################################


for juan_jo_es_marica_si_borra_esto in commandsInputFile:
    print(juan_jo_es_marica_si_borra_esto)


#TODO:
#   Verificar recursión
#   Sistema Try Except para encontrar errores
#   Variable names lower case 
#   Variables no pueden tener nombres de comandos
#   Parametros temporales para las funciones ?? PREGUNTAR