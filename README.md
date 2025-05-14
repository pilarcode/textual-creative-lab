# Textual Devops lab

This is a dummy project to understand how to deploy a textual app in a container.

## Usage

* Option 1: The app will run as a web app at http://localhost:8000
```bash
python "app_entrypoint.py"
```

* Option 2: The app will run as a terminal user interface app.
```bash
python "app.py"
```

## Deployment on the Cloud

### 1. Build your Docker image
Build the Docker image using the provided Dockerfile. This command creates a new image named `poc`:
```bash
docker build -t poc .
```

### 2. Run a new container from your image

**Run in detached (background) mode:**
This starts the container in the background and maps port 8000 on your host to port 8000 in the container (so you can access the web app at http://localhost:8000):
```bash
docker run -d -p 8000:8000 poc
```

**Run in interactive mode with a shell:**
This starts the container and gives you an interactive shell (useful for debugging or manual operations). It also maps port 8000:
```bash
docker run -it -p 8000:8000 poc /bin/bash
```

**Run in interactive mode without exposing ports:**
This gives you a shell inside the container, but does not expose any ports to your host:
```bash
docker run -it poc /bin/bash
```

### 3. List running containers
See all running and stopped containers:
```bash
docker ps -a
```

### 4. Execute a command inside a running container
Open a shell inside an already running container (replace `<container_id>` with the actual container ID from `docker ps`):
```bash
docker exec -it <container_id> /bin/bash
```
