import data_manager

# --- Student Service Functions ---

def get_all_students_service():
    """
    STORY: The principal needs a complete list of every student. This service
    function's only job is to ask the data_manager for the raw student data.
    It doesn't do any filtering or processing itself.

    INPUT: None
    OUTPUT: A list of lists, containing all student records.
    """
    return data_manager.get_all_students()

def get_students_by_class_service(class_name):
    """
    STORY: A teacher wants to see all students in their class. This service
    function orchestrates the process.

    INPUT:
    - class_name (string): The class to filter by (e.g., "10").

    PROCESS:
    1. Ask the data_manager for the full list of students.
    2. Filter that list to find only the students in the specified class.

    OUTPUT: A list of lists, containing only the matching student records.
    """
    all_students = data_manager.get_all_students()
    students_in_class = []
    for student in all_students:
        if student[3] == class_name:
            students_in_class.append(student)
    return students_in_class

def get_student_details_service(student_id):
    """
    STORY: A user wants to see the full profile of a single student.

    INPUT:
    - student_id (string): The ID of the student to find.

    PROCESS:
    1. Get all students from the data manager.
    2. Loop through the list to find the student with the matching ID.

    OUTPUT: A list representing the student's record, or None if not found.
    """
    all_students = data_manager.get_all_students()
    # Student implementation here
    return None # Placeholder

def add_student_service(first_name, last_name, class_name, section):
    """
    STORY: A new student is being admitted to the school. The admissions office
    needs to add them to the official registry.

    INPUT:
    - first_name (string): The student's first name.
    - last_name (string): The student's last name.
    - class_name (string): The class they are joining.
    - section (string): The section of the class.

    PROCESS:
    1. Generate a new, unique student ID. This is a tricky problem! A simple
       way is to get all students, find the highest existing ID, and add 1.
    2. Get the appropriate teacher_id for the given class and section (this might
       require a call to another service or the data_manager).
    3. Create the new student record as a list of strings.
    4. Call the data_manager's add_record function to append this new line
       to the 'students.txt' file.

    OUTPUT: The newly created student record, or None if it fails.
    """
    # Student implementation here
    return None # Placeholder

def remove_student_service(student_id):
    """
    STORY: A student is leaving the school. They need to be removed from the
    student registry. This is a very sensitive operation.

    INPUT:
    - student_id (string): The ID of the student to remove.

    PROCESS:
    1. Get the full list of all students.
    2. Create a new list, excluding the student with the matching ID.
    3. Call a data_manager function to completely overwrite the 'students.txt'
       file with the new, updated list. Also consider removing their marks.

    OUTPUT: True if successful, False otherwise.
    """
    # Student implementation here
    return False # Placeholder

def get_student_count_service():
    """
    STORY: The principal wants a quick headcount of all students in the school.

    INPUT: None
    PROCESS: Get all students and return the length of the list.
    OUTPUT: An integer representing the total number of students.
    """
    # Student implementation here
    return 0 # Placeholder

def get_students_by_first_name_service(name_query):
    """
    STORY: The office is searching for a student but only has their first name.

    INPUT:
    - name_query (string): The first name to search for.

    PROCESS:
    1. Get all students.
    2. Filter the list to find students whose first name (case-insensitively)
       contains the search query.

    OUTPUT: A list of matching student records.
    """
    # Student implementation here
    return [] # Placeholder

# --- Add 8 more student-related function placeholders ---

def get_students_by_section_service(class_name, section):
    """(1) Find all students in a specific section of a class."""
    return []

def get_newest_admissions_service(count):
    """(2) Get the last 'count' students that were admitted."""
    return []

def get_student_sibling_info_service(student_id):
    """(3) Find if a student has siblings in the school (by last name and address if available)."""
    return []

def update_student_class_service(student_id, new_class, new_section):
    """(4) Promote a student to a new class."""
    return False

def get_students_without_marks_service():
    """(5) Find students who do not have any marks recorded yet."""
    return []

def get_student_address_service(student_id):
    """(6) Retrieve just the address for a student (requires adding address to data)."""
    return None

def search_students_by_lastname_service(last_name_query):
    """(7) Search for students by their last name."""
    return []

def get_students_in_multiple_classes_service(class_list):
    """(8) Get a list of all students from a list of classes (e.g., all students from 6th and 7th)."""
    return []
