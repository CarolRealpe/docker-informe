# 🐳 Proyecto Docker con Python

## 1. Resumen de los videos vistos

### Video 1: [Docker para principiantes](https://youtu.be/CV_Uf3Dq-EU)
En este video aprendí los **conceptos básicos de Docker**, entendiendo que se trata de una herramienta que permite crear y ejecutar **contenedores**.  
Los contenedores son entornos ligeros que incluyen todo lo necesario para ejecutar una aplicación (código, dependencias, librerías y configuración).  

El video explica cómo Docker **facilita la portabilidad y el despliegue**: una aplicación que funciona en un contenedor se comportará igual en cualquier máquina que tenga Docker instalado.  
También se muestra cómo usar comandos esenciales como:
- `docker run` para ejecutar contenedores.  
- `docker ps` para ver los contenedores activos.  
- `docker images` para listar las imágenes disponibles.  
- `docker build` para crear una nueva imagen desde un `Dockerfile`.

### Video 2: [Docker Compose explicado paso a paso](https://youtu.be/4Dko5W96WHg)
Este video enseña el uso de **Docker Compose**, una herramienta que permite definir y ejecutar **múltiples contenedores** de manera sencilla con un solo archivo llamado `docker-compose.yml`.  
El objetivo principal es **automatizar y simplificar** el despliegue de aplicaciones que necesitan varios servicios (por ejemplo, una app web y una base de datos).  

Aprendí cómo usar comandos como:
- `docker-compose up` para levantar los servicios.  
- `docker-compose down` para detenerlos.  
- `docker-compose build` para reconstruir las imágenes si hay cambios.

---

## 2. Reflexión personal

Al principio Docker me parecía algo complicado, pero después de ver los videos entendí que su poder está en la **facilidad para trabajar de forma aislada**.  
Lo que antes requería instalar muchas dependencias ahora se resuelve con solo un contenedor.

### Ventajas:
- Puedo ejecutar mi aplicación sin preocuparme por el sistema operativo.  
- Ahorra mucho tiempo en configuraciones.  
- Permite compartir proyectos fácilmente con otros desarrolladores.  

### Desafíos:
- Al comienzo, los comandos pueden confundir un poco.  
- Se necesita práctica para entender cómo se relacionan las imágenes, los volúmenes y los puertos.  

### Uso práctico:
Con Docker puedo crear entornos de prueba, desarrollar aplicaciones web, conectar bases de datos o incluso desplegar un sistema completo con un solo comando.  
Es una herramienta que hoy en día es esencial para programadores, sobre todo cuando se trabaja con frameworks o servidores.

---

## 3. Ejemplo práctico: Mini Proyecto con Python y Docker

Este proyecto muestra cómo **ejecutar una aplicación Python dentro de un contenedor Docker** usando un `Dockerfile` y un `docker-compose.yml`.

### Estructura del proyecto
hola-docker/ <br>
│ <br>
├── app/ <br>
│ └── main.py <br>
│ <br>
├── Dockerfile <br>
├── docker-compose.yml <br>
└── README.md 
## El resultado fue: 
- <img width="1680" height="960" alt="image" src="https://github.com/user-attachments/assets/8ad0a6e7-eb94-4645-9d54-38d92bd65ae7" />


