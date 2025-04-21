# Regular_expression_merged_university_management_system


# 🎓 University Management System — *Regex Based Validation Project*

A command-line Python project for managing students and teachers across colleges in a university. This system uses **regular expressions (regex)** to validate user input for accuracy and consistency. Data is stored persistently in a `.txt` file acting as a simple database.

---

## 📁 Project Structure

```
.
├── reg.py                      # Regex-based validation functions
├── university_management.py    # Main university management script
├── database.txt                # Text-based database for persistent storage
├── README.md                   # Project documentation
```

---

## ✅ Features

- 🏫 **Create Colleges**
- 👨‍🎓 **Add Students** (with validation)
- 👩‍🏫 **Add Teachers** (with validation)
- 🔍 **Search by Roll Number**
- 📋 **Display Details**
- 🔐 **Regex-based Input Validation**:
  - ✔️ Name (alphabets, space, and dot)
  - 📅 Date of Birth (`dd-mm-yyyy` → `dd Month yyyy`)
  - 📧 Email ID (Gmail only)
  - 📱 Mobile Number (`XXX-XXX-XXXX` format → digits only)
- 💾 Persistent storage in a `.txt` file using Python dictionaries

---

## 🔍 Regex Validation (from `reg.py`)

| Field        | Pattern Used                            | Description                              |
|--------------|------------------------------------------|------------------------------------------|
| Name         | `^[A-Za-z .]+$`                          | Allows only letters, spaces, and dots    |
| Date of Birth| `\d{2}-\d{2}-\d{4}`                      | Must be in `dd-mm-yyyy` format           |
| Email ID     | `[a-z0-9]+@gmail.com\Z`                 | Only Gmail addresses, lowercase & digits |
| Mobile No.   | `\d{3}-\d{3}-\d{4}`                      | Hyphenated format, converted to digits   |

---

## 🚀 How to Run

```bash
python university_management.py
```

---

## 📘 Sample Interaction

```text
Welcome to University Management System:

1. Create College
2. Add Student
3. Add Teacher
4. Display Students
5. Display Teachers
6. Search a Student / Teacher
7. Exit
```

---

## 🔧 Future Enhancements

- Convert `.txt` to `.json` or database integration (SQLite/MySQL)
- GUI interface with Tkinter or web dashboard
- Authentication & user roles
- PDF/CSV report generation

---

## ✨ Acknowledgements

Developed as a regex-focused Python mini-project for learning and practice.  
Developed by **Muthavarapu Venkata Akhil**
