import re

def ParseElementString(string):
    # Parse Element name strings to find the names and quantities of individual elements
    # Handles chemical names w/o coefficients behind each element (Like in CH4 or N2O)
    # M. Hageman 11/2018
    # Original, Primary Matlab code taken verbatim from Fangjun Jiang on MATLAB Answers:
    # https://www.mathworks.com/matlabcentral/answers/13600-how-to-extract-info-from-a-chemical-formula
    # Accessed 11/6/2018
    #Converted to Python 9/18/2023 using ChatGPT

    # Inputs:
    # str = Chemical name
    # Output:
    # EleList = list of element names
    # NumList = list of element coefficients

    # Initialize lists to store element names and coefficients
    ElementList = []
    NumberList = []
    i = 0
    while i < len(string):
        if string[i].isalpha(): #is the character in position i an alphabetic letter?
            element = string[i] #Initialize variable "element" with that letter.
            i += 1 #increment i to the next position
            while i < len(string) and string[i].islower(): #Collects lowercase letters that are part of the element name.
                element += string[i] #append the lowercase letter to the element name.
                i += 1 #increment i to the next position
            ElementList.append(element) #Once element name is complete, append it to the element list.
            if i < len(string) and string[i].isdigit(): #is the character in position i a digit (0-9)
                number = "" #initialize empty string "number"
                while i < len(string) and string[i].isdigit():
                    number += string[i] #append digit to the "number" string
                    i += 1 #increment i to the next position
                NumberList.append(int(number)) #Once numeric portion is fully collected, convet to integer, and append to NumberList.
            else:
                NumberList.append(1)
        else:
            i += 1 #increment i to the next position
    return ElementList, NumberList

#Pythong loops are ended by changing indentation.

