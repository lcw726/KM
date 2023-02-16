# PDF Online Viewer

This project integrates mozilla/pdf.js with Flask using: 
- [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for scalability
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system (passwords hashed with bcrypt)
- [dash](https://dash.plot.ly/)

SECRET_KEY must be set in /instance/config.toml.

{{static}}/pdf_files/ folder is hidden for obivios reasons, you can add your PDF files in the folder, and bind it through /instance/config.toml and app/base/templates/report_list.html.

LDAP auth is marked for devolpment under windows, please revert it back under app/extensions.py and app/base/routes.py.

LDAP_SERVER and LDAP_HOST must be set in /instance/config.toml to make LDAP funcion normally.

##  Install requirements 
    pipenv sync
    or
    pip install -r requirements.txt

### Run the application
    (pipenv run) python run.py
    or 
    (pipenv run) sh run_web.sh
