FROM python:3.12-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de aplicación
WORKDIR /app

# Copiar archivos necesarios
COPY . /app/

# Instalar dependencias de Python sin almacenar los archivos de cache de pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Set working directory to where the app should be served from
WORKDIR /app

# Expose the port that textual serve uses by default
#EXPOSE 8005
#CMD ["python", "app_entrypoint.py"]

CMD ["python", "app.py"]