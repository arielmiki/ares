import os
import requests
from bs4 import BeautifulSoup
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__),'.env'))

# From .env file
USERNAME = os.environ.get('SSO_USERNAME', '')
PASSWORD = os.environ.get('SSO_PASSWORD', '')

#HTTP POST to it
auth_url = 'https://academic.ui.ac.id/main/Authentication/Index'

#HTTP GET to it
change_role_url = 'https://academic.ui.ac.id/main/Authentication/ChangeRole' 

#HTTP GET to it
#GET token from url
course_plan_url = 'https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit'


#HTTP POST to it
course_save_url = 'https://academic.ui.ac.id/main/CoursePlan/CoursePlanSave'

course = {
    'c[{COURSECODE}_{CURRICULUM}]':'{CLASS}-{SKS}' ,
    # e.g:'c[CSGE614093_01.00.12.01-2016]':'592114-3',
    'comment':'',
    'submit':'Simpan IRS'}

error = True
counter = 1
while error:
    print('[{}]'.format(counter), end=' ')
    counter += 1

    sess = requests.Session()

    # Authentication
    data = {'u':USERNAME,'p':PASSWORD}
    sess.post(auth_url,data=data)
    sess.get(change_role_url)

    # Get Token
    r = sess.get(course_plan_url)
    soup = BeautifulSoup(r.content,'html.parser')

    try:
        tokens = soup.input['value']
        if not tokens:
            print(soup.select_one('#info h3 a')['href'])
            continue
    except:
        try:
            print(soup.select_one('h2#ti_h').text)
        except:
            print(soup.select_one('.container p').text)
        continue
    

    error = False

# Post Course
course['tokens'] = tokens
sess.post(course_save_url, data=course)

