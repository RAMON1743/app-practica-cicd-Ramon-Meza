# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 (puedes cambiarlo si es necesario)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
