
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

## entering interactive console after regi
* py manage.py shell
* from account.models import User
* users = User.objects.all() -sample only
* users
* user = users.first()
* user.email
* user.name

