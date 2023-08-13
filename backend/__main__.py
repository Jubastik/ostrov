from subprocess import run


run("gunicorn -w 1 -b 0.0.0.0:5000 backend.wsgi:application".split(' '))
