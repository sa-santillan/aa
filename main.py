# Project
from pyscript import document, display

# Seatwork 1 (Club Member Checker)

ict_club_members = [
    "Joshua Ortiz",
    "Enzo Ruiz",
    "Logan Anaque",
    "Doctor Doom",
    "John Hizon",
    "Khabib Nurmagomedov"
]
# Checks if the name inputted is in the ICT Club Members list
def check_club_member(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
# Removes spaces at the start and end of the text, and makes it so that it is not case-sensitive
    club_member_name = f"{first_name.strip()} {last_name.strip()}".title()
# Checks if the name is in the list
    is_member = club_member_name in ict_club_members

    # Different messages shown to the user depending on whether they are a member
    messages = [
        "Sorry " + club_member_name + ", your name is not on the list.",
        "Congratulations " + club_member_name + "! You are now part of the ICT club."
    ]

    # Displays the Candidate Verification System
    document.getElementById("result").innerHTML = ""
    display(messages[is_member], target="result")

# Skills Test (Element Checker)

nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.002),
    "F": ("Fluorine", 9, 19.00),
    "Ne": ("Neon", 10, 20.18),
    "P": ("Phosphorus", 15, 30.97),
    "C": ("Carbon", 6, 12.01),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Se": ("Selenium", 34, 78.96),
    "Br": ("Bromine", 35, 79.90),
    "I": ("Iodine", 53, 126.90),
    "Ar": ("Argon", 18, 39.95),
    "Kr": ("Krypton", 36, 83.80),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}

# Searches the dictionary for the entered element
def search_element(e):

    # Gets the input and corrects its capitalization
    Nonmetal1 = document.getElementById("nonmetal1").value.strip().capitalize()

    # Gets the element's properties or shows a fallback message
    result = nonmetals.get(Nonmetal1, ("Non-metal not found", "-", "-"))

    # Displays the element's properties
    document.getElementById("symbol").innerText = Nonmetal1
    document.getElementById("name").innerText = result[0]
    document.getElementById("atomic_number").innerText = result[1]
    document.getElementById("atomic_mass").innerText = result[2]

# Drill 2 (ICT Club Members)

# Sets for each grade
grade_7 = {"Doctor Doom", "Iron Man"}
grade_8 = {"Khabib Nurmagomedov", "Islam Makhachev"}
grade_9 = {"Joshua Ortiz", "John Hizon"}
grade_10 = {"Logan Anaque", "Enzo Ruiz"}

# Combines all grade sets
all_members = grade_7 | grade_8 | grade_9 | grade_10

# Displays all members and the total amount
def show_members():
    members_list = "<br>".join(sorted(all_members))

    # Displays the members and total inside the results box
    document.getElementById("club_members_result").innerHTML = (
        f"ALL MEMBERS:<br>{members_list}<br><br>TOTAL MEMBERS: {len(all_members)}"
    )

# Adds a new club member
def add_club_member(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    # Adds the full name to the set
    all_members.add(first_name + " " + last_name)

    # Updates the displayed results
    show_members()

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
