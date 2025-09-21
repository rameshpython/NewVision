import data_manager

# --- Teacher Service Functions ---

def get_all_teachers_service():
    """
    STORY: The principal needs a directory of all teachers. This service function
    gets the raw teacher data from the data_manager.

    INPUT: None
    OUTPUT: A list of lists, containing all teacher records.
    """
    return data_manager.get_all_teachers()

def get_teacher_details_service(teacher_id):
    """
    STORY: A user wants to see the details of a specific teacher.

    INPUT:
    - teacher_id (string): The ID of the teacher to find.

    PROCESS:
    1. Get all teachers from the data manager.
    2. Find the teacher with the matching ID.

    OUTPUT: A list representing the teacher's record, or None if not found.
    """
    # Student implementation here
    return None # Placeholder

def get_teachers_by_subject_service(subject):
    """
    STORY: The academic coordinator wants to find all teachers who teach a
    specific subject, like 'Mathematics'.

    INPUT:
    - subject (string): The subject to search for.

    PROCESS:
    1. Get all teachers.
    2. Filter the list to find teachers whose subject matches.

    OUTPUT: A list of matching teacher records.
    """
    # Student implementation here
    return [] # Placeholder

def add_teacher_service(first_name, last_name, subject):
    """
    STORY: The school has hired a new teacher. They need to be added to the
    faculty records.

    INPUT:
    - first_name (string): Teacher's first name.
    - last_name (string): Teacher's last name.
    - subject (string): The primary subject they teach.

    PROCESS:
    1. Generate a new, unique teacher ID.
    2. Create the new teacher record.
    3. Ask the data_manager to append the record to the 'teachers.txt' file.

    OUTPUT: The newly created teacher record.
    """
    # Student implementation here
    return None # Placeholder

def remove_teacher_service(teacher_id):
    """
    STORY: A teacher is leaving the school. Their record needs to be removed.
    This also has implications: what happens to the class they were assigned to?
    For now, we'll just remove the teacher.

    INPUT:
    - teacher_id (string): The ID of the teacher to remove.

    PROCESS:
    1. Get all teachers.
    2. Create a new list without the specified teacher.
    3. Ask the data_manager to overwrite the 'teachers.txt' file.

    OUTPUT: True if successful, False otherwise.
    """
    # Student implementation here
    return False # Placeholder

def get_teacher_class_assignments_service(teacher_id):
    """
    STORY: A teacher wants to see a list of all classes they are assigned to teach.

    INPUT:
    - teacher_id (string): The ID of the teacher.

    PROCESS:
    1. Get all class records from the data_manager.
    2. Filter the list to find classes where the teacher_id matches.

    OUTPUT: A list of class records assigned to that teacher.
    """
    # Student implementation here
    return [] # Placeholder

# --- Add 9 more teacher-related function placeholders ---

def get_unassigned_teachers_service():
    """(1) Find teachers who are not currently assigned to any class."""
    return []

def update_teacher_subject_service(teacher_id, new_subject):
    """(2) Change the primary subject for a teacher."""
    return False

def get_teacher_count_by_subject_service():
    """(3) Get a count of how many teachers teach each subject."""
    return {} # e.g., {'Mathematics': 5, 'Physics': 3}

def search_teachers_by_name_service(name_query):
    """(4) Search for teachers by their first or last name."""
    return []

def assign_teacher_to_class_service(teacher_id, class_name, section):
    """(5) Assign a teacher to a specific class section."""
    return False

def unassign_teacher_from_class_service(class_name, section):
    """(6) Unassign a teacher, leaving the class without an assigned teacher."""
    return False

def get_newest_hires_service(count):
    """(7) Get the last 'count' teachers that were hired."""
    return []

def get_teachers_teaching_multiple_subjects_service():
    """(8) In a more advanced model, find teachers who teach more than one subject."""
    return []

def get_teacher_of_student_service(student_id):
    """(9) Find the primary teacher for a given student."""
    return None