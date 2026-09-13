# Python y Django: ejercicios prácticos y aplicación de Directores y Películas

Repositorio de aprendizaje y práctica con **Python** y **Django**, que reúne ejercicios progresivos de programación y una aplicación web desarrollada con **Django 4**.

El contenido recorre conceptos fundamentales de Python —estructuras de control, funciones, programación orientada a objetos, módulos, ficheros, colecciones, programación funcional, interfaces gráficas y SQLite— y culmina con una aplicación Django basada en el patrón **MVT** para consultar directores y películas.

## Contenido del repositorio

### Ejercicios de Python

Los directorios `EjerciciosTema4` a `EjerciciosTema11` contienen prácticas sobre distintos fundamentos del lenguaje:

- Condicionales y bucles.
- Funciones y resolución de problemas.
- Programación orientada a objetos y herencia.
- Creación y uso de módulos propios.
- Lectura, escritura y serialización de ficheros con `pickle`.
- Colecciones, conjuntos y ordenación de datos.
- Funciones `lambda`, `filter` y `reduce`.
- Interfaces gráficas básicas con **Tkinter**.
- Persistencia de datos con **SQLite**.

## Proyecto Django: Directores y Películas

La carpeta `Django/DirectoresPeliculas` contiene una aplicación web desarrollada con **Django 4.0.5**.

El proyecto implementa dos modelos relacionados:

- `Director`: nombre y apellido del director.
- `Pelicula`: título, descripción y relación con un director mediante `ForeignKey`.

La aplicación permite:

- Consultar el listado de directores.
- Consultar todas las películas.
- Filtrar películas por director.
- Ver el detalle de una película.
- Renderizar la información mediante templates de Django.

## Tecnologías utilizadas

- **Python**
- **Django 4.0.5**
- **SQLite**
- **HTML / Django Templates**
- **Tkinter**
- Programación orientada a objetos
- Patrón MVT de Django

## Estructura principal

```text
OB-Python-Django/
├── EjerciciosTema4/
├── EjerciciosTema5/
├── EjerciciosTema6/
├── EjerciciosTema7/
├── EjerciciosTema8/
├── EjerciciosTema9/
├── EjerciciosTema10/
├── EjerciciosTema11/
└── Django/
    └── DirectoresPeliculas/
        ├── DirectoresPeliculas/
        ├── myapp/
        ├── db.sqlite3
        ├── manage.py
        └── requirements.txt
```

## Puesta en marcha del proyecto Django

Se recomienda utilizar un entorno virtual de Python.

```bash
cd Django/DirectoresPeliculas
python -m venv .venv
```

Activación del entorno virtual:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Aplica las migraciones si es necesario:

```bash
python manage.py migrate
```

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Después, abre en el navegador:

```text
http://127.0.0.1:8000/
```

## Finalidad del repositorio

Este repositorio tiene una finalidad **formativa y práctica**. Sirve como recorrido desde los fundamentos de Python hasta el desarrollo de una aplicación web sencilla con Django, modelos relacionados, consultas mediante ORM, rutas, vistas y templates.

No está planteado como una aplicación preparada para producción, sino como material de aprendizaje y demostración de conceptos de **programación con Python y desarrollo web con Django**.

## Autor

**Silverio Marín** — Docente TIC en Valencia, especializado en programación y desarrollo de software.

Más contenidos sobre **programación, Python y desarrollo de software**:

[**silveriomarin.com/programacion**](https://silveriomarin.com/programacion/)

GitHub: [**@smarinwm**](https://github.com/smarinwm)
