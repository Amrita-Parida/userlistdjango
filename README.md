### **Tool , Technologies and Version**

Django==2.2.12
djangorestframework==3.11.0
pkg-resources==0.0.0
pytz==2019.3
sqlparse==0.3.1
drf-yasg==1.17.1


### **Installation**

Inside your root directory create VIRTUAL ENVIRONMENT :

virtualenv env --python=python3 (If your Current version of Python is Python2)

virtual env (If your Current default version of Python is Python3)

After creating Virtual Environment you need to Activate that environment so that all the installed package will only available for this Specific Project not for the rest if any.

source env/bin/activate

After activating an environment we need to install all the required packages.

pip install -r requirements.txt

Requirements.txt (Required Packages)

certifi==2019.11.28
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
Django==2.2.12
djangorestframework==3.11.0
drf-yasg==1.17.1
idna==2.9
inflection==0.3.1
itypes==1.1.0
Jinja2==2.11.1
MarkupSafe==1.1.1
packaging==20.3
pkg-resources==0.0.0
pyparsing==2.4.6
pytz==2019.3
requests==2.23.0
ruamel.yaml==0.16.10
ruamel.yaml.clib==0.2.0
six==1.14.0
sqlparse==0.3.1
uritemplate==3.0.1
urllib3==1.25.8



#### **Usage**

**To start the Server:**

python manage.py runserver

##### **To Populate data to the database:**
python manage.py populate_data 2
