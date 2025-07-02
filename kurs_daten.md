
# Django Restframework Seminar

**Github:**

[https://github.com/kaptainkrust/django\_event\_project](https://github.com/kaptainkrust/django\_event\_project)



**Doku:**

[https://djangoheroes.friendlybytes.net/](https://djangoheroes.friendlybytes.net/)



**Django Docs:**

[https://docs.djangoproject.com/en/5.2/](https://docs.djangoproject.com/en/5.2/)



**Projekt anlegen**

django-admin startproject project .



**App anlegen**

 python manage.py startapp user

 

 

**PIP TOOLS**

 pip-compile requirements.in

 pip-sync requirements*.txt

 

** Ruff (linter, formatter)**

 [https://github.com/astral-sh/ruff](https://github.com/astral-sh/ruff)

 

 

 

** Modernere Packagetools**

 - UV

 - Poetry

 (basieren auf pyproject.toml)

 [https://peps.python.org/pep-0621/](https://peps.python.org/pep-0621/)

 

** Feldtypen**

 [https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-types](https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-types)

 

** Datenbank migrieren**

 manage.py makemigrations events

 manage.py migrate events

 

** User Model**

 [https://djangoheroes.friendlybytes.net/create\_project/user\_model.html](https://djangoheroes.friendlybytes.net/create\_project/user\_model.html)





**Django Debug Toolbar**

[https://djangoheroes.friendlybytes.net/working\_with\_forms/debug\_toolbar.html](https://djangoheroes.friendlybytes.net/working\_with\_forms/debug\_toolbar.html)



**PRE COMMIT**



pip install pre-commit

git init

pre-commit install

pre-commit run --all-files



**Prefetch Related**

[https://docs.djangoproject.com/en/5.2/ref/models/querysets/#select-related](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#select-related)





**Aufgabe**

- Fabriken erstellen (optional)

- API erstellen für Projekt von gestern (Serializer, View, Urls)



**TODO Mittwoch**

- django-environ (.env - Datei)

- Validatoren (Model, Serializer)

- Logging

- Token Authentifizierung (KNOX, JWT)

- Permissions und eigene Permissions

- Bulk Creation von Events

- Pytest mit Factory Boy / Coverage

- Nested Serializer

- Filter

- Caching

- Django-Extensions

- Swagger UI 

- UV 



**Pytest Settings für pyproject.toml**

[tool.pytest.ini\_options]

DJANGO\_SETTINGS\_MODULE = "project.settings"

python\_files = ["tests.py", "test\_*.py", "*\_tests.py"]

addopts = "--cov --cov-report=term-missing"

norecursedirs = ["migrations"]



**Django Logging SEttings für Streaming auf Console**

LOGGING = {

    "version": 1,

    "disable\_existing\_loggers": False,

    "handlers": {

        "console": {

            "class": "logging.StreamHandler",

        },

    },

    "root": {

        "handlers": ["console"],

        "level": "INFO",

    },

}







**Ruff Settings in pyproject.toml reinkopieren:**




