from django.shortcuts import render
from django.views.generic import ListView
from .models import Campsite
from django.http import HttpResponse


import publica

def index(request):
    campsites_list = [
        {'name': 'Abracal',
         'location': 'San Javier - Córdoba',
         'category':'Camping',
         'services':'Conservación, educación ambiental, observación de fauna silvestre, turismo',
         'image': 'abracal.jpeg',
         },
          {'name': 'Achalay',
         'location': 'Primera sección de islas del Delta, Tigre, Provincia de Buenos Aires',
         'category':'Camping',
         'service':'Conservación, educación ambiental, turismo, investigación, observación de fauna silvestre',
         'image': 'achalay.jpeg',
         },
          {'name': 'Curindy',
         'location': 'Localidad de Garuhapé, provincia de Misiones',
         'category':'Camping',
         'service':'Conservación, explotación forestal, ganadería, investigación y turismo',
         'image':'curindy.jpeg',
         },
 
    ]

    context = {                
                'campsites': campsites_list,
                'title': "Reservas Naturales Privadas",
            }
    return render(request,'publica/index.html',context)

def login(request):

    return render(request,'publica/login.html')

def get_categories(request, category, campsites_list):
    filtered_campsites = [camp for camp in campsites_list if camp['category'] == category]
    
    context = {'campsites_list': filtered_campsites, 'category': category}
    
    return render(request, 'campisite_category.html', context)

class CampsiteListView(ListView):
    model = Campsite
    template_name = 'campsite_list.html'
    context_object_name = 'campsites'

    def get_queryset(self):
        category = self.kwargs['category']
        return Campsite.objects.filter(category=category)