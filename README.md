# FastAPI Demo App - Task Manager API

A simple REST API built with FastAPI to demonstrate CI/CD capabilities with CloudBees Unify platform.

## Features

- RESTful API for task management (CRUD operations)
- Automatic API documentation with Swagger UI
- Comprehensive test suite with pytest
- Docker containerization
- Jenkins pipeline for CI/CD
- Code linting with flake8
- Test coverage reporting

## API Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint
- `GET /tasks` - Get all tasks
- `GET /tasks/{id}` - Get a specific task by ID
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional)
- Git

### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd fastapi-demo-app
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

5. Access the API:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### Running Tests

```bash
pytest tests/ -v --cov=app
```

### Running with Docker

1. Build the Docker image:
```bash
docker build -t fastapi-demo-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 fastapi-demo-app
```

## CI/CD with CloudBees

This project includes a `Jenkinsfile` that defines a complete CI/CD pipeline with the following stages:

1. **Checkout** - Clone the repository
2. **Setup Python Environment** - Create virtual environment and install dependencies
3. **Lint** - Run code quality checks with flake8
4. **Test** - Run pytest with coverage reporting
5. **Build Docker Image** - Build and tag Docker container
6. **Security Scan** - Check dependencies for security vulnerabilities
7. **Archive Artifacts** - Save build artifacts

### Setting up in CloudBees

1. Create a new repository on GitHub and push this code
2. In CloudBees Unify, create a new pipeline project
3. Connect it to your GitHub repository
4. The Jenkinsfile will be automatically detected
5. Run the pipeline to see the CI/CD process in action

## Example API Usage

### Create a task
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}'
```

### Get all tasks
```bash
curl http://localhost:8000/tasks
```

### Update a task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": true}'
```

### Delete a task
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## Project Structure

```
fastapi-demo-app/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Test suite
├── Dockerfile           # Docker configuration
├── Jenkinsfile          # CloudBees CI/CD pipeline
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI
- **Pydantic** - Data validation using Python type annotations
- **Pytest** - Testing framework
- **Docker** - Containerization
- **Jenkins** - CI/CD automation

## License

MIT License - Feel free to use this project for learning and demonstration purposes.
