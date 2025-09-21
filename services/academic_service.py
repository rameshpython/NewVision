import data_manager


# --- Academic Service Functions ---

def get_top_students_service():
    """
    STORY: The Principal wants to honor the top 5 students in the school based on
    their average marks. This service function calculates this from raw data.

    PROCESS:
    1.  Get all students and all marks from the data_manager.
    2.  Calculate the average mark for each student.
    3.  Combine student names with their calculated averages.
    4.  Sort the list of students by their average mark in descending order.
    5.  Return the top 5 students from the sorted list.

    OUTPUT: A list of dictionaries, each representing a top student.
    """
    all_students = data_manager.get_all_students()
    all_marks = data_manager.get_all_marks()

    if not all_students or not all_marks:
        return []

    student_marks = {}
    for mark_record in all_marks:
        student_id, _, mark_value = mark_record
        mark_value = int(mark_value)

        if student_id not in student_marks:
            student_marks[student_id] = {'total': 0, 'count': 0}

        student_marks[student_id]['total'] += mark_value
        student_marks[student_id]['count'] += 1

    student_averages = []
    for student_record in all_students:
        student_id = student_record[0]
        if student_id in student_marks:
            avg_data = student_marks[student_id]
            average = avg_data['total'] / avg_data['count']

            student_info = {
                'name': f"{student_record[1]} {student_record[2]}",
                'average_mark': average
            }
            student_averages.append(student_info)

    sorted_students = sorted(student_averages, key=lambda s: s['average_mark'], reverse=True)

    return sorted_students[:5]


def get_class_performance_service(class_name):
    """
    STORY: A teacher wants to see the average performance of their class to
    understand if the class is doing well overall.

    INPUT:
    - class_name (string): The class to analyze (e.g., "10").

    PROCESS:
    1. Get all students in the specified class.
    2. Get all marks.
    3. For each student in the class, find all their marks.
    4. Calculate the average mark for the entire class.

    OUTPUT: A float representing the class average, or 0 if no marks are found.
    """
    # Student implementation here
    return 0.0  # Placeholder


def get_student_grades_service(student_id):
    """
    STORY: A student wants to see their report card with all their marks.

    INPUT:
    - student_id (string): The ID of the student.

    PROCESS:
    1. Get all marks from the data_manager.
    2. Filter the marks to find all records matching the student's ID.

    OUTPUT: A list of mark records for that student.
    """
    # Student implementation here
    return []  # Placeholder


def get_subject_average_service(subject):
    """
    STORY: The head of a department wants to know the average mark across all
    classes for a specific subject, like 'Physics'.

    INPUT:
    - subject (string): The subject to analyze.

    PROCESS:
    1. Get all marks.
    2. Filter for marks only related to the specified subject.
    3. Calculate the average of those marks.

    OUTPUT: A float representing the subject's average mark.
    """
    # Student implementation here
    return 0.0  # Placeholder


def get_all_classes_service():
    """
    STORY: The office needs a list of all classes offered.

    PROCESS: Just asks the data_manager for the classes.
    OUTPUT: A list of all class records.
    """
    return data_manager.get_all_classes()


# --- Add 15 more academic-related function placeholders ---

def get_student_rank_in_class_service(student_id, class_name):
    """(1) Find the rank of a student within their own class."""
    return 0


def add_marks_for_student_service(student_id, subject, marks):
    """(2) Add a new mark record for a student."""
    return False


def get_students_who_failed_subject_service(subject, passing_mark):
    """(3) Get a list of students who scored below a passing mark in a subject."""
    return []


def get_class_best_performer_service(class_name):
    """(4) Find the single best performing student in a specific class."""
    return None


def get_all_subjects_service():
    """(5) Get a list of all unique subjects taught at the school."""
    return []


def get_student_attendance_report_service(student_id):
    """(6) (Requires new attendance data file) Get the attendance percentage for a student."""
    return 0.0


def record_student_attendance_service(student_id, date, status):
    """(7) (Requires new attendance data file) Mark a student as 'present' or 'absent' on a specific date."""
    return False


def create_new_class_service(class_name, section, teacher_id):
    """(8) Add a new class section to the school records."""
    return False


def get_class_roster_service(class_name, section):
    """(9) Get a simple list of student names for a given class section."""
    return []


def get_school_wide_average_service():
    """(10) Calculate the average mark across all students and all subjects."""
    return 0.0


def get_student_progress_over_time_service(student_id):
    """(11) (Requires new data with dates) Track a student's marks over time."""
    return []


def get_hardest_subject_service():
    """(12) Find the subject with the lowest average mark across the school."""
    return None


def get_easiest_subject_service():
    """(13) Find the subject with the highest average mark across the school."""
    return None


def get_teacher_workload_service():
    """(14) Calculate how many students a teacher is responsible for."""
    return {}


def get_fee_status_for_student_service(student_id):
    """(15) (Requires new fees data file) Check if a student has paid their fees."""
    return "Paid"
