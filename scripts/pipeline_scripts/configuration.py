import os
# Arrays Key/Values for Lookup
globalvariables = {
    'env': 'prod',
    'adminEmail' : 'testingcook@gmail.com',
}

test_urls = {
    'com' : 'https://www.catsofwc.com',
    'org' : 'https://www.catsofwc.org'
}

api_urls = {
    'petstablished' : 'api.petstablished.com'
}

testFormData_MainMenu = {
    'userLogin' : 'catadmin'
}

# Dictionary to select above type
VAR_TYPES = {
    'globals': globalvariables,
    'test_urls': test_urls,
    'api_urls': api_urls,
}
