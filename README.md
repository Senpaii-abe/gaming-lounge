
**_NOTES:_**  
gamer2: 426ccad7-c6b1-4d64-a2e0-8c5b018f1b34
gamer1: 9842445d-c540-4e9f-bb73-5b6219b64c24
## to create a virtual environment and install dependencies for backend:
* open terminal or cmd, "cd path_ng_project_natin_sa_pc_mo"
* create a virtual environment "python -m venv name_ng_environment_mo"
* active virtual environment "env\Scripts\activate"
* install dependencies
    * pip install django
    * pip install djangorestframework
    * pip install djangorestframework-simplejwt
    * pip install pillow
    * pip install django-cors-headers
    * pip install python-dotenv


## migrating database
* enter glbackend by "cd glbackend"
* python manage.py migrate
* npm run dev (outside env - cd glfrontend)
* python manage.py runserver (inside backend)


## entering interactive console after regi
* py manage.py shell
* from account.models import User
* users = User.objects.all() -sample only
* users
* user = users.first()
* user.email
* user.name

## database main-2023-09-30-9nht4s
* username = q81cyopsenxaxismckq1
* password = pscale_pw_aDhH0EGx4qBMBmxmZaBEkUPhru7dcP21SHsnWaj8KIT

* .env: 
DB_NAME=dbgaminglounge
DB_USER=q81cyopsenxaxismckq1
DB_PASSWORD=pscale_pw_aDhH0EGx4qBMBmxmZaBEkUPhru7dcP21SHsnWaj8KIT
DB_HOST=aws.connect.psdb.cloud
DB_PORT=3306
MYSQL_ATTR_SSL_CA=/etc/ssl/certs/ca-certificates.crt
