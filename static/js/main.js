document.addEventListener('DOMContentLoaded', () => {

    // --- Element References ---
    const loginView = document.getElementById('login-view');
    const roleSelect = document.getElementById('role-select');
    const loginBtn = document.getElementById('login-btn');
    const navbarContainer = document.getElementById('navbar-container');

    const principalDashboard = document.getElementById('principal-dashboard');
    const teacherDashboard = document.getElementById('teacher-dashboard');
    const studentDashboard = document.getElementById('student-dashboard');

    const API_URL = 'http://127.0.0.1:5000/api';

    // --- State ---
    let currentRole = null;

    // --- Core Functions ---

    function hideAllViews() {
        loginView.classList.add('d-none');
        principalDashboard.classList.add('d-none');
        teacherDashboard.classList.add('d-none');
        studentDashboard.classList.add('d-none');
        navbarContainer.innerHTML = '';
    }

    function handleLogin() {
        const selectedRole = roleSelect.value;
        if (!selectedRole || selectedRole === 'Choose...') {
            alert('Please select a role to continue.');
            return;
        }
        currentRole = selectedRole;
        showDashboard(currentRole);
    }

    function showDashboard(role) {
        hideAllViews();
        loadNavbar(role);
        switch (role) {
            case 'principal':
                principalDashboard.classList.remove('d-none');
                loadPrincipalDashboard();
                break;
            case 'teacher':
                teacherDashboard.classList.remove('d-none');
                loadTeacherDashboard();
                break;
            case 'student':
                studentDashboard.classList.remove('d-none');
                loadStudentDashboard();
                break;
        }
    }

    function loadNavbar(role) {
        navbarContainer.innerHTML = `
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">${role.charAt(0).toUpperCase() + role.slice(1)} Portal</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="#" id="home-btn"><i class="bi bi-house-door-fill"></i> Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#" id="logout-btn"><i class="bi bi-box-arrow-right"></i> Logout</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        `;
        document.getElementById('logout-btn').addEventListener('click', () => location.reload());
        document.getElementById('home-btn').addEventListener('click', () => showDashboard(currentRole));
    }

    // --- Dashboard Loaders ---
    function loadPrincipalDashboard() {
        principalDashboard.innerHTML = `
            <div id="principal-view-content" class="content-view" style="display: none;"></div>
            <h3 class="mb-4">Student Management</h3>
            <div class="dashboard-grid">
                <div class="dashboard-item" data-action="get_all_students"><i class="bi bi-people-fill"></i>View All Students</div>
                <div class="dashboard-item" data-action="get_students_by_class"><i class="bi bi-person-video3"></i>Find by Class</div>
                <div class="dashboard-item" data-action="get_student_details"><i class="bi bi-person-lines-fill"></i>Student Details</div>
                <div class="dashboard-item" data-action="add_new_student"><i class="bi bi-person-plus-fill"></i>Admit Student</div>
                <div class="dashboard-item" data-action="remove_student"><i class="bi bi-person-x-fill"></i>Remove Student</div>
                <div class="dashboard-item" data-action="get_student_count"><i class="bi bi-bar-chart-fill"></i>Total Student Count</div>
            </div>
            <h3 class="mt-5 mb-4">Teacher Management</h3>
            <div class="dashboard-grid">
                <div class="dashboard-item" data-action="get_all_teachers"><i class="bi bi-person-workspace"></i>View All Teachers</div>
                <div class="dashboard-item" data-action="assign_teacher_to_class"><i class="bi bi-link-45deg"></i>Assign Teacher</div>
                <div class="dashboard-item" data-action="get_unassigned_teachers"><i class="bi bi-person-dash-fill"></i>Unassigned Teachers</div>
            </div>
            <h3 class="mt-5 mb-4">Academic & Performance</h3>
            <div class="dashboard-grid">
                <div class="dashboard-item" data-action="get_all_classes"><i class="bi bi-book-half"></i>View All Classes</div>
                <div class="dashboard-item" data-action="view_top_students"><i class="bi bi-trophy-fill"></i>Top Performers</div>
                <div class="dashboard-item" data-action="get_subject_average"><i class="bi bi-calculator-fill"></i>Subject Averages</div>
                <div class="dashboard-item" data-action="get_students_failing"><i class="bi bi-emoji-frown-fill"></i>Students At-Risk</div>
            </div>
        `;
    }

    function loadTeacherDashboard() {
        teacherDashboard.innerHTML = `
            <div id="teacher-view-content" class="content-view" style="display: none;"></div>
            <h3 class="mb-4">My Class Management</h3>
            <div class="dashboard-grid">
                <div class="dashboard-item" data-action="get_my_classes"><i class="bi bi-collection-fill"></i>My Classes</div>
                <div class="dashboard-item" data-action="get_students_in_my_class"><i class="bi bi-people"></i>My Students</div>
                <div class="dashboard-item" data-action="take_attendance"><i class="bi bi-check-circle-fill"></i>Take Attendance</div>
                <div class="dashboard-item" data-action="enter_grades"><i class="bi bi-pencil-square"></i>Enter Grades</div>
                <div class="dashboard-item" data-action="view_class_performance"><i class="bi bi-graph-up"></i>Class Performance</div>
                <div class="dashboard-item" data-action="view_announcements_teacher"><i class="bi bi-megaphone-fill"></i>Announcements</div>
            </div>
        `;
    }

    function loadStudentDashboard() {
        studentDashboard.innerHTML = `
            <div id="student-view-content" class="content-view" style="display: none;"></div>
            <h3 class="mb-4">My Portal</h3>
            <div class="dashboard-grid">
                <div class="dashboard-item" data-action="view_my_profile"><i class="bi bi-person-circle"></i>My Profile</div>
                <div class="dashboard-item" data-action="view_my_grades"><i class="bi bi-card-checklist"></i>My Report Card</div>
                <div class="dashboard-item" data-action="view_my_rank_in_class"><i class="bi bi-award-fill"></i>My Class Rank</div>
                <div class="dashboard-item" data-action="view_my_attendance"><i class="bi bi-calendar-check-fill"></i>My Attendance</div>
                <div class="dashboard-item" data-action="view_class_timetable"><i class="bi bi-table"></i>Class Timetable</div>
                <div class="dashboard-item" data-action="view_announcements_student"><i class="bi bi-info-circle-fill"></i>Announcements</div>
            </div>
        `;
    }

    // --- Event Handling ---
    function handleDashboardClick(event) {
        const target = event.target.closest('.dashboard-item');
        if (!target) return;

        const action = target.dataset.action;
        const contentView = event.currentTarget.querySelector('.content-view');
        const allGrids = event.currentTarget.querySelectorAll('.dashboard-grid, h3');

        // Hide dashboard items and show content view
        allGrids.forEach(el => el.style.display = 'none');
        contentView.style.display = 'block';
        contentView.innerHTML = `<div class="text-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>`;

        switch(action) {
            case 'get_all_students':
                fetchAllStudents(contentView);
                break;
            case 'get_all_teachers':
                fetchAllTeachers(contentView);
                break;
            case 'get_all_classes':
                fetchAllClasses(contentView);
                break;
            case 'get_students_by_class':
                const className = prompt("Please enter the class to search for (e.g., 10):");
                if (className) fetchStudentsByClass(className, contentView);
                else showDashboard(currentRole);
                break;
            case 'view_top_students':
                fetchTopStudents(contentView);
                break;
            default:
                contentView.innerHTML = `<div class="alert alert-warning">Feature "${action}" is not implemented yet.</div>`;
        }
    }

    // --- API Fetch Functions ---
    async function fetchAllStudents(contentView) {
        try {
            const response = await fetch(`${API_URL}/students`);
            const data = await response.json();
            let html = `<h4><i class="bi bi-people-fill"></i> All Students</h4><table class="table table-hover"><thead><tr><th>ID</th><th>Name</th><th>Class</th><th>Section</th></tr></thead><tbody>`;
            data.forEach(s => {
                html += `<tr><td>${s[0]}</td><td>${s[1]} ${s[2]}</td><td>${s[3]}</td><td>${s[4]}</td></tr>`;
            });
            html += '</tbody></table>';
            contentView.innerHTML = html;
        } catch (e) {
            contentView.innerHTML = '<div class="alert alert-danger">Error fetching student data.</div>';
        }
    }

    async function fetchAllTeachers(contentView) {
        try {
            const response = await fetch(`${API_URL}/teachers`);
            const data = await response.json();
            let html = `<h4><i class="bi bi-person-workspace"></i> All Teachers</h4><table class="table table-hover"><thead><tr><th>ID</th><th>Name</th><th>Subject</th></tr></thead><tbody>`;
            data.forEach(t => {
                html += `<tr><td>${t[0]}</td><td>${t[1]} ${t[2]}</td><td>${t[3]}</td></tr>`;
            });
            html += '</tbody></table>';
            contentView.innerHTML = html;
        } catch (e) {
            contentView.innerHTML = '<div class="alert alert-danger">Error fetching teacher data.</div>';
        }
    }

    async function fetchAllClasses(contentView) {
        try {
            const response = await fetch(`${API_URL}/classes`);
            const data = await response.json();
            let html = `<h4><i class="bi bi-book-half"></i> All Classes</h4><table class="table table-hover"><thead><tr><th>Class</th><th>Section</th><th>Teacher ID</th></tr></thead><tbody>`;
            data.forEach(c => {
                html += `<tr><td>${c[0]}</td><td>${c[1]}</td><td>${c[2]}</td></tr>`;
            });
            html += '</tbody></table>';
            contentView.innerHTML = html;
        } catch (e) {
            contentView.innerHTML = '<div class="alert alert-danger">Error fetching class data.</div>';
        }
    }

    async function fetchStudentsByClass(className, contentView) {
        try {
            const response = await fetch(`${API_URL}/students/by_class/${className}`);
            const data = await response.json();
            let html = `<h4><i class="bi bi-person-video3"></i> Students in Class ${className}</h4>`;
            if (data.length === 0) {
                html += `<div class="alert alert-info">No students found for class ${className}.</div>`;
            } else {
                html += `<table class="table table-hover"><thead><tr><th>ID</th><th>Name</th><th>Section</th></tr></thead><tbody>`;
                data.forEach(s => {
                    html += `<tr><td>${s[0]}</td><td>${s[1]} ${s[2]}</td><td>${s[4]}</td></tr>`;
                });
                html += '</tbody></table>';
            }
            contentView.innerHTML = html;
        } catch (e) {
            contentView.innerHTML = `<div class="alert alert-danger">Error fetching data for class ${className}.</div>`;
        }
    }

    async function fetchTopStudents(contentView) {
        try {
            const response = await fetch(`${API_URL}/students/top_performers`);
            const data = await response.json();
            let html = `<h4><i class="bi bi-trophy-fill"></i> Top 5 Performing Students</h4>`;
            if (data.length === 0) {
                html += `<div class="alert alert-info">No student mark data available.</div>`;
            } else {
                html += `<table class="table table-hover"><thead><tr><th>Rank</th><th>Student Name</th><th>Average Mark</th></tr></thead><tbody>`;
                data.forEach((s, i) => {
                    html += `<tr><td><span class="badge bg-primary">${i + 1}</span></td><td>${s.name}</td><td>${s.average_mark.toFixed(2)}</td></tr>`;
                });
                html += '</tbody></table>';
            }
            contentView.innerHTML = html;
        } catch (e) {
            contentView.innerHTML = '<div class="alert alert-danger">Error fetching top student data.</div>';
        }
    }

    // --- Initial Setup ---
    async function init() {
        try {
            const response = await fetch(${API_URL}/status);
            if (!response.ok) {
                alert('Error: Backend server is not responding. Please start the Python server by running "python app.py".');
            }
        } catch (error) {
            alert('CRITICAL: Could not connect to the backend server. Please ensure it is running and there are no network issues.');
        }

        loginBtn.addEventListener('click', handleLogin);
        principalDashboard.addEventListener('click', handleDashboardClick);
        teacherDashboard.addEventListener('click', handleDashboardClick);
        studentDashboard.addEventListener('click', handleDashboardClick);
    }

    init();
});
