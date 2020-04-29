from subprocess import Popen
print("Running scripts...\n")

Popen('python manage.py loaddata update_summary.json')
print("Running scripts...\n")

Popen('python manage.py runserver')
