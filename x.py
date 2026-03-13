from flask import request, make_response
import mysql.connector
from datetime import datetime
import re
from functools import wraps

def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password1",
            database = "travel_destinations"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as ex:
        print(ex, flush=True)
        raise Exception("Database under maintenance", 500)



##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view


##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
REGEX_USER_FIRST_NAME = f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()
    if not re.match(REGEX_USER_FIRST_NAME, user_first_name):
        raise Exception("company_exception user_first_name")
    return user_first_name


##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
REGEX_USER_LAST_NAME = f"^.{{{USER_LAST_NAME_MIN},{USER_LAST_NAME_MAX}}}$"
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name", "").strip()
    if not re.match(REGEX_USER_LAST_NAME, user_last_name):
        raise Exception("company_exception user_last_name")
    return user_last_name


##############################
REGEX_USER_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    user_email = request.form.get("user_email", "").strip()
    if not re.match(REGEX_USER_EMAIL, user_email): 
        raise Exception("company_exception user_email")
    return user_email


##############################
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception("company_exception user_password")
    return user_password
###############################

DESTINATION_TITLE_MIN = 2
DESTINATION_TITLE_MAX = 255
REGEX_DESTINATION_TITLE = f"^.{{{DESTINATION_TITLE_MIN },{DESTINATION_TITLE_MAX}}}$"
def validate_destination_title():
    destination_title = request.form.get("destination_title", "").strip()
    if not re.match(REGEX_DESTINATION_TITLE, destination_title):
        raise Exception("company_exception destination_title")
    return destination_title

####################################################
DESTINATION_COUNTRY_MIN = 2
DESTINATION_COUNTRY_MAX = 255
REGEX_DESTINATION_COUNTRY = f"^.{{{DESTINATION_COUNTRY_MIN },{DESTINATION_COUNTRY_MAX}}}$"
def validate_destination_country():
    destination_country = request.form.get("destination_country", "").strip()
    if not re.match(REGEX_DESTINATION_COUNTRY, destination_country):
        raise Exception("company_exception destination_country")
    return destination_country

######################################

DESTINATION_LOCATION_MIN = 2
DESTINATION_LOCATION_MAX = 255
REGEX_DESTINATION_LOCATION = f"^.{{{DESTINATION_LOCATION_MIN },{DESTINATION_LOCATION_MAX}}}$"
def validate_destination_location():
    destination_location = request.form.get("destination_location", "").strip()
    if not re.match(REGEX_DESTINATION_LOCATION, destination_location):
        raise Exception("company_exception destination_location")
    return destination_location

####################################

def validate_start_date():
    start_date = request.form.get("start_date", "").strip()

    if not start_date:
        raise Exception("company_exception start_date_missing")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise Exception("company_exception start_date_invalid")

    return start_date

#######################################
def validate_end_date():
    end_date = request.form.get("end_date", "").strip()

    if not end_date:
        raise Exception("company_exception end_date_missing")

    try:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise Exception("company_exception end_date_invalid")

    return end_date





