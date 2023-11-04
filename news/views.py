from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,get_object_or_404
from . models import Category ,News
from polls.models import Wilaya , Follow , Destination
import random
from django.http import HttpResponseRedirect
from django.views.generic import ListView , DetailView
from django.contrib import messages



def following(request):
    if request.user.is_authenticated:
    
        if request.method =='POST':
            wila_id = request.POST['wilaya']
            print(wila_id)
            follow = Wilaya.objects.get(pk=wila_id)
            
            if Follow.objects.filter(wilaya_followed=follow, follower=request.user).exists():
                print("Combination exists")
                messages.info(request , 'Combination exists')
            
                
            else:
                w = Follow(wilaya_followed=follow, follower=request.user)
                w.save()
                messages.success(request, 'Congratulations , you are following this wilaya now!')
            
            return HttpResponseRedirect('/')
    else:
        messages.warning(request, 'User is not logged in ')
               
        return HttpResponseRedirect('/')
        

def dest(request):
    dests = Destination.objects.all()
    
    return render(request , 'news/destination.html' , {'dests': dests})


def wildetail(request, wil_id):
    

  
    wil = get_object_or_404(Wilaya, wilaya_name=wil_id)
    print(type(wil.id))
    wi = get_object_or_404(Wilaya, pk=wil.id)
    
    return render(request, "news/wilaya.html", {"wila": wil  , 'will': wi})


class CategoryView(ListView):
    template_name = 'news/news_list.html'
    context_object_name = 'cats'
    model = Category
    
    def get_queryset(self):
        categories = Category.objects.all()
        cats = random.sample(list(categories) ,len(categories))
        return cats
        
wila = ['Adrar', 'Chlef', 'Laghouat', 'Oum El Bouaghi', 
 'Batna', 'Béjaïa', 'Biskra', 'Béchar', 'Blida', 'Bouira',
 'Tamanrasset', 'Tébessa', 'Tlemcen', 'Tiaret', 'Tizi Ouzou',
 'Alger', 'Djelfa', 'Jijel', 'Sétif', 'Saïda', 'Skikda', 'Sidi Bel Abbès',
 'Annaba', 'Guelma', 'Constantine', 'Médéa','Mostaganem', 'MSila',
 'Mascara', 'Ouargla', 'Oran', 'El Bayadh','Illizi',
 'Bordj Bou Arreridj', 'Boumerdès', 'El Tarf' ,'Tindouf', 'Tissemsilt', 
 'El Oued', 'Khenchela', 'Souk Ahras',
 'Tipaza', 'Mila', 'Aïn Defla', 'Naâma', 'Aïn Témouchent',
 'Ghardaïa', 'Relizane']

def news(request):
    # for i in wila :
    #     n = wila.index(i) + 1
    #     print(n)
        
    #     wil = Wilaya(wilaya_name= i  , wilaya_code= n)
    #     wil.save() 
    #     print('saved')
    
    categories = Category.objects.all()
    wils = Wilaya.objects.all()
    
    cato = random.sample(list(categories) ,len(categories))
    cats = cato[:6]
    context = { 'wilayas': wils,'categories' : categories , 'cats': cats}
    return render(request, 'news/news_list.html', context)



def category(request, cat_id):
    category = get_object_or_404(Category , pk=cat_id)
    
    context = {'category':category}
    
    return render(request, 'news/category.html' , context)