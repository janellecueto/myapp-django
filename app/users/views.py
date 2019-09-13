from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = { 'name' : 'Adonis', 'tasks' : ['Do the laundry', 'Eat'] }
    return render(request, 'users/home.html', context)
