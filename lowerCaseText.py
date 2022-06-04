#
# PYTHON CODE QUESTION:
#
# Can you write Python code to turn text to lower case?
#
# Input:  list of words (strings)
#
# Output: string in lower
#

def codeToTurnTextIntoLowerCase(inString):
  
    stringtext = ""
    
    if(inString is None):
        stringtxt = ["Welcome", "to", "Qwykrtech", "This","Is","JuSt","An","EXAMPLE"]

    stringtxt_lower = [x.lower() for x in stringtxt]

    print(stringtxt_lower)
    return stringtext_lower
  
 codeToTurnTextIntoLowerCase()
