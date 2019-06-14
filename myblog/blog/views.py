from django.shortcuts import render,render_to_response
from blog.models import Movie,Weather,Phones,Bags
from django.core.paginator import Paginator
        
def index(request):
    return render(request, 'index.html')
    
def movie(request):
    list1 = Movie.objects.all()
    p = Paginator(list1,25)   
    if p.num_pages <= 1: 
        movie_list = list1  
        data = ''
    else:
        page = int(request.GET.get('page',1))  
        movie_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False 
        right_has_more = False  
        first = False  
        last = False 
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1: 
            right = page_range[page:page+2]  
            if right[-1] < total_pages - 1:  
                right_has_more = True
            if right[-1] < total_pages: 
                last = True
        elif page == total_pages: 
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1] 
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1:
                first = True
        else: 
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1] 
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {  
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'movie.html',context={
        'movie_list':movie_list,'data':data
    })
    
def weather(request):
    list2 = Weather.objects.all()
    bj = Weather.objects.filter(wCity="北京")
    sh = Weather.objects.filter(wCity="上海")
    gz = Weather.objects.filter(wCity="广州")
    wz = Weather.objects.filter(wCity="温州")
    return render_to_response("weather.html",locals()) 

def phones(request):
    list3 = Phones.objects.all()
    p = Paginator(list3,60)
    if p.num_pages <= 1:
        phones_list = list3
        data = '' 
    else:
        page = int(request.GET.get('page',1)) 
        phones_list = p.page(page)
        left = [] 
        right = []  
        left_has_more = False 
        right_has_more = False 
        first = False  
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            if right[-1] < total_pages - 1:  
                right_has_more = True
            if right[-1] < total_pages: 
                last = True
        elif page == total_pages:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else: 
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            right = page_range[page:page+2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {   
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'phones.html',context={
        'phones_list':phones_list,'data':data
    })

def info(request):
    return render(request, 'info.html')

def bags(request):
    list4 = Bags.objects.all()
    return render_to_response("bags.html",locals()) 