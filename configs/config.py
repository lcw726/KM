import os

class Config(object):
    SECRET_KEY = 'key'
    
    LDAP_SERVER = "ldap://10.3.3.13:389"
    LDAP_HOST = 'tw.fpg.com'

    AUTH = [
    "N000130115",
    "N000148912",
    "N000155642",
    "N000159761",
    "N000165170",
    "N000174156",
    "N000175896",
    "N000161878",
    "N000183062"
    ]


class ProductionConfig(Config):
    DEBUG = False

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('GENTELELLA_DATABASE_USER', 'gentelella'),
        os.environ.get('GENTELELLA_DATABASE_PASSWORD', 'gentelella'),
        os.environ.get('GENTELELLA_DATABASE_HOST', 'db'),
        os.environ.get('GENTELELLA_DATABASE_PORT', 5432),
        os.environ.get('GENTELELLA_DATABASE_NAME', 'gentelella')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
