# Task Management API

This repository contains the source code for a Task Management API, built using Flask and PostgreSQL.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed on your machine:

- Python (version 3.11.0)
- PostgreSQL (version 11 or higher) | Supported Versions: Current (15) / 14 / 13 / 12 / 11


## Getting Started

To get started with the Task Management API, follow these steps:

1. Clone the repository to your local machine. 
2. Using (HTTPS: https://github.com/RawadKadi/task-management-api.git) 
3. Or (SSH: git@github.com:RawadKadi/task-management-api.git)
4. Navigate to the project directory.
5. Install the project dependencies using pip.
6. Set up the PostgreSQL database by creating a new database named `task_manager` and updating the database connection URI in the `app.py` file with your PostgreSQL credentials.
7. Apply the database migrations.
8. Launch the application.

The Task Management API will be accessible at http://localhost:5000.

## API Endpoints

The Task Management API provides the following endpoints:

- GET /tasks: Retrieve a list of all tasks.
- GET /tasks/{task_id}: Retrieve details of a specific task.
- POST /tasks: Create a new task.
- PUT /tasks/{task_id}: Update the details of a specific task.
- DELETE /tasks/{task_id}: Delete a specific task.

For detailed information on the request and response formats for each endpoint, please refer to the API documentation.

## Swagger Documentation

The Task Management API documentation is provided using Swagger UI. To access the Swagger documentation, follow these steps:

1. Launch the application.
2. Open your web browser and go to http://localhost:5000/swagger
3. You can also access the json file here http://localhost:5000/swagger.json

The Swagger UI interface will allow you to explore and interact with the API endpoints in a user-friendly way.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Flask: Lightweight web framework for Python.
- PostgreSQL: Powerful open-source relational database management system.