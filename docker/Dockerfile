FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /dagster_home

# Copiar el contenido de la carpeta local warp/ al contenedor
COPY warp/ /dagster_home

# Instalar Flask (u otras dependencias que necesites)
RUN pip install Flask

# Comando por defecto para ejecutar la aplicación
CMD ["python", "prueba.py"]