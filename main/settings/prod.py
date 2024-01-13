from .base import *

# DATABASES={
#     "default":{
#         "ENGINE": "django.db.backends.postgresql.psycopg2",
#         "NAME": config("SQL_DATABASE"),
#         "USER": config("SQL_USER"),
#         "PASSWORD": config("SQL_PASSWORD"),
#         "HOST": config("SQL_HOST"),
#         "PORT": config("SQL_PORT"),
#         "ATOMIC_REQUESTS": True,
#     }
# }

DATABASES={
    "default":{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}