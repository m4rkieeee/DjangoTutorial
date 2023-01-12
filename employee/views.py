from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    #Get all of the employees that exist in the database
    users =  User.objects.all().values()
    #Get the index.html file to display
    template = loader.get_template('employee/index.html')
    #Load the myEmployees into the html
    context = {
        'users': users
    }
    #Send the request with myEmployees and the request
    return HttpResponse(template.render(context, request))

def delete(request, id):
    if request.user.is_staff:
    #Collect the ID from the data table that needs to be deleted
        deleteEmployee = User.objects.get(id = id)
    #Delete from database
        deleteEmployee.delete()
    #Return to index upon completion
        return HttpResponseRedirect(reverse('employee'))
    else:
        return redirect('/employee')
def update(request, id):
    if request.user.is_staff:
    #Collect the id of the employee
        updateEmployee = User.objects.get(id = id)
    #Load the page updater with Employee connection to the database
        template = loader.get_template('employee/updatePage.html')
        context = {
            'Employee': updateEmployee
        }
    #Send the file over
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/employee')

def updateData(request, id):
    if request.user.is_staff:
    #Get name, title from input form
        getName = request.POST['name']
    #Collect the right id of the user that is being edited and load inputted name, title
        updateEmployee = User.objects.get(id = id)
        updateEmployee.username = getName
    #Push update to database
        updateEmployee.save()
    #Return back to index
        return HttpResponseRedirect(reverse('employee'))
    else:
        return redirect('/employee')

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