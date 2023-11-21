import requests

url = "https://login.microsoftonline.com/f8cdef31-a31e-4b4a-93e4-5f571e91255a/oauth2/v2.0/token"
data = {
    'grant_type': 'client_credentials',
    'client_id': 'a3b437a6-6853-4685-9f2a-e616295684fe',
    'client_secret': 'Deq8Q~L5Fk6Q1aiC1-MJn..aFUE.sx_~mMdTydeQ',
    'scope': 'https://graph.microsoft.com/.default'
}

response = requests.post(url, data=data)
access_token = response.json()['access_token']