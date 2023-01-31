# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:43:19 2020

@author: N000174156
"""

import ldap
from flask import current_app as app


def ladp_auth(user, pwd):
    LDAP_SERVER = app.config['LDAP_SERVER']
    LDAP_USERNAME = f"{user}@{app.config['LDAP_HOST']}"
    LDAP_PASSWORD = f"{pwd}"

    ldap_client = ldap.initialize(LDAP_SERVER)
    ldap_client.set_option(ldap.OPT_REFERRALS, 0)

    try:
        ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
        return True
    except ldap.INVALID_CREDENTIALS:
        print("Your username or password is incorrect.")
        return False
    except ldap.LDAPError as e:
        if type(e.message) == dict and e.message.has_key("desc"):
            print(e.message["desc"])
        else:
            print(e)
        return False
    finally:
        ldap_client.unbind()


def authenticate_user(credentials):
    """
    generic authentication function
    returns True if user is correct and False otherwise
    """
    #
    # replace with your code
    # authed = (credentials['user'] in users) and (credentials['password'] == users[credentials['user']])
    #
    #
    ### LDAP
    authed = ladp_auth(credentials["user"], credentials["password"])

    return authed
