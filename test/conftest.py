# archivo conftest.py es usado para guardar funciones de uso global, que seran usadas por
# los distintos archivos de test


import smtplib

import pytest


@pytest.fixture(scope="module") 
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)