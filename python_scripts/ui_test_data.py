import os
# Arrays Key/Values for Lookup
globalvariables = {
    'env': 'np',
    'adminEmail' : 'testingcook@gmail.com',
}

test_urls = {
    'com' : 'https://www.catsofwc.com',
    'org' : 'https://www.catsofwc.org',
}

api_urls = {
    'petstablished' : 'api.petstablished.com'
}

testFormData_MainMenu = {
    'userLogin' : 'catadmin'
    # Use GitHub Secrets for pass
}

database_info = {
    'dbuser' : "catadmin"
}

# Dictionary to select above type
VAR_TYPES = {
    'globals': globalvariables,
    'test_urls': test_urls,
    'api_urls': api_urls,
    'database': database_info
}

# VAR_TYPE Examples
# env = loop_vars("env", "globals")
# url = loop_vars("org", "test_urls")
# api = loop_vars("petstablished", "api_urls")
# db_user = loop_vars("dbuser", "database")
