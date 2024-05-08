#!bin/bash
echo 'Create migrations'
python manage.py makemigrations api
echo '======================================'

echo 'Migrate'
python manage.py migrate
echo '======================================'

echo 'Start Server'
python manage.py runserser 0.0.0.0:8000