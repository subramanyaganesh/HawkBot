How this project was created

    django-admin startproject project_name
    python manage.py startapp app_name
    In your Django project's settings.py file, add 'rest_framework' to the INSTALLED_APPS list:
            INSTALLED_APPS = [
            # ...
            'rest_framework',
            'app_name',  # Add your app here
            ]

Do the following to setup the server

    1. pip install embedchain
    2. pip install django djangorestframework
    3. python manage.py makemigrations
    4. python manage.py migrate
    5. python manage.py runserver





To do a quick check on what are the embedding in the database do the following
1. python manage.py shell
2. Run the following commands
    from embedchain import App
    import os
    from django.conf import settings
    os.environ["OPENAI_API_KEY"] =  settings.OPENAI_KEY
    configPath = os.path.join('/Users/subramanyaganesh/Documents/hawkBot/HawkBot/server/iitbot', "openai.yaml")
    hawk_bot = App.from_config(config_path=configPath)

3. To specify the location for a database that the model has to use do the following
    https://docs.embedchain.ai/api-reference/advanced/configuration
Look into the dir part


Note always use a id with the App instance so that the db does not get updated with every request