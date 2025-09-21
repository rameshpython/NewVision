from flask import Flask, jsonify, request
from flask_cors import CORS

# Import the service modules
from services import student_service
from services import teacher_service
from services import academic_service

# Initialize the Flask app
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# --- Static File and Status Endpoints ---

@app.route('/')
def index():
    """Serve the main index.html file."""
    return app.send_static_file('index.html')

@app.route('/api/status', methods=['GET'])
def get_status():
    """A simple endpoint to check if the API is running."""
    return jsonify({"status": "ok", "message": "Backend is running!"})

# --- Student API Endpoints ---

@app.route('/api/students', methods=['GET'])
def api_get_all_students():
    """API endpoint to get all students."""
    students = student_service.get_all_students_service()
    return jsonify(students)

@app.route('/api/students/by_class/<class_name>', methods=['GET'])
def api_get_students_by_class(class_name):
    """API endpoint to get students from a specific class."""
    students = student_service.get_students_by_class_service(class_name)
    return jsonify(students)

@app.route('/api/students/top_performers', methods=['GET'])
def api_get_top_students():
    """API endpoint to get the top performing students."""
    top_students = academic_service.get_top_students_service()
    return jsonify(top_students)

# --- Teacher API Endpoints ---

@app.route('/api/teachers', methods=['GET'])
def api_get_all_teachers():
    """API endpoint to get all teachers."""
    teachers = teacher_service.get_all_teachers_service()
    return jsonify(teachers)

# --- Academic API Endpoints ---

@app.route('/api/classes', methods=['GET'])
def api_get_all_classes():
    """API endpoint to get all classes."""
    classes = academic_service.get_all_classes_service()
    return jsonify(classes)

# --- Main Execution ---

if __name__ == '__main__':   # ✅ fixed here
    app.run(debug=True, port=5000)
