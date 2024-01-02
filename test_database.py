import os
import django
from django.db import connections
from django.db.utils import OperationalError

if __name__ == '__main__': # pragma: no cover
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings_production")

    try:
        django.setup() # Load django
        db_conn = connections['default'] # Try making a connection
        c = db_conn.cursor()

    except OperationalError as e:
        print("------------OperationalError------------")
        print(e)
        exit(1)

    exit(0)
