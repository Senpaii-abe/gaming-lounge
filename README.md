
**_NOTES:_**  

## to create a virtual environment and install dependencies for backend:
* open terminal or cmd, "cd path_ng_project_natin_sa_pc_mo"
* create a virtual environment "python -m venv name_ng_environment_mo"
* active virtual environment "env\Scripts\activate"
* install dependencies
    * pip install django
    * commit mo muna sa github repo
    * pip install djanorestframework
    * pip install djanorestframework-simplejwt
    * pip install pillow
    * pip install django-cors-headers


## migrating database
* enter glbackend by "cd glbackend"
* python manage.py migrate
* python manage.py runserver

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
