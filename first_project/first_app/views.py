from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    #template = loader.get_template('first_app/index.html')
    my_dict = {
        'insert_me':'Hello from views.py'
    }
    #return HttpResponse(template.render(my_dict, request))
    return render(request, 'first_app/index.html', my_dict)