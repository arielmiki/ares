import os
import requests
from bs4 import BeautifulSoup
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__),'.env'))

USERNAME = os.environ['SSO_USERNAME']
PASSWORD = os.environ['SSO_PASSWORD']


#HTTP POST to it
auth_url = 'https://academic.ui.ac.id/main/Authentication/Index'
data = {'u':USERNAME,'p':PASSWORD}

#HTTP GET to it
change_role_url = 'https://academic.ui.ac.id/main/Authentication/ChangeRole' 

#HTTP GET to it
#GET token from url
course_plan_url = 'https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit'


#HTTP POST to it
course_save_url = 'https://academic.ui.ac.id/main/CoursePlan/CoursePlanSave'
course = {'c[COURSECODE_CURRICULUM]':'number-sks','comment':'','submit':'Simpan IRS'}

sess = requests.Session()
sess.post(auth_url,data=data)
sess.get(change_role_url)

r = sess.get(course_plan_url)
soup = BeautifulSoup(r.content,'html.parser')

tokens = soup.input['value']
course['tokens'] = tokens

print(tokens)	



