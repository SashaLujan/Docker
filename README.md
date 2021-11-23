# Docker
seminarioDocker TUDAI 

Ejercicio 1 - Construir un Dockerfile con las siguientes características:
● La imagen base tiene que ser python:3
● El contenido del proyecto debe ser copiado a un folder llamado "myapp" dentro de
la imágen.
● Se debe ejecutar el comando "pip install -r requirements.txt" luego de
copiar el proyecto.
● Se debe configurar la imágen (con una sentencia en el Dockerfile) de manera que
cuando se inicialice un container, se ejecute el siguiente comando (dentro de la
carpeta donde se copió el proyecto): python hello.py

Ejercicio 2 - Construir un docker-compose
Construir un docker compose que construya la imágen del ejercicio 1 y agregue un servicio
Mongo. La imagen del servicio mongo es mongo. El servicio mongo necesita 2 variables de
ambiente MONGO_INITDB_ROOT_USERNAME y MONGO_INITDB_ROOT_PASSWORD. Setear
ambas en root. Adicionalmente requiere el mapeo de puerto 27017. (Validar que la uri
en la línea 7 del archivo hello.py coincida con los datos definidos para mongo en el
docker-compose)

Ejercicio 3 - Montar un volumen
Modificar los ejercicios anteriores para que el proyecto no sea copiado dentro de la imágen
construida sino que el código fuente sea mapeado de una carpeta local.
