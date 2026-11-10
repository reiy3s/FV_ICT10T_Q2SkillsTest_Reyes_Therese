from pyscript import display, document

#Element Name, info, info, info
elements = {"Hydrogen": ("H", "Hydrogen", 1, 1)}

# Function to search for an element
def search_element(e):
    # get input value
    element1 = document.getElementById("element").value