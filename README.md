### Memorial site for DDT
- - -

How to install

1. Init a virtualenv/pyenv/similar
2. `pip install -r requirements.txt`
3. Copy `.env-example` to `.env` and insert required values
4. Init django: `python manage.py migrate`, `python manage.py createsuperuser`, `python manage.py runserver`
5. Create first record for SiteSettings -model
6. Go to http://127.0.0.1:8000 and watch it go
