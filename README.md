# Textual Devops lab

This is a dummy project to understand how to deploy a textual app in a container.

## Usage

* Option 1: The app will run as a web app at http://localhost:8005
```bash
python "app_entrypoint.py"
```

* Option 2: The app will run as a terminal user interface app.
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
docker run -it -p 8005:8005 poc /bin/bash
```

### Inside the container
```bash
docker ps -a
```

### Exec will run inside your existing, running container 
```bash
docker exec -it <container_id> /bin/bash
```
