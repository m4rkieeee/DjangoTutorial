from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
from django.db.models import Q
# Create your views here.

def index(request):
    #Get all of the employees that exist in the database
    myEmployees =  Employee.objects.all().values()
    #Get the index.html file to display
    template = loader.get_template('employee/index.html')
    #Load the myEmployees into the html
    context = {
        'myEmployees': myEmployees
    }
    #Send the request with myEmployees and the request
    return HttpResponse(template.render(context, request))

def create(request):
    #Load the createPage page
    template = loader.get_template('employee/createPage.html')
    #Send the createPage to user
    return HttpResponse(template.render({}, request))

def createData(request):
    #Get the submitted username & title
    getName = request.POST['name']
    getTitle = request.POST['title']
    #Load the user submitted date into Employee
    newEmployee = Employee(name=getName, title=getTitle)
    #Save Employee to the database
    newEmployee.save()
    #Return back to the index page upon completion
    return HttpResponseRedirect(reverse('employee'))

def delete(request, id):
    #Collect the ID from the data table that needs to be deleted
    deleteEmployee = Employee.objects.get(id = id)
    #Delete from database
    deleteEmployee.delete()
    #Return to index upon completion
    return HttpResponseRedirect(reverse('employee'))

def update(request, id):
    #Collect the id of the employee
    updateEmployee = Employee.objects.get(id = id)
    #Load the page updater with Employee connection to the database
    template = loader.get_template('employee/updatePage.html')
    context = {
        'Employee': updateEmployee
    }
    #Send the file over
    return HttpResponse(template.render(context, request))

def updateData(request, id):
    #Get name, title from input form
    getName = request.POST['name']
    getTitle = request.POST['title']
    #Collect the right id of the user that is being edited and load inputted name, title
    updateEmployee = Employee.objects.get(id = id)
    updateEmployee.name = getName
    updateEmployee.title = getTitle
    #Push update to database
    updateEmployee.save()
    #Return back to index
    return HttpResponseRedirect(reverse('employee'))

def blog(request):
    posts = BlogPosts.objects.filter(featured = False)
    featuredPost = BlogPosts.objects.filter(featured = True)
    template = loader.get_template('employee/blog.html')
    context = {
        'posts': posts,
        'featuredPost': featuredPost
    }
    return HttpResponse(template.render(context, request))

def detailsPage(request, id):
    #Collect the id of the employee
    detailsPost = BlogPosts.objects.get(id = id)
    #Load the page updater with Employee connection to the database
    template = loader.get_template('employee/detailsPage.html')
    context = {
        'posts': detailsPost
    }
    #Send the file over
    return HttpResponse(template.render(context, request))