from main import (BASE_TEN_NUMBERS_ALPHABET,
                  LOWERCASE_ALPHABET,
                  UPPERCASE_ALPHABET,
                  VARIABLE_DICTIONARY,
                  COMMAND_DICTIONARY)
import os
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
        lines.append("\n") # Adds blank line so the filterByCommand function wont't show an error.
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




def filterByToken(lista: list[str])->list[str]:
    """List to filter the 'commandsInputFile' list by each token.

    Args:
        lista (list[str]): List by commands.

    Returns:
        list[str]: List by each token.
    """

    newList = []  # lista separada por los espacios
    newNewList = []

    for command in lista:
        command = command.replace('(',' ( ')
        command = command.replace(')',' ) ')
        command = command.replace('[',' [ ')
        command = command.replace(']',' ] ')
        splitDelCommand = command.split(' ') # Nueva lista separada por los espacios

        for token in splitDelCommand:
            newList.append(token)

    for i in newList:
        if i != '':
            # i es cada Token, incluyendo: [] ()
            newNewList.append(i)

    return newNewList




def readLineByLine(lines: list[str], localVars = None):
    """Reads the code line by line.

    Args:
        lista (list[str]): List by each token.
        localVars (list): Local variables of a function, by default none, can be used in recursion cases.  

    Returns:
        (None)
    """
    countA = 0 #Current index of the Token

    while countA < len(lines):
        
        
        if lines[countA] not in COMMAND_DICTIONARY:
            #print(lines[countA])
            #print(COMMAND_DICTIONARY)
            raise Exception("\n"*5 + "ERROR: Undefined command " + lines[countA] + "\n"*5)
        

        command = lines[countA] #Current command


        if command == "(":
            countA += 1
            command += lines[countA]


        if command == "(BLOCK":
            recursiveLines = []
            while lines[countA+1] != ")":  #While the block hasn't stopped.
                countA += 1
                recursiveLines.append(lines[countA])

            countA += 1
            readLineByLine(recursiveLines)

        elif command == "(REPEAT":
            countA += 1
            isIntegerOrVariable(lines[countA])
            recursiveLines = []
            countA += 1
            if not lines[countA] == "[":
                raise Exception("\n"*5 + "ERROR: Expected [, found " + lines[countA] +  " instead" + "\n"*5)
            while lines[countA+1]!="]":
                countA += 1
                recursiveLines.append(lines[countA])
            countA += 1
            if not lines[countA] == ")":
                raise Exception("\n"*5 + "ERROR: Expected ), found " + lines[countA] +  " instead" + "\n"*5)  
            countA += 1
            readLineByLine(recursiveLines)

        elif command == "TO":
            split_list = []
            split_list.append(lines[countA])
            while lines[countA]!="END":
                countA += 1
                split_list.append(lines[countA])
            recursiveLines, localVars = defineFunction(split_list)
            readLineByLine(recursiveLines,localVars)

        elif command == "IF":
            countA += 1
            if not lines[countA] in COMMAND_DICTIONARY[command][0]:
                raise Exception("\n"*5 + "ERROR: Argument " + lines[countA] + " is incorrect" + "\n"*5)
            countA += 1
            if lines[countA] != '[':
                raise Exception("\n"*5 + "ERROR: Missing [ on if command" + "\n"*5)
            countA += 1
            recursiveLines = [] 
            while lines[countA+1]!="]":
                recursiveLines.append(lines[countA])
                countA += 1
            countA += 1
            readLineByLine(recursiveLines)
            
        elif type(COMMAND_DICTIONARY[command]) == None:
            pass #Robot doesn't do anything
    
        else:
            countB = 0 #Current argument within command
            
            while countB < len(COMMAND_DICTIONARY[command]):
                countA += 1
                if COMMAND_DICTIONARY[command][countB] == "int":
                    isIntegerOrVariable(lines[countA],localVars)
                elif COMMAND_DICTIONARY[command][countB] == 'variable_name':
                    addVariableIfInteger(lines[countA],lines[countA+1])
                elif COMMAND_DICTIONARY[command][countB] == 'error':
                    raise Exception("\n"*5 + "ERROR: Syntax error" + "\n"*5)
                elif type(COMMAND_DICTIONARY[command][countB]) == list:
                    if not lines[countA] in COMMAND_DICTIONARY[command][countB]:
                        raise Exception("\n"*5 + "ERROR: Argument " + lines[countA] + " is incorrect" + "\n"*5)
                countB += 1

        countA += 1


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


def verifyVariableNameIsAllowed(name: str):
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


def isIntegerOrVariable(n, localVars = None):
    """Function to verify a parameter is either an integer or a user-saved integer variable.
    
    Args:
        n: An integer or a user-saved integer variable.
        localVars (list): Local variables of a function, by default none, can be used in recursion cases.  

    Returns:
        (None)
    """
    if (localVars) != None:
        if not (verifyIsInAlphabet(n, BASE_TEN_NUMBERS_ALPHABET) or (n in VARIABLE_DICTIONARY) or (n in localVars)):
            raise Exception("\n"*5 + "ERROR: " + n + " variable is undefined" + "\n"*5)
    else:
        if not (verifyIsInAlphabet(n, BASE_TEN_NUMBERS_ALPHABET) or (n in VARIABLE_DICTIONARY)):
            raise Exception("\n"*5 + "ERROR: " + n + " variable is undefined" + "\n"*5)


def addCommand(name: str, args):
    """Function to add or replace a command and its parameters.

    Args:
        name: The name of a command.
        args: The parameters of the command.

    Returns:
        (None)
    """
    COMMAND_DICTIONARY[name] = args


def addVariableIfInteger(name: str, value):
    """Function to save an integer as a variable, if value is an integer.

    Args:
        name: The name of a variable.
        value: A base ten integer.

    Returns:
        (None)
    """
    if (verifyIsInAlphabet(value, BASE_TEN_NUMBERS_ALPHABET)) and (verifyVariableNameIsAllowed(name)) and (verifyIsInAlphabet(name, LOWERCASE_ALPHABET)): 
        VARIABLE_DICTIONARY[name] = value
    else:
        raise Exception("\n"*5 + "ERROR: Syntax error regarding " + name + " variable" + "\n"*5)


def defineFunction(split_list:list[str])->list[str]:
    """Function to define a new TO command.
    Args:
        split_list (list[str]): Python list with the whole TO function.
    Returns:
        list[str]: The expression inside the function to be asserted afterwards
    """
    name = split_list[1]
    localVars = []

    if not ((split_list[0] == "TO") and (split_list[-1]=="END") and ("OUTPUT" in split_list)):
        raise Exception("\n"*5 + "ERROR: Wrong syntax for the function: " + name + "\n"*5)

    if not (verifyIsInAlphabet(name, LOWERCASE_ALPHABET + UPPERCASE_ALPHABET + BASE_TEN_NUMBERS_ALPHABET) and verifyVariableNameIsAllowed(name) and verifyIsInAlphabet(name[0], LOWERCASE_ALPHABET + UPPERCASE_ALPHABET)): 
        raise Exception("\n"*5 + "ERROR: Wrong name for the function: " + name + "\n"*5)
    arguments = []
    count = 2
    while True:
        if split_list[count]=="OUTPUT":
            break
        if split_list[count][0] != ":":
            raise Exception("\n"*5 + "ERROR: Wrong argument syntax for the function: " + name + "\n"*5)
        if not (verifyIsInAlphabet(split_list[count][1:], LOWERCASE_ALPHABET) and verifyVariableNameIsAllowed(split_list[count][1:])): 
            raise Exception("\n"*5 + "ERROR: Wrong name for the argument: " + split_list[count][1:] + " in the function: " + name + "\n"*5)
        arguments.append(split_list[count][1:])
        localVars.append(split_list[count])
        count+=1
    arguments = tuple(arguments)
    addCommand(name,arguments)
    count+=1
    recursiveLines = []
    while split_list[count]!="END":
        recursiveLines.append(split_list[count])
        count += 1
    return (recursiveLines,localVars)
