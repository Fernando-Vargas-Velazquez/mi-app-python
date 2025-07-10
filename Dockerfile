#usaremos una imagen base oficial de python

FROM python:3.10-slim

#Establecer el directorio de trabajo dentro del contenedor

WORKDIR /app

#Copiar el archivo de la aplicación al contenedor 

COPY app.py .

#Comando a ejecutar al iniciar el contenedor 

CMD [ "python", "app.py" ]


