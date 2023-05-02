"""
Name:print_title.py
Author:Rex
Date:2/21/23
Purpose: Print program title function or module
"""

"""
Notes about arrays:

append() adds a new element to the end of a list
insert() places a new element at a designated index and moves other aside
sort() sorts values lowest to highest
reverse() reverse original value of list
index() looks for first instance of value in list
count() looks for total instances of value in list
remove() removes an item with a certain value
del removes an item at an index
pop() removes an item fro a list at a designated index and returns a value
extend() takes a list as an argument and appends all the elements)
join() string method: joins two lists
"""

#from rich.console import Console
#from rich.panel import Panel
#Make sure to also initiate console (console = Console() )
from rich.console import Console
from rich.panel import Panel
console = Console()


def cool_title():
    #Print a nice title for our program
    console.print(
        Panel.fit(
        "-----Da Code-----",
        style="blue",
        subtitle="By SirRexOfRider")
    )

def get_float(prompt):
    """
    Get a number from the user with try catch
    The prompt string parameter is used toa sk the user
    for the type of input needed
    """
    #Delcare local variable
    num = 0

    #Ask the user for an input based on the what parameter
    num = input(prompt)

    #If the input is numeric, convert to float and return value
    try:
        return float(num)
    #If teh input is not numeric, infomr the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")
        #Call function from the beginning
        #This is a recursive function call
        return get_float(prompt)







def get_int(prompt):
    """
    Get an integer from the user with try catch
    The prompt string parameter is used to ask the user
    for the type of input needed
    """
    #Declare local variable
    num = 0

    #Ask the user for an input based on the prompt string parameter
    num = input(prompt)

    #If the input is numeric, convert to int and return value
    try:
        return int(num)

    #If the input is not numeric,
    #Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a whole number.")
        print(f"Let's try that agian. \n")

        #Call function fromm the beginning
        #This is a recursive function vall
        return get_int(prompt)


def main():
    print(title("Print Title"))

def title(statement):
    """Takes in a string argument and returns a string with ascii decorations"""
    #Get the length of the statement
    text_length = len(statement)
    
    #Create the title string
    #Initialize the result string vaiable
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result

#If standalone, else use as module
if __name__ == "__main__":
    main()
