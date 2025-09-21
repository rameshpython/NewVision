
# --- Data Manager Module ---
# This file is the gateway to our "database" (the text files).
# Its only job is to perform the basic Create, Read, Update, Delete (CRUD)
# operations on the data files. It contains NO business logic.
# For example, it will give you all students, but it won't know how to
# find students in a specific class. That's the job of the 'services' layer.

import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def _get_file_path(filename):
    """A helper function to get the full path to a data file."""
    return os.path.join(DATA_DIR, filename)

def _read_file(filename):
    """A generic function to read all records from any data file."""
    records = []
    try:
        with open(_get_file_path(filename), 'r') as f:
            for line in f:
                if line.strip():
                    records.append(line.strip().split(','))
    except FileNotFoundError:
        print(f"Data file '{filename}' not found.")
        return []
    return records

def get_all_students():
    """Reads all student records from students.txt."""
    return _read_file('students.txt')

def get_all_teachers():
    """Reads all teacher records from teachers.txt."""
    return _read_file('teachers.txt')

def get_all_classes():
    """Reads all class records from classes.txt."""
    return _read_file('classes.txt')

def get_all_marks():
    """Reads all mark records from marks.txt."""
    return _read_file('marks.txt')

# --- Functions for writing data will be added below ---

def write_all_records(filename, records):
    """
    STORY: When we remove or update a record, the easiest way to save the
    change is to rewrite the entire file with the new, updated data.

    INPUT:
    - filename (string): The name of the file to write to (e.g., 'students.txt').
    - records (list of lists): The complete data that should be in the file.

    PROCESS:
    1. Opens the specified file in 'write' mode, which erases it completely.
    2. Loops through the list of records.
    3. For each record (which is a list of strings), it joins them back
       together with commas and writes it as a new line in the file.

    OUTPUT: True if successful, False otherwise.
    """
    try:
        with open(_get_file_path(filename), 'w') as f:
            for record in records:
                line = ",".join(record)
                f.write(line + '\n')
        return True
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        return False

def add_record(filename, record):
    """
    STORY: When a new student or teacher is added, we just need to append
    their record as a new line at the end of the file.

    INPUT:
    - filename (string): The name of the file to add to.
    - record (list of strings): The record to add.

    PROCESS:
    1. Opens the file in 'append' mode ('a').
    2. Joins the record list with commas.
    3. Writes the resulting string as a new line at the end of the file.

    OUTPUT: True if successful, False otherwise.
    """
    try:
        with open(_get_file_path(filename), 'a') as f:
            line = ",".join(record)
            f.write(line + '\n')
        return True
    except IOError as e:
        print(f"Error appending to file {filename}: {e}")
        return False
