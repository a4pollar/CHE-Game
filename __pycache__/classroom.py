# A list of all departments that fall under the faculty of engineering
_all_departments = ["Architectural Engineering", "Architecture", "Biomedical Engineering", "Chemical Engineering",
                   "Civil Engineering", "Computer Engineering", "Electrical Engineering", "Environmental Engineering",
                   "Geological Engineering", "Management Engineering", "Mechanical Engineering",
                   "Mechatronics Engineering", "Nanotechnology Engineering", "Software Engineering",
                   "Systems Design Engineering"]


def _generate_birthdays(num_students):
    """
    Generates a list of birthdays, in format dd-mm-yyyy, for 'num_students' number of students.
    """
 
    # Import here so they don't show up when module is imported with *
    from datetime import date, datetime
    from random import randint

    # Check inputs
    if type(num_students) is not int:
        return None

    # Birth year for all students
    year_of_birth = 2000

    # Create the start and end dates (inclusive of both ends) between which randomly create birthdays
    # You have not seen this function before, don't worry about it.
    start_date_ordinal = datetime(year=year_of_birth, month=1, day=1).toordinal()
    end_date_ordinal = datetime(year=year_of_birth, month=12, day=31).toordinal()

    # Create the list into which to put birthday
    dates = []

    # Populate the list of birthdays
    for _ in range(num_students):
        # Generate the random birthday
        random_date = date.fromordinal(randint(start_date_ordinal, end_date_ordinal))

        # Extract the day and month of birth as numbers
        day = random_date.day
        month = random_date.month

        # Convert the birthday to a string
        birthday = "{:02d}-{:02d}-{}".format(day, month, year_of_birth)

        # Add it to the list of birthdays
        dates.append(birthday)

    return dates


def _generate_departments(num_students):
    """
    Generates a list of departments for 'num_students' number of students.
    Departments are taken from the all_departments variable defined at the top
    of this file.
    """
    
    # Import here so they don't show up when modeule is imported with *
    from random import randint

    # Check inputs
    if type(num_students) is not int:
        return None

    # Create the list
    departments = []

    # Populate the list of departments
    for _ in range(num_students):
        # Get a random index into all_departments
        random_department_index = randint(0, len(_all_departments) - 1)
        departments.append(_all_departments[random_department_index])

    return departments


def _generate_student_ids(num_students):
    """
    Generates a list of unique student ids for num_students number of students
    """

    # Check inputs
    if type(num_students) is not int:
        return None

    # Create the list
    ids = []

    # Populate the list of ids
    for i in range(num_students):
        ids.append(21502000 + i)

    return ids


def get_example_data():
    """
    Returns example data to use for testing.
    """
        
    # List of the names for the students
    names = ["Malcom Frye", "Cecilia Russell", "Kathy Singleton", "Derek Carlson", "Brant Huff", "Ronda Frey",
            "Gilbert Cameron", "Alana Hobbs", "Jerold Lindsey", "Gina Klein", "Santos Gilbert", "Ursula Davies",
            "Minh Rice", "Stanley Wilkinson", "Nicole Walker", "Lenore Hughes", "Franklyn Huynh", "Sophia Acevedo",
            "Derick Miranda", "Marjorie House", "Angel Hunter", "Rhett Stevens", "Haley Humphrey", "Dannie Lucero",
            "Peter Harrison", "Jesus Solis", "Ava Vang", "Teresa Blackburn", "Donny Mccormick", "Bob Macias",
            "Deloris Hampton", "Moises Owen", "Twila Estes", "Marshall Franklin", "Leland Holmes", "Loren Hebert",
            "Lane Archer", "Corinne Cox", "Ernesto Singh", "Berry Patton", "Cynthia Dougherty", "Deangelo Oliver",
            "Veronica Laura", "Tecla Angelique", "Uxia Eadbhard", "Depa Marylou", "Anja Cusmaan", "Milojica Raj",
            "Itziar Govind", "Chile Gustav", "Benthe Percival", "Thad Jurica", "Libuse Tabea", "Okeke Conchobhar",
            "Cora Zimmerman", "Myrna Thomas", "Susie Griffin", "Landon Nicholson", "Stacie Castaneda", "Fritz Malone",
            "Gerald Armstrong", "Lionel Gamble", "Raul Wang", "Valeria Trujillo", "Joann Weber", "Max Frank",
            "Leanne Vasquez", "Noemi Reilly", "Bobbie Blackburn", "Clement Lindsey", "Columbus Stephenson", "Anna Barron",
            "Ofelia Skinner", "Miquel Barajas", "Silas Gamble", "Willie Jefferson", "Katheryn Calderon",
            "Bertie Patterson", "Micheal Richmond", "Alyce Nash", "Raphael Hooper", "Celina Hebert", "Olen Santos",
            "Forrest Cummings", "Liliana Chaney", "Sheila Tran", "Noreen Barnes", "Casey Martin", "Mary English",
            "Beulah Robinson", "Willa Landry", "Don Joyce", "Gretchen Dillon", "Scott Chase", "Dewayne Peters",
            "Terrie Bentley", "Adolfo Gill", "Alphonso Ellison", "Petra Holt", "Bernice Sanders", "Emilia Durham",
            "Kristie Tyler", "Zelma Shah", "Lindsey Morton", "Wendy Forbes", "Tyrone Hatfield", "Brock Daniels",
            "Booker Dodson", "Lillie Beck", "Tamra Burns", "Ebony Fernandez", "Cathleen Chang", "Lupe Ross",
            "Domingo Townsend", "Joanna Wheeler", "Minnie Riley", "Staci Flynn", "Virginia Pacheco", "Daniel Beasley",
            "Katina Fitzpatrick", "Harvey Frye", "Buddy Burch", "Frances Koch", "Eddy Terrell", "Eugenia Lowe",
            "Carey Shaffer", "Earl Berger", "Rudolf Holder", "Ike Maynard", "Jaime Hartman", "Cliff Roy", "Aubrey Dodson",
            "Bobbie Garner", "Tuan Krueger", "Robbie Adams", "Matt Schneider", "Boris Howell", "Maryanne Rasmussen",
            "Emerson Meza", "Iris Reynolds", "Earle Mahoney", "Gracie Bright", "Manuel Hogan", "Faith Mcmahon",
            "Ruben Vasquez", "Nickolas Orozco", "Nathaniel Clay", "Jesse Liu", "Antony Pratt", "Newton Blake",
            "Andreas Avila", "Anne Walton", "David Farmer", "Abel Holloway", "Effie Andrews", "Alec Gaines", "Jeri Stark",
            "Cynthia Lopez", "Faye Torres", "Jolene Macdonald", "Lorenzo Aguirre", "Booker Holland", "Lupe Ross",
            "Domingo Townsend", "Joanna Wheeler", "Minnie Riley", "Staci Flynn", "Virginia Pacheco", "Daniel Beasley",
            "Katina Fitzpatrick", "Harvey Frye", "Buddy Burch", "Frances Koch", "Eddy Terrell", "Eugenia Lowe",
            "Carey Shaffer", "Itziar Govind", "Chile Gustave", "Benthe Percivel", "Thad Jurika", "Libuse Tabea",
            "Okece Conchobhar", "Diote Aline", "Nike Genove", "Eamon Frej", "Clio Apolonija", "Naile Laora", "Earl Berger",
            "Rudolf Holder", "Ike Maynard", "Jaime Hartman", "Cliff Roy", "Aubrey Dodson", "Bobbie Garner", "Tuan Krueger",
            "Robbie Adams", "Matt Schneider", "Boris Howell", "Maryanne Rasmussen", "Emerson Meza", "Iris Reynolds",
            "Earle Mahoney", "Gracie Bright", "Manuel Hogan", "Faith Mcmahon", "Ruben Vasquez", "Nickolas Orozco",
            "Nathaniel Clay", "Jesse Liu", "Antony Pratt", "Newton Blake", "Andreas Avila", "Anne Walton", "David Farmer",
            "Abel Holloway", "Effie Andrews", "Alec Gaines", "Jeri Stark", "Cynthia Lopez", "Faye Torres",
            "Jolene Macdonald", "Lorenzo Aguirre", "Booker Holland", "Selena Willis", "Selma Faulkner",
            "Martina Dominguez", "Kris Johnston", "Marisol Gallegos", "Jimmie Yates", "Rudy Patton", "Winifred Sweeney",
            "Lanny Reilly", "Madge Browning", "Kate Harmon", "Clyde Rose", "Robin Cervantes", "Susanna Hansen",
            "Virgilio Tucker", "Zane Dillon", "Florine Phillips", "Jasmine Pugh", "Nannie Waters", "Sharron Donaldson",
            "Alejandro Oliver", "Allison Houston", "Mauro Chambers", "Adalberto Arellano", "Tad Atkins", "Hans Mayer",
            "Kaitlin Strong", "Juliet Garrett", "Hattie Nielsen", "Elliot Good", "Tabitha Harding", "Tammy Zuniga",
            "Bud Mays", "Dillon Day", "Tamera Stout", "Debora Davis", "Matt Olsen", "Shayne Strickland", "Donna Clarke",
            "Lewis Pitts", "Miriam Banks", "Cedrick Burch", "Billie Blanchard", "Paul Garner", "Freda Evans",
            "Winfred Caldwell", "Jennifer Dougherty", "Rey Schroeder", "Marian Wyatt", "Darell Fuentes", "Helena Bishop",
            "Denny Mason", "Barton Bell", "Dorian Herrera", "Spencer Weeks", "Kelley Larsen", "Stacy Bautista",
            "Chelsea Bradshaw", "Megan Webster", "Arlene Joyce", "Kelli Boyd", "Dan Ramos", "Leann Mccoy", "Van Mack",
            "Aubrey Ray", "Eileen Livingston", "Walker Cline", "Douglas Marks", "Carmella Sosa", "Eleanor Brooks",
            "Clarence Hutchinson", "Edgar Stout", "Alejandra Woodward", "Tommie Bowers", "Bryant Madden", "Doris Hammond",
            "Connie Crawford", "Adrian Ware", "Douglass Harrison", "Mitch Lane", "Lacy Whitaker", "Blair Branch",
            "Petra Bryant", "Darrin Wiley", "Eldon Petersen", "Cornelius Copeland", "Orlando Kirby", "Alphonso James",
            "Robyn Key", "Imogene Castro", "Eugenia Lynn", "Betsy Chapman", "Dolores Davis", "Harvey Vaughan",
            "Jenny Salas", "Simone Knapp", "Jolene Shepard", "Danial Hernandez", "Angie Braun", "Merle Walker",
            "Helena Bishop", "Denny Mason", "Barton Bell", "Dorian Herrera", "Spencer Weeks", "Kelley Larsen",
            "Stacy Bautista", "Chelsea Bradshaw", "Megan Webster", "Arlene Joyce", "Kelli Boyd", "Dan Ramos",
            "Leann Mccoy", "Van Mack", "Aubrey Ray", "Eileen Livingston", "Walker Cline", "Douglas Marks", "Carmella Sosa",
            "Eleanor Brooks", "Clarence Hutchinson", "Edgar Stout", "Alejandra Woodward", "Tommie Bowers", "Bryant Madden",
            "Doris Hammond", "Connie Crawford", "Adrian Ware", "Douglass Harrison", "Mitch Lane", "Lacy Whitaker",
            "Blair Branch", "Petra Bryant", "Darrin Wiley", "Eldon Petersen", "Cornelius Copeland", "Orlando Kirby",
            "Alphonso James", "Robyn Key", "Eugenia Lynn", "Betsy Chapman", "Dolores Davis", "Harvey Vaughan",
            "Jenny Salas", "Simone Knapp", "Jolene Shepard", "Danial Hernandez", "Angie Braun", "Merle Walker",
            "Meical Megaera", "Rainard Derdriu", "Idalia Latifa", "Workneh Anacleto", "Donna Esmaralda", "Horus Nashwa",
            "Rhys Ninoslav", "Afanen Reva", "Jayashri Guro", "Eukene Asih", "Margaid Shokoufeh", "Mary Beth",
            "Zinovia Gyorgy", "Diot Aline", "Nike Genovaite", "Eamon Frej", "Clio Apolonija", "Naile Laura",
            "Meikal Megaera", "Rainart Derdriu", "Idalia Latiffa", "Workneh Anecleto", "Dona Esmaralda", "Horuz Nashwa",
            "Rhis Ninoslav", "Afanen Rewa", "Jayashri Guro", "Eukane Assih", "Marfaid Shokoufeh", "Mari Beth",
            "Zynovia Gyorgy", "Veronica Laora", "Tecla Angel", "Uxi Eadbhard", "Depa Marylou", "Anja Cusman",
            "Milojica Rajj"]

    # Number of students
    num_students = len(names)

    # List containing their date of births (dd-mm-yyyy) as a string
    birthdays = _generate_birthdays(num_students)

    # List of departments, each one MUST be from "all_departments"
    departments = _generate_departments(num_students)

    # List of student IDs, each represented as an int.
    student_ids = _generate_student_ids(num_students)

    return ((names, student_ids, birthdays, departments), _all_departments)