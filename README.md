#Game project
para correr el juego debes escribir las siguientes instrucciones en la terminal
```sh
cd game 
python3 main.py
```
#App Project para Virtual Environment

```sh
1. Clona el repositorio con el siguiente comando:
   git clone https://github.com/monick96/python-practice2.git
   
2. Navega al directorio del proyecto:
   cd app

3-Crea el entorno virtual
    python3 -m venv env
   
4. Activa el entorno virtual:
   source env/bin/activate
   
5. Instala las dependencias del proyecto:
   pip3 install -r requirements.txt
   
6. Ejecuta el archivo principal:
   python3 main.py
```
#Para correr con Docker

```sh
1- Instala Docker siguiendo las instrucciones adecuadas para tu sistema operativo:

   *Para Windows y macOS: Descarga Docker Desktop desde el sitio oficial de Docker        
   (https://www.docker.com/products/docker-desktop) e instálalo.
   *Para Linux: Sigue las instrucciones específicas para tu distribución para instalar Docker.

2- Clona el repositorio con el siguiente comando:
   git clone https://github.com/monick96/python-practice2.git

3- Navega al directorio del proyecto:
   cd python-practice2/app

4-Ejecuta el siguiente comando para construir la imagen del contenedor:
   docker-compose build

5- Ejecuta el siguiente comando para iniciar el contenedor:
   docker-compose up

6-Verifica el estado de los contenedores ejecutando el siguiente comando:
   docker-compose ps
```