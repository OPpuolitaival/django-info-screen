# Running the example application

Clone django-info-screen:

```  
git clone https://github.com/OPpuolitaival/django-info-screen.git
cd django-info-screen/example
pip install -r requirements.txt

# Normal install
pip install -e git+https://github.com/OPpuolitaival/django-info-screen.git#egg=Package
# Development install
pip install -e pip install -e `pwd`/..
```

Make migrations after changing the model:
```
python manage.py makemigrations
```

Create database and superuser:

```
python manage.py migrate
python manage.py createsuperuser
```


Now you need to run the Django development server:

```
python manage.py runserver
```

You should then be able to open your browser on http://127.0.0.1:8000 and
see a page with links to sign in or sign up.
