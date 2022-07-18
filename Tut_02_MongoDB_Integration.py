"""
-> https://www.djongomapper.com/get-started/
-> https://www.django-rest-framework.org/

*)  Step 1: (Setup)
        -> python -m venv venv
                -> cd .\venv\Scripts
                -> activate.bat (to activate virtual env using cmd)
        -> poetry init
        -> poetry add django
        -> poetry add autopep8 (package for auto formatting)
        -> poetry add djongo (mongodb for django)
        -> poetry add pymongo==3.12.3
        -> poetry add dnspython

        *) to rename project folder as config:
            -> https://youtu.be/mUPQii90K5A?t=278

        -> NOTE: we are not setting up users for this project because we are focusing on using mongodb

    Step 2: (update Setting.py)
        -> DATABASES = {
                'default': {
                    'ENGINE': 'djongo',
                    'NAME': 'your-db-name',
                }
            }
        -> python manage.py makemigrations
        -> python manage.py migrate
        
    Step 3: (create user admin)
        -> python manage.py createsuperuser
        
    Step 3: (create apps)
        -> python manage.py startapp todo
        -> inside setting.py:
            ->  INSTALLED_APPS = [
                    'todo',
                ]

    Step 4: add template
        -> ./todo/template/todo.html
        -> TEMPLATES = [
                {
                    'DIRS': [os.path.join(BASE_DIR, 'todo\\template')],
                },
            ]

    Step 4: (update urls, add views, models):
        -> add models inside 'todo/models.py'
        -> update urls.py inside ./config/urls.py
        -> update urls.py inside ./todo/urls.py
        -> create views inside './todo/views.py'
        -> python manage.py makemigrations
        -> python manage.py migrate
    


"""
