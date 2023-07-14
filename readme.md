# ProjectoCanchas

Software de gestion de reservas de canchas hecha con Django, Web-sockets con django-channels e integracion de paypal.
Es importante aclarar que para realizar los pagos de paypal hay que usar Sandbox Paypal.

## Requisitos

- Python 3.x
- Django 3.x
- Django-channels
- Daphne

## Instalación

1. Clone este repositorio
2. Cree un entorno virtual y activelo
3. Instale las dependencias necesarias ejecutando `pip install -r requirements.txt`
4. Cree una base de datos en PostgreSQL y configúrela en `settings.py`
5. Ejecute `python manage.py migrate` para crear las tablas necesarias en la base de datos
6. Ejecute `python manage.py runserver` para iniciar el servidor de desarrollo
7. Acceda a `http://localhost:8000/` en su navegador para ver la aplicación

## Uso

1. Registre un usuario o inicie sesión si ya tiene una cuenta
2. Cargue sus habitaciones desde admin(al ser algo inmueble es lo unico que no se puede hacer desde el cliente).
3. Cree pasajeros, editelos.
4. Realice reservas, editelas.
5. Las reservas quedan almacenadas por status (reservadas, check-in, check out, y no-show).


## developers 
Julian Ward

## Contribución

Si desea contribuir a este proyecto, envíe un pull request con sus cambios.


#### Frontend:


<p align="left">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png"  width=10% height=10%>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"  width=10% height=10%>
</p>
<p align="left">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png"  width=8% height=8%>
</p>


#### Backend:


<p align="left">
<img src="https://raw.githubusercontent.com/github/explore/7456fdff59816d37ef383a6c8f32a26ff7332db2/topics/django/django.png"  width=10% height=10%>




## Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más información.
