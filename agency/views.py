from django.shortcuts import render

from django.views.generic import ListView , DetailView

# class AgListView(ListView):
#     template_name = 'agency/a.html'

def agency(request):
    
    context = {}
    
    return render(request , 'agency/a.html' , context)