# Textual Devops lab

This is a dummy project to understand how to deploy a textual app in a container.

## Setup

Create a virtual environment
```bash
python -m venv venv
```

Activate the enviroment
```bash
venv\Scripts\activate
```

Install all the dependencies
```bash
pip install -r requirements.txt
```

## Usage

The app will run as a terminal user interface app.
```bash
python "app.py"
```

## Deployment on the Cloud

### Build your Docker image with the Dockerfile 
```bash
docker build -t poc .
```

### Run a new container
```bash
docker run -it -p 8000:8000 poc /bin/bash
```

### Inside the container
```bash
docker ps -a
```

### Exec will run inside your existing, running container 
```bash
docker exec -it <container_id> /bin/bash
```
