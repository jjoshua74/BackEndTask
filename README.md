# BackEndTask
 
python libraries:
django
djangorestframework
virtualenv

instructions:
pip install virtualenv

create a virtual environment and run the following commands within it:

pip install django
pip install djangorestframework

from within the virtual environment run in terminal:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

------------------------------------------------------------------

Endpoints: 
Localhost:8000/articles/
- lists all the articles

Localhost:8000/articles/1/
- returns the article with id=1

Localhost:8000/articles/1/comments/
- returns all the comments for article 1

Localhost:8000/articles/1/comments/2
- returns the comment with id=2 for article 1

Unit tests:
# Units tests are also something new to me. For some reason the 'from .models import Article' doesn't work in this file.
# I can't figure out what is causing the import error - so this file does not run. I have added a few examples of
# how I would have attempted to run unit tests. I did not add unit tests for the whole project, since the file does
# not actually work and trying to fix the import error has delayed me to the point where I don't think I will submit on
# time if I still try to finish all unit tests.

# sorry 