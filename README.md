# Django blog
This is my first time using Django web framework. 
This blog is just a page with inputs for creating the articles and possibility to read them.
## Getting Started
On this section you will understand how to get a copy of the project and 
deploy it on your local machine for development or testing purposes.
### Get the source code
First, you need to get this project on your local machine. 
Well, go to the directory you want to see this project in.
```
> cd ~/.../<target_directory>
```
Now you can get all the source code of this project using git clone command.
```
> git clone https://github.com/KamilRizatdinov/django_blog.git
```
Congratulations, now you have all the source code of this project!
## Deployment using Docker
### Change environmental variables
Now you can see example.env with such content inside it:
```
SECRET_KEY=your_django_secret_key_here
```
As you already guessed - you need to put your django secret key here. Don't worry if you don't have one, you can get it [here](https://djecrety.ir).
### Copy to .env
Now you need to copy the content of example.env to .env file. Use this:
```
> cp example.env .env
```
### Run migrations
Now you need to run the migrations, to do this use the following command:
```
> docker-compose run web python /app/manage.py migrate
```
### Create superuser (optional)
If you want to use Django admin panel you need to create a superuser with the following command:
```
> docker-compose run web python /app/manage.py createsuperuser
```
### Start application
Now you can start this application by running:
```
> docker-compose up -d --build
```










