# PDF Online Viewer

This project integrates PDF.js with Flask using: 
- [flask](https://flask.palletsprojects.com/) for web framework
- [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for scalability
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system
- [PDF.js](https://mozilla.github.io/pdf.js/) for displaying PDF files
- [TOML](https://toml.io/en/) for human-readable config
- [Gunicorn](https://gunicorn.org/) for production grade Python WSGI HTTP Server

SECRET_KEY must be set in /instance/config.toml.

LDAP_SERVER and LDAP_HOST must be set in /instance/config.toml to make LDAP funcion normally.

LDAP auth is marked for devolpment under windows, please revert it back under app/extensions.py and app/base/routes.py.

{{static}}/pdf_files/ folder is hidden for obivios reasons, you can add your PDF files in the folder, and bind it through /instance/config.toml.

##  Install requirements 
    pipenv sync
    or
    pip install -r requirements.txt

### Run the application
    (pipenv run) python run.py
    or 
    (pipenv run) sh run_web.sh
