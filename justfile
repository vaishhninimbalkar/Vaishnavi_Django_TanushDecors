default:
	cat justfile

install:
	uv pip install -r requirements.txt

run *ARGS: runserver
	

# auth
changepassword:
    python manage.py changepassword


createsuperuser:
    python manage.py createsuperuser



# contenttypes
remove_stale_contenttypes:
    python manage.py remove_stale_contenttypes



# django
check:
    python manage.py check


compilemessages:
    python manage.py compilemessages


createcachetable:
    python manage.py createcachetable


dbshell:
    python manage.py dbshell


diffsettings:
    python manage.py diffsettings


dumpdata:
    python manage.py dumpdata


flush:
    python manage.py flush


inspectdb:
    python manage.py inspectdb


loaddata:
    python manage.py loaddata


makemessages:
    python manage.py makemessages


makemigrations:
    python manage.py makemigrations


migrate:
    python manage.py migrate


optimizemigration:
    python manage.py optimizemigration


sendtestemail:
    python manage.py sendtestemail


shell:
    python manage.py shell


showmigrations:
    python manage.py showmigrations


sqlflush:
    python manage.py sqlflush


sqlmigrate:
    python manage.py sqlmigrate


sqlsequencereset:
    python manage.py sqlsequencereset


squashmigrations:
    python manage.py squashmigrations


startapp:
    python manage.py startapp


startproject:
    python manage.py startproject


test:
    python manage.py test


testserver:
    python manage.py testserver



# rest_framework
generateschema:
    python manage.py generateschema



# sessions
clearsessions:
    python manage.py clearsessions



# staticfiles
collectstatic:
    python manage.py collectstatic


findstatic:
    python manage.py findstatic


runserver *ARGS:
    python manage.py runserver {{ARGS}}


