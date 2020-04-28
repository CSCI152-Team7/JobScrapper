#!/bin/bash
path=”C:\Users\Andy\Documents\GitHub\JobScrapper\web_django\src”
python manage.py loaddata update_summary.json
python manage.py runserver
