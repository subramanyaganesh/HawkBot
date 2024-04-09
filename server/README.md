How this project was created

    django-admin startproject project_name
    python manage.py startapp app_name
    In your Django project's settings.py file, add 'rest_framework' to the INSTALLED_APPS list:
            INSTALLED_APPS = [
            # ...
            'rest_framework',
            'iit-hawkbot',  
            ]

Do the following to setup the server
Installations

    1. pip install embedchain
    2. pip install django djangorestframework
    3. pip install django-environ
    4. pip install django-cors-headers

Execution
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



Location of deployment::::ssh -l sganesh10 192.168.147.35
 XWjJVJsJdXhH


 run application ::

cp /root/ssl/2024-april/wildcard.crt  /localHawkBot/HawkBot/server/cert/hawkbot.crt

nohup python3 manage.py runserver 192.168.147.35:8000 & 

nohup python3 manage.py runsslserver --cert /root/ssl/2024-april/wildcard.crt --key /localHawkBot/HawkBot/server/cert/hawkbot.key 192.168.147.35:8000 &


python3 manage.py runsslserver --cert /root/ssl/2024-april/wildcard.crt --key /localHawkBot/HawkBot/server/cert/hawkbot.key 192.168.147.35:8000


kill -9 `ps -ef|grep runserver|grep -v grep|awk {'print $2'}`
kill -9 `ps -ef|grep runsslserver|grep -v grep|awk {'print $2'}`


868ms. Visit https://platform.openai.com/account/rate-limits to learn more.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}