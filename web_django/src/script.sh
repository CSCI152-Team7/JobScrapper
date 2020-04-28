#!/bin/bash

python manage.py loaddata update_summary.json
python manage.py runserver
