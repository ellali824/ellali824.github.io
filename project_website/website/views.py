from django.shortcuts import render
from website.models import Project, Work
# Create your views here.
# sends the data from the database to the HTML templates 

def cover(request):
    return render(request, 'cover.html',{})

def about(request):
    return render(request, 'about.html',{})
    
def project_index(request):
    projects = Project.objects.all() # perform a query (a command that allows you to create, retrieve, update, or delete objects (or rows) in your database. In this case, you’re retrieving all objects in the projects table.)    
    url = str(Project.image).replace('static', '')
    context = { # The dictionary only has one entry projects to which we assign our Queryset containing all projects. The context dictionary is used to send information to our template. Every view function you create needs to have a context dictionary.
        'projects': projects, 'url': url
    }
    return render(request, 'project_index.html', context) # Any entries in the context dictionary are available in the template, as long as the context argument is passed to render(). You’ll need to create a context dictionary and pass it to render in each view function you create.

def work(request):
    works = Work.objects.all() # perform a query (a command that allows you to create, retrieve, update, or delete objects (or rows) in your database. In this case, you’re retrieving all objects in the projects table.)    
    url = str(Project.image).replace('static', '')
    context = { # The dictionary only has one entry projects to which we assign our Queryset containing all projects. The context dictionary is used to send information to our template. Every view function you create needs to have a context dictionary.
        'works': works, 'url': url
    }
    return render(request, 'work.html', context) # Any entries in the context dictionary are available in the template, as long as the context argument is passed to render(). You’ll need to create a context dictionary and pass it to render in each view function you create.
    