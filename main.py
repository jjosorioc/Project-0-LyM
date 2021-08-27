"""
Project 0
- Juan José Osorio (@jjosorioc)
- Luis Rubiano (@larubiano)
"""



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




with open("commands.txt", "r") as cmdFile:

    lines = cmdFile.readlines()
    lines.append("\n")


    
    print(filterByCommand(lines))


    lista_comandos = {
        'MOVE': 'int',
        'RIGHT': 'int',
        'LEFT': 'int',
        'ROTATE': 'int',
        'LOOK': [ # Lista por las coordenadas north east south west
            'N',
            'E',
            'W',
            'S'
        ],
        "DROP": 'int',
        "FREE": 'int',
        "PICK": 'int',
        "POP": 'int',
        "CHECK": (['C', 'B'], 'int'), # tuple -> (list, str)
        "BLOCKEDP": None, #es un boolean
        "NOP": None, #Robot doesn't do shit
    }
    
    #     Falta esto:
    #     A block of commands: (BLOCK commands) where commands is simply a se-
    # quence of one or more commands (separated by new lines).
    # { Iterative instructions: (REPEAT n [commands]), where n is a variable or a num-
    # bers describen the number of times the commands inside the [] will repeat,
    # and commands is a sequence of basic commands separated by new lines.
    # { A conditional command: IF expr [ commands ], where expr is a boolean ex-
    # pression, and commands is a sequence of basic commands separated by new
    # lines
    # { DEFINE n val { denes a new variable n assigning it value val (an integer).
    # Note that variable names need to be lowercase.
    # { TO f :param OUTPUT expression END. Functions are dened between the TO
    # and END keywords, giving them a name f and a list of space separated parame-
    # ters each dened by the colons before its name (as in :param). The inner works
    # of a function are given as an expression or block of commands in its OUTPUT.