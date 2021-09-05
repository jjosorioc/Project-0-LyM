"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano0)
"""


##################################### SETTINGS #####################################
import model

#FILE_NAME = "commands.txt" #Name of the text file 

# commands.txt
# deletelater.txt


##################################### CONSTANTS ##################################### 


BASE_TEN_NUMBERS_ALPHABET = "0123456789" #An alphabet with all the possible symbols that can be found in a base ten number.
LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz" #An alphabet with all the possible symbols that can be found in a base ten number.
UPPERCASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 


##################################### DATA #####################################


VARIABLE_DICTIONARY = {} #Python dictionary of all posible user created variables

COMMAND_DICTIONARY = {
        'MOVE': ('int',), #Tuple
        'RIGHT': ('int',),
        'LEFT': ('int',),
        'ROTATE': ('int',),
        'LOOK': ([ # Coordinate tuple north east south west
            'N',
        'E',    'W',
            'S'
                ],),
        "DROP": ('int',),
        "FREE": ('int',),
        "PICK": ('int',),
        "POP": ('int',),
        "CHECK": (['C', 'B'], 'int',), # tuple -> (list, int)
        "BLOCKEDP": None, #bool
        '!BLOCKEDP': None, #bool
        "NOP": None, 
        "BLOCK": ("error",), #Block command without a previous '('
        "REPEAT": ("error",),
        "IF": (["BLOCKEDP",'!BLOCKEDP'], "[", "commands", "]"), 
        "DEFINE": ('variable_name', 'int',), # tuple -> (str, int)
        'TO': ('f' , ':param' ,'OUTPUT', "commands", 'END'),
        '(BLOCK':("commands",')'), #All the possible commands that can be after a "BLOCK" statement #Fix with repeat
        "(REPEAT": ('int', "[", "commands", "]", ")"),
        '(':None
}



##################################### EXECUTION #####################################


if __name__ == "__main__":
    FILE_NAME = input("\nEnter the name of the Text file without the '.txt' extension: ") + ".txt"

    
    inputTxt = model.openFile(FILE_NAME)
    
    commandsInputFile = model.filterByCommand(inputTxt)
    
    tokenList = model.filterByToken(commandsInputFile)
    
    model.readLineByLine(tokenList)
    
    print("\n"*10 + "The code is good to go :)" + "\n"*10)


##################################### DEBUG #####################################


#TODO: Encontrar errores: Que pasa cuando se acaba el código y no se encuentra un delimitador ")" o "]"


