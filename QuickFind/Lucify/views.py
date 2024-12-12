from django.shortcuts import render,redirect
from .models import Hero,About,AboutFeatures,Deliveries,Section,Service,ServiceSection,PortfolioItem
from django.http import JsonResponse
from django.core.mail import send_mail
# Create your views here.


def index(request):
    hero = Hero.objects.all()
    about = About.objects.all()
    feature = AboutFeatures.objects.all()
    deliver = Deliveries.objects.all()
    section = Section.objects.all()
    service = Service.objects.first()
    servicesection = ServiceSection.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    context = {
        'hero':hero,
        'about':about,
        'feature':feature,
        'deliver':deliver,
        'section':section,
        'service':service,
        'servicesection':servicesection,
        'portfolio_items': portfolio_items
        }
    return render(request,'index.html',context)




from .models import Business

def business_list(request):
    businesses = Business.objects.all()
    query = request.GET.get('q')
    if query:
        businesses = businesses.filter(name__icontains=query)
    return render(request, 'business_list.html', {'businesses': businesses})

def business_detail(request):
    business = Business.objects.all()
    return render(request, 'business_detail.html', {'business': business})






















