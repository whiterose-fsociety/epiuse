# epiuse
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mo-rsa24/epiuse?color=blue&logo=django&logoColor=blue&style=plastic)


Epiuse employee management system
## Video
> You Can Watch The Video Above
## Installation
> Ensure that you have python3 installed

`$ git clone https://github.com/mo-rsa24/epiuse/`

`$ cd epiuse`

`$ virtualenv -p=/usr/bin/python3.8 venv`

`$ source venv/bin/activate`

`$ cd epiuse`

`$ pip install -r requirements.txt`
 
> If pip does not work try this

 `$ python3 -m pip install -r requirements.txt`
 
## Preparing The Database
> Find a folder that has the file 'manage.py'

`$ python manage.py makemigrations`

`$ python manage.py migrate`
  
 
## Running The Application

> Go the folder that has the "manage.py" file

`$ python3 manage.py runserver`

> Go to your browser and go the link: http:127.0.0.1:8000
