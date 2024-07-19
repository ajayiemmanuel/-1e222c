echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate
pip install django
# install all deps in the venv
pip install pillow
pip install six
pip install -U django-jazzmin
pip install psycopg2-binary

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

echo "BUILD END"
