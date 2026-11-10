from pyscript import display, document

#Element Name, info, info, info
elements = {"HYDROGEN": ("H", "Hydrogen", 1, 1.00),
            "HELIUM": ("He", "Helium", 2, 4.00),
            "CARBON": ("C", "Carbon", 6, 12.01),
            "NITROGEN": ("N", "Nitrogen", 7, 14.01),
            "OXYGEN": ("O", "Oxygen", 8, 16.00),
            "FLUORINE": ("F", "Fluorine", 9, 19.00),
            "SULFUR": ("S", "Sulfur", 16, 32.07),
            "CHLORINE": ("Cl", "Chlorine", 17, 35.45),
            "ARGON": ("Ar", "Argon", 18, 39.95),
            "SELENIUM": ("Se", "Selenium", 34, 78.96),
            "BROMINE": ("Br", "Bromine", 35, 79.90),
            "KYRPTON": ("Kr", "Krypton", 36, 83.80),
            "IODINE": ("I", "Iodine", 53, 126.90),
            "XENON": ("Xe", "Xenon", 54, 131.29),
            "ASTATINE": ("At", "Astatine", 85, 210.00),
            "RANDON": ("Rn", "Radon", 86, 222.00),
            "TENNESSINE": ("Ts", "Tenessine", 118, 294.00),
            "OGANESSON": ("Og", "Oganesson", 118, 294.00)
            }

# Function to search for an element
def search_element(e):
    # get input value
    element1 = document.getElementById("element1").value #get info from dict
    result = elements.get(element1, ("Element not found, maybe it's not a non-metal element?", "N/A", "N/A", "N/A")) #fall back if not found
    #display the result
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("atomic_#").innerText = result[2]
    document.getElementById("atomic_m").innerText = result[3]