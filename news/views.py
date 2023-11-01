from django.shortcuts import render ,get_object_or_404
from . models import Category ,News


def news(request):
    categories = Category.objects.all()
    
    context = {'categories' : categories}
    return render(request, 'news/news_list.html', context)



def category(request, cat_id):
    category = get_object_or_404(Category , pk=cat_id)
    
    context = {'category':category}
    
    return render(request, 'news/catwgory.html' , context)