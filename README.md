
# Todo App with Django

This is a simple Todo application built using Django, where users can add, view, and track their to-do tasks. It allows users to manage their daily tasks, marking them as completed or not, with the option to add detailed descriptions.

## Features
- **Add Todos**: Users can add new tasks with titles and descriptions.
- **Track Task Completion**: Mark tasks as completed or pending.
- **View Todos**: View a list of all tasks with their status (completed or pending).
- **Database Integration**: Uses Django's ORM to store todo tasks in a database.

## Technologies Used
- **Django**: Web framework for building the application.
- **Python**: The programming language used to write the application.
- **SQLite** (default): The default database used by Django for this application.

## Installation

### 1. Clone the Repository
Clone this project to your local machine using the following command:

```bash
git clone https://github.com/your-username/todo-app.git

### 2. Install Dependencies

Navigate to the project folder and create a virtual environment:

bash

Copy

`cd todo-app
python -m venv venv` 

Activate the virtual environment:

-   On Windows:
    
    bash
    
    Copy
    
    `venv\Scripts\activate` 
    
-   On macOS/Linux:
    
    bash
    
    Copy
    
    `source venv/bin/activate` 
    

Then, install the required dependencies:

bash

Copy

`pip install -r requirements.txt` 

### 3. Set Up the Database

After installing the dependencies, you need to set up the database by running the following commands:

bash

Copy

`python manage.py makemigrations
python manage.py migrate` 

This will apply the migrations and set up the necessary database tables.

### 4. Create a Superuser (Optional for Admin Access)

If you want to use the Django admin interface to manage the Todos, create a superuser by running the following command:

bash

Copy

`python manage.py createsuperuser` 

Follow the prompts to create a superuser account.

### 5. Run the Development Server

To start the development server and view the application in your browser, run:

bash

Copy

`python manage.py runserver` 

You can now access the app at `http://127.0.0.1:8000/` in your browser.

If you want to access the Django admin interface, go to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created earlier.

## Project Structure

Here’s a brief overview of the project structure:

bash

Copy

`todo-app/
│
├── manage.py # The main entry point for managing the Django project ├── requirements.txt # List of required Python packages ├── myapp/ # The Django app containing all the logic │   ├── migrations/ # Database migration files │   ├── __init__.py
│   ├── admin.py # Admin configuration │   ├── apps.py
│   ├── models.py # The database models (TodoItem) │   ├── views.py # View functions (home, todos) │   ├── templates/ # Template files for HTML views │   │   ├── home.html
│   │   └── todos.html
│   └── urls.py # URL routing for the app ├── todoapp/ # The main project folder │   ├── settings.py # Project settings │   ├── urls.py # Main URL routing for the project │   ├── wsgi.py
│   └── asgi.py
└── venv/ # Virtual environment folder (do not commit this folder)` 

### Files Explained:

-   **`models.py`**: Contains the `TodoItem` model, which defines the structure of the Todo item (title, description, completed status, and timestamps).
    
-   **`views.py`**: Contains view functions to handle requests. For example, `home` renders the home page, and `todos` fetches all Todo items from the database and displays them.
    
-   **`templates/`**: Contains HTML templates to render the views. `home.html` is the home page, and `todos.html` displays the list of Todo items.
    
-   **`urls.py`**: Defines URL routing for the app. It maps URLs to specific views.
    

## Usage

Once the server is running, you can visit the following URLs:

-   `/` — Home page.
    
-   `/todos/` — Displays the list of all todo tasks.
    
-   `/admin/` — Django Admin interface for managing todos (only accessible to superusers).
    

### Adding a Todo:

-   Go to the Django admin panel at `/admin/`.
    
-   Log in with the superuser credentials.
    
-   Add a new `TodoItem` by filling in the fields: `title`, `description`, and `completed`.
    

### Viewing Todos:

-   Go to `/todos/` to see a list of all Todo items stored in the database, with their title, completion status, and description.
    

## Customization

You can easily modify this project to:

-   Add user authentication (login and registration).
    
-   Customize the appearance using CSS or JavaScript.
    
-   Add more features like deadlines, priority levels, or categorization for tasks.
    

## Contributing

Feel free to fork this repository and contribute. If you make any improvements, bug fixes, or new features, submit a pull request, and I’d be happy to review it.
