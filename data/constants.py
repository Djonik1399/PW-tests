import os

class Constants:
    try:
        email = os.getenv('AUTH_EMAIL')
        password = os.getenv('AUTH_PASSWORD')
    except KeyError:
        print("EMAIL OR PW WASN'T FOUND")