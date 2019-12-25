# Django blog
This is my first time using Django web framework. 
This blog is just a page with inputs for creating the articles and possibility to read them.

![Django blog](https://i.ibb.co/vdFg7Dm/photo-2019-12-22-21-50-02.jpg)
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
Put your django secret key here. If you don't have one, you can get it [here](https://djecrety.ir).
### Copy to .env
Now you need to copy the content of example.env to .env file. Use this:
```
> cp example.env .env
```
### Compose up
Now you need build our application, to do this use the following command:
```
> docker-compose up --build -d
```
### Run migrations
Now you need to migrate your postgres database, use this:
```
> docker-compose run web /code/manage.py migrate
```
### Create superuser (optional)
If you want to use Django admin panel you need to create a superuser with the following command:
```
> docker-compose run web python /code/manage.py createsuperuser
```










