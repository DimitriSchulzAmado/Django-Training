# Steps

### Basic Steps
***
- Instalar os pacotes:

    `pip install -r requirements.txt`


- Criar um projeto Django:

    `django-admin startproject <project_name> .`


- Executar o servidor:

    `python manage.py runserver`


Configurar o runserver para run/debug direto pelo PyCharm

- Criar um novo app:

    `django-admin startapp <app_name>`


- Criar as migrações para serem executados no BD:

    `python manage.py makemigrations`


- Executar as alterações no BD:

    `python manage.py migrate`


- Criar um superusuario:

    `python manage.py createsuperuser`


- Configurar o pycharm para rodar o python console com suporte ao django:

    ```
    import sys; os, django
    print('Python %s on %s' % (sys.version, sys.platform))
    sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
    django.setup()
    ```

- Instalar o ipython (para um console mais poderoso): `pip install ipython`


### Docker
***
Rodar com docker-compose:

- Se o arquivo tiver o nome diferente de "docker-compose.yml":

    `docker-compose -f file_name.yml build`

    `docker-compose -f file_name.yml up -d`


- Senão rodar somente:

    `docker-compose up`


- Entrar na maquina:
    `docker exec -it <container_id> bash`