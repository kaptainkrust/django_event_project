# Django DRF Beispielprojekt

## Installation

    python -m venv .venv
    source ./.venv/bin/activate
    cd event_manager
    pip-sync requirements*.txt

## Testdaten erstellen

    python manage.py create_user
    python manage.py create_events --number 100
    
## Programm starten

    python manage.py runserver
    
    