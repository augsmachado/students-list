# Students List - FastApi

## Overview

This project is a simple RESTful API built with FastAPI for managing student data. It uses an in-memory dictionary to store student information, including name, age, and year. The project demonstrates basic CRUD operations with FastAPI and serves as a starting point for building more complex APIs.

## 🚀 Features

The API provides the following endpoints:

-   **GET/**: Returns a welcome message "First Data".
-   **GET/status**: Returns the API name and version.
-   **GET/get-student/{student_id}**: Retrieves a student by their ID using a path parameter. Returns a "Student not found" message if the ID doesn't exist.
-   **GET/get-by-name**: Retrieves a student by their name using a query parameter. Returns a "Student not found" message if the name doesn't exist.
-   **POST/create-student/{student_id}**: Creates a new student with the given ID. Returns a "Student already exists" message if the ID is already in use. Accepts a JSON payload with student data.
-   **PUT/update-student/{student_id}**: Updates an existing student's information. Accepts a JSON payload with optional fields for name, age, and year. Returns a "Student not found" message if the ID doesn't exist.
-   **DELETE/delete-student/{student_id}**: Deletes a student by their ID. Returns a "Student deleted successfully" message upon successful deletion or a "Student not found" message if the ID doesn't exist.

The API uses Pydantic models for data validation and serialization. Student model defines the required fields for creating a student, while UpdateStudent allows optional fields for updating.

## 🛠 Tech Stack

-   Python 3.11
-   FastAPI

## 📦 Prerequisites

-   Python 3.11+
-   pip

## 🔧 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/students-list.git
cd students-list
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🚦 Running the Application

```bash
uvicorn main:app --reload
```

### 🔍 Testing

```bash
pytest
```

### 🤝 Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. Use the framework below:

-   Fork the repository
-   Create your feature branch
-   Commit your changes
-   Push to the branch
-   Create a Pull Request

### 📄 License

This project is licensed under the Apache License 2.0.
See the LICENSE file for details.
