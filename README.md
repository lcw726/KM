# PDF File Online Viewing Website

This project is delicated to share secret PDF files for certain people, not allow direct download but to view these files only on browsers. Although tech-savvy can still find ways to get the "secret" PDF files, most people can only copy or print screen some content from these files, which stop them from plagiarism.

This project integrates PDF.js with Flask using: 
- [flask](https://flask.palletsprojects.com/) for web framework
- [Blueprints](https://flask.palletsprojects.com/en/latest/blueprints/) for scalability
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system
- [PDF.js](https://mozilla.github.io/pdf.js/) for displaying PDF files
- [TOML](https://toml.io/en/) for human-readable config
- [Gunicorn](https://gunicorn.org/) for production grade Python WSGI HTTP Server

SECRET_KEY must be set in /instance/config.toml.

LDAP_SERVER and LDAP_HOST must be set in /instance/config.toml to make LDAP function normally.

LDAP auth is marked for devolpment under windows, please revert it back under app/extensions.py and app/base/routes.py.

Python-LDAP installation would be problematic on windows, auth through ldap only if you rebuild this project on Linux.

{{static}}/pdf_files/ folder is hidden for obivios reasons, you can add your PDF files in the folder, and bind it through /instance/config.toml.

##  Install requirements 
    pipenv install
    or
    pip install -r requirements.txt

### Run the application
    (pipenv run) python run.py
    or 
    (pipenv run) sh run_web.sh
