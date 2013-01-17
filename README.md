#Getting Started with Django

In this module, we will create our first Django Application with two views, that will greet you with your name.

## Lesson 1 - Creating the Project
To get started with Django, you need to install Django first. If you have `pip` installed you can simply run `pip install Django`. Luckily, this has already been done on the codelearn server, so you don't need to bother about the installation process. However, if you want to work on your local mahcine you can follow the [instuctions here](https://docs.djangoproject.com/en/1.4/intro/install/)

To create your first django project, goto the console and run

	django-admin.py startproject django_blog
	
This will create a folder *django_blog* with the following structure. Here, *django_blog* is the name of our project.
	
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	└── manage.py
	
These files are:

- **The outer django_blog/** directory is just a container for your project. Its name doesn't matter to Django; you can rename it to anything you like.
- **manage.py:** A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin.py and manage.py.
- **The inner django_blog/** directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside it (e.g. import mysite.settings).
- **django_blog/__init__.py:** An empty file that tells Python that this directory should be considered a Python package. (Read more about packages in the official Python docs if you're a Python beginner.)
- **django_blog/settings.py:** Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- **django_blog/urls.py:** The URL declarations for this Django project; a "table of contents" of your Django-powered site. You can read more about URLs in URL dispatcher.
- **django_blog/wsgi.py:** An entry-point for WSGI-compatible webservers to serve your project. See How to deploy with WSGI for more details.

Now, that our project is setup. We can test it by running a development server

	python manage.py runserver
	
This will run a development server on port 8000. If you preview your app now you'll see a **"Welcome to Django"** page, in pleasant, light-blue pastel. It worked!

## Lesson 2 - Creating the app
To create our application, we'll run this command inside our Django project in th console.

	python manage.py startapp blog
This will create a folder *blog* inside our project. The new file structure should look something like this.


	├── blog
	│   ├── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   ├── views.py
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	└── manage.py
	
Each Django application will consist of *models.py, tests.py and views.py*. For this module we'll only be dealing with *views.py* which shall be used to serve the content of our application.

Now open *views.py* for editing, replace its content with the following code

	from django.http import HttpResponse


	def home(request):
        return HttpResponse('<h1>Hey Joe</h1>')
    

This will create a `home view` for our application that simply returns **Hey Joe**.

Now that our view is ready, we need to tell our our django project when to serve this view. If you have been following closely, you can guess. We do this in `django_blog/urls.py`

Now, add the following python code below the comment on line 8

	url(r'^$', 'blog.views.home'),

This shall be enough to tell our django project, to serve the home view in blog application when we visit the root url of the project.

You can test the same by running development server again.

	python manage.py runserver

That is it, preview your application and you shall see the **Hey Joe** message.
## Lesson 3 - Displaying your name

In this lesson, we'll display your name instead of Joe. To do this we'll need some input from the user.

So we'll create another view `greeting` in `blog/views.py`. Add the following lines to the `views.py`

	def greeting(request, name):
        return HttpResponse("<h1>Hey %s</h1>" % name)
        
**Note-** We are taking additional parameter called `name` in our view. This view shall return *Hey <Name>*

Now, we move onto our `urls.py', to serve the greeting view in our project. You can do this by adding the line, just below the previous route for home view.

    url(r'^(?P<name>\w+)/$', 'blog.views.greeting'),
    
This route shall accept any digit, character and underscore. (Matching with `/w` regular expression). And store it in variable name, which shall be passed to our django view `greeting`

So now if you test your application on the development server you shall still see **Hey Joe**. But if you visit `<WebsiteName>/<Your Name>`, you should see the greeting with your name.

That's it for this module. We'll get give into modules and get started with blog views in the next module.