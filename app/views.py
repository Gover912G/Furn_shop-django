from django.shortcuts import render, redirect

from app.models import Products, Testimony, ShopItem, Team, Blog, SiteDescription, Contact


# Create your views here.

def index(request):
    product = Products.objects.all()
    test = Testimony.objects.all()
    site = SiteDescription.objects.all()[0]
    context = {'nav': 'index', 'pro': product, "tests": test,
               'site':site}
    return render(request, 'index.html', context)


def contact(request):
    site = SiteDescription.objects.all()[0]

    return render(request, 'contact.html', {'nav': 'contact', 'site':site})


def about(request):
    team = Team.objects.all()
    site = SiteDescription.objects.all()[0]

    return render(request, 'about.html', {'nav': 'about','teams':team, "site":site})


def blog(request):
    blog = Blog.objects.all()
    site = SiteDescription.objects.all()[0]

    return render(request, 'blog.html', {'nav': 'blog', 'blogs':blog, 'site':site})


def checkout(request):
    return render(request, 'checkout.html', {'nav': 'check'})


def services(request):
    product = Products.objects.all()
    site = SiteDescription.objects.all()[0]

    return render(request, 'services.html', {'nav': 'services','pro':product, 'site':site})


def shop(request):
    item = ShopItem.objects.all()
    return render(request, 'shop.html', {'nav': 'shop', 'items':item})


def thank(request):
    return render(request, 'thankyou.html', {'nav': 'thank'})


def cart(request):
    return render(request, 'cart.html', {'nav': 'cart'})

def test(request):
    tests = Testimony.objects.all()
    return render(request, 'testimonials.html', {"test":tests})

def messages(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        info = Contact(fname=fname, lname=lname, email=email,message=message)
        info.save()
        return redirect('app:contact')

    return redirect('contact')