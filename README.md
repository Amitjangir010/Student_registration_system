# 🎓 Student Management System

A modern, user-friendly student information management system built with Flask, featuring secure authentication and comprehensive student data management capabilities.

## 📸 System Workflow

<p align="center">
  <img src="images/welcome.jpeg" width="250" alt="Login Interface" style="margin-right: 10px;"/>
  <img src="images/login.jpeg" width="250" alt="Login Interface" style="margin-right: 10px;"/>
  <img src="images/dashboard.jpeg" width="350" alt="Dashboard Interface" style="margin-right: 10px;"/>
  <img src="images/update.jpeg" width="250" alt="Update Interface"/>
</p>
<p align="center">
  <em>Welcome → Login → Dashboard → Update Student Information</em>
</p>

## 🌟 Features

- **Secure Authentication System**
  - Custom database connection
  - User-friendly login interface
  - Session management

- **Student Management**
  - Add new students
  - Update existing records
  - Delete student entries
  - Search functionality
  - Export data to CSV

- **Modern UI/UX**
  - Clean, intuitive interface
  - Responsive design
  - Interactive feedback
  - Professional styling

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL/PostgreSQL
- **Security**: Session-based authentication

## 💻 Quick Start Guide

<p align="center">

### Login Page

<img src="images/login.jpeg" width="500" alt="Login Interface">

*Secure login with database credentials*

### Dashboard
<img src="images/dashboard.jpeg" width="600" alt="Dashboard Interface">

*Comprehensive student management dashboard*

### Update Form
<img src="images/update.jpeg" width="500" alt="Update Interface">

*Student information update form*

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Amitjangir010/Student_registration_system.git
cd student-management-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Access the system:
```
URL: http://localhost:81
Default Credentials:
- Hostname: root
- Username: abcd
- Password: 1234
```

## 💻 Usage Guide

### Login
1. Enter database credentials
2. Click "Connect" to access dashboard

### Managing Students
- **Add**: Fill the form with student details
- **Search**: Use the search bar for quick lookup
- **Update**: Click edit icon to modify records
- **Delete**: Remove entries with delete button
- **Export**: Download data in CSV format

## 📁 Project Structure

```
student_management/
├── main.py              # Main application file
├── templates/           # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── update_student.html
├── static/             # Static assets
│   ├── styles.css
│   └── images/
│       ├── user.jpeg
│       ├── password.jpeg
│       └── th.jpg
└── requirements.txt    # Dependencies
```

## 🔒 Security Features

- Session-based authentication
- Secure password handling
- Protected routes
- Input validation
- SQL injection prevention

## 🎯 Future Improvements

- [ ] Add user roles and permissions
- [ ] Implement profile pictures
- [ ] Add bulk import/export
- [ ] Email notifications
- [ ] Advanced search filters

---
Made with ❤️ by Amit Jangir
 
