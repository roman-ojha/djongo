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
        -> python manage.py startapp cards
        -> python manage.py startapp cards
            -> 

    Step 4: (update urls, add views, models):
        -> update urls.py inside ./config/urls.py
        -> update urls.py inside ./cards/urls.py


"""
