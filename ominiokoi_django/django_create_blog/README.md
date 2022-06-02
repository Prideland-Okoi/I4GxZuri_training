## [Django: Getting Started]

 

Create a new Python virtual environment.

 

Initialize it, and install Django in it.

 

Create a new Django project. Use your ZuriBoard username as the name of the project.

 

Push your project to a new Public GitHub repository and submit the URL

 

## Technologies
* Py files are compiled using 'python 9.10'
* Tested on Ubuntu 20.04 LTS

## Files
All the files are scripts and programs written in python:

## Resources:
** Python Django Blog in less than 20 minutes - Blogging website tutorial - Code with Stein (www.youtube.com/watch?v=m3hhLE1KR5Q)
** *www.jsdeliver.com*
##Steps
|S/No | Instruction|
|----------|----------|
|1.|mkdir project_folder|
|2.|virtualenv virtual_environment_name|
|3.|source virtual_environment_name/bin/activate|
|4.|django_admin startproject project_name|
|5.|cd project_name|
|6.|python manage.py blog|
|7.|cd blog|
|8.|mkdir templates, cd template|
|9.|mkdir blog|
|10.|touch indexpage.html base.html post_detail.html|
|11.|python manage.py makemigration (update database), python manage.py migrate, python manage.py createsuperuser, python manage.py runserver|
|12.| Other files edited include settings.py admin.py models.py views.py forms.py|
