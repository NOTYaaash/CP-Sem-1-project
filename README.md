# 📝 Flask To-Do List Application

This is a simple, full-stack To-Do List web application. The backend is built with Python, Flask, and SQLAlchemy, providing a RESTful API. The frontend is a single-page application built with vanilla HTML, CSS, and JavaScript that consumes the backend API.

---

## 🚀 Features

* **Add Tasks:** Easily add new tasks to your list.
* **View Tasks:** All tasks are loaded and displayed on page load.
* **Delete Tasks:** Mark tasks as "Done," which removes them from the database.
* **Database Persistence:** Tasks are stored in a MySQL database.
* **RESTful API:** Clean separation between the Flask backend and the JavaScript frontend.

---

## 🛠️ Tech Stack

* **Backend:**
    * **Python:** The core programming language.
    * **Flask:** A micro web framework for building the server and API.
    * **Flask-SQLAlchemy:** An ORM (Object-Relational Mapper) for database operations.
    * **PyMySQL:** A MySQL driver for Python.
* **Database:**
    * **MySQL:** A relational database for storing the tasks.
* **Frontend:**
    * **HTML:** For the page structure.
    * **CSS:** For styling the user interface.
    * **JavaScript (Vanilla):** For DOM manipulation and making API calls (`fetch`).

---

## ⚙️ Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

* **Python 3.x**
* **pip** (Python package installer)
* **A running MySQL server**

### 2. Clone & Setup Backend

1.  **Clone the repository** (or save the files to a new project folder).

2.  **Create a `templates` folder:** Flask looks for HTML files in a folder named `templates` by default.
    ```bash
    mkdir templates
    ```

3.  **Move `index.html`:**
    ```bash
    mv index.html templates/index.html
    ```
    Your project structure should look like this:
    ```
    /
    ├── app.py
    └── templates/
        └── index.html
    ```

4.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

5.  **Install Python dependencies:**
    ```bash
    pip install Flask Flask-SQLAlchemy PyMySQL
    ```

### 3. Database Configuration

1.  **Log in to your MySQL server** and create a new database for the project:
    ```sql
    CREATE DATABASE todo_db;
    ```

2.  **Update the Connection String:** Open `app.py` and find this line:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yash123@localhost/todo_db?unix_socket=/tmp/mysql.sock'
    ```
    * Modify `root` and `yash123` to match **your MySQL username and password**.
    * The `unix_socket` part may be specific to macOS/Linux. If you are on **Windows** or your setup is different, a more standard connection string might work better.
    * **Standard (Windows/most setups) example:**
        ```python
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/todo_db'
        ```

### 4. Run the Application

1.  **Run the Flask app:**
    ```bash
    python app.py
    ```
    When you run this for the first time, the line `db.create_all()` will automatically create the `task` table in your `todo_db` database.

2.  **Open your browser:**
    Navigate to **`http://127.0.0.1:5000/`** to use your To-Do list!

---

## 📖 How to Use

* **View Tasks:** Just load the page, and all tasks will be fetched from the database.
* **Add a Task:** Type a task into the input box and click "Add Task" or press Enter.
* **Complete a Task:** Click the "Done" button next to any task to remove it from the list.

---

## 🌐 API Endpoints

The Flask backend provides the following API endpoints:

* **`GET /`**
    * **Description:** Serves the main `index.html` web page.
* **`GET /api/tasks`**
    * **Description:** Gets a list of all tasks in the database.
    * **Response:** `200 OK`
        ```json
        [
            {"id": 1, "content": "Buy groceries"},
            {"id": 2, "content": "Finish project"}
        ]
        ```
* **`POST /api/add`**
    * **Description:** Adds a new task to the database.
    * **Request Body:**
        ```json
        {"content": "New task content"}
        ```
    * **Response:** `201 Created`
        ```json
        {"id": 3, "content": "New task content"}
        ```
* **`DELETE /api/delete/<int:task_id>`**
    * **Description:** Deletes a task by its ID.
    * **Response:** `200 OK`
        ```json
        {"message": "Task deleted successfully"}
        ```
