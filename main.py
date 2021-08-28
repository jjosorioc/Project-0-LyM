"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano)
"""
# SETTINGS

file_name = "commands.txt" #Name of the text file 

# FUNCTIONS

def openFile(file_name: str):
    with open("commands.txt", "r") as cmdFile:
        lines = cmdFile.readlines()
        lines.append("\n")
    return lines


def filterByCommand(lines: list[str])->list[str]:
    """Function to separate each command in the "commands.txt" file.
    
    Args:
        lines (list[str]): Method readlines() for the commands.txt file.

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

#####def addVariable():

#####def defineFunction():

# DATA STRUCTURES

command_dictionary = {
        'MOVE': int,
        'RIGHT': int,
        'LEFT': int,
        'ROTATE': int,
        'LOOK': [ # Coordinate list north east south west
            'N',
            'E',
            'W',
            'S'
        ],
        "DROP": int,
        "FREE": int,
        "PICK": int,
        "POP": int,
        "CHECK": (['C', 'B'], int), # tuple -> (list, int)
        "BLOCKEDP": None, #is a bool
        "NOP": None, #Robot doesn't do shit
        "BLOCK": [], #All the possible commands that can be after a "BLOCK" statement
        "REPEAT" : (int, []), # tuple -> (int, command_list)
}

command_list = list(command_dictionary.keys()) #Python list of all the posible commands
command_dictionary["BLOCK"]=command_list
command_dictionary["REPEAT"][1]=command_list


variables = {} #Python dictionary of all posible user created variables




# EXECUTION
lines = openFile(file_name)
print(lines)




# DEV COMMENTS
    ##########Verificar recursión