#  Smart File Organizer – Python Automation Tool

Smart File Organizer is a Python-based automation tool that helps you keep your folders clean and organized by automatically sorting files into categorized directories based on their file types.

This project focuses on **file system automation**, **clean project structure**, and **real-world Python practices**.

--- 

##  Features

- Automatically organizes files by type (Images, Documents, Videos, etc.)
- Creates folders dynamically if they don’t exist
- Handles unknown file types by placing them in a default folder
- Clean and modular project structure
- Logging system to track all file operations
- Cross-platform (Windows / Linux / macOS)

---

##  Project Concept

The tool scans a target directory and:
1. Detects files inside the folder
2. Identifies each file’s extension
3. Matches the extension to a predefined category
4. Moves the file to the appropriate folder
5. Logs every operation for future reference

This automates a repetitive manual task that users typically perform daily.

---

##  Project Structure
file_organizer/  
│  
├── config.py # File type configuration  
├── logger.py # Logging setup  
├── organizer.py # Main automation script  
├── organizer.log # Generated log file  

---

##  Technologies Used

- Python 3
- os
- shutil
- logging

---
## Future Enhancements

Real-time Folder Monitoring (Watch Folder)

A future enhancement for this project is real-time folder monitoring, which will allow the application to continuously watch a specified directory and automatically organize files the moment they are added. Instead of running the script manually, the tool will operate in the background using an event-driven approach, detecting file system changes and applying the same organization logic instantly. This feature will improve usability and efficiency, making the automation process fully continuous.
