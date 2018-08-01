# Making-a-api-using-jwt-in-django

First go to convenient location in your system.  
For example i created this project in drive F: and first i created a folder and i gave a name it (jwt).  
Then i open the terminal/cmd at this location (F:/jwt/). And type  
1. django-admin startproject "give a project name"  
2. cd "project name".  
Enter into manage.py file.  
Type  
3. python manage.py startapp "Give app name".  
you can check it wheather it is working or not.  
Open terminal and go to that location where manage.py file is present.  
And type  
4. python manage.py runserver.  
And open browser and type  
http://127.0.0.1:8000  
and you will see a message "Welcome Django".  
After it change the settings.py file according to above give file.  
Then copy the models.py file code in your app models.py file and make migration to create the databse.
open pyCharm editor terminal and type  
5. python manage.py makemigrations "app name"  
It will give you a pop message like "Create User"  
6. python manage.py migrate
Then copy whole code as it  is .  
And go to postman and type the following url in url field  
http://127.0.0.1:8000/user/create/  
and change the request like Post and go to header and type key and value  
7. key="Type of Content", value="Application/JSON"  
Then you go to body and select "raw" section and type following  in the body (in JSON format)  
{
"email":"",  
"first_name":"",
"last_name":"",
"password":"",
}  
It will create a user. Next if you want to create token of registered user then go to url field and change the url  
http://127.0.0.1:8000/user/obtain_token/  
and change the request to "GET" and go to header and  
Repeat step 7 and go to body and type following in the body  
{
"email":"",
"password":""
}  
And you will get a jwt token you can verify it using jwt website.
And you can authenticate a user.

