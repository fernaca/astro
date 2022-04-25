from django.shortcuts import render, redirect
from website.models import Category, Object, ImageHome, Trip, Equipment, Published, Links

# Envio de mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.


def home(request):
    homeimage = ImageHome.objects.all().order_by('-rating')
    return render(request, 'home.html', {'homeimage': homeimage})


def equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment.html', {'equipments': equipments})


# def contact(request):
#     return render(request, 'contact.html', {})
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            print(body)
            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect("home.html")
            return render(request, 'contact.html', {'message_name': form.cleaned_data['name']})

    form = ContactForm()
    return render(request, "contact.html", {})


def links(request):
    links = Links.objects.all().order_by('name')
    return render(request, 'links.html', {'links': links})


def published(request):
    published = Published.objects.all()
    return render(request, 'published.html', {'published': published})


def trips(request):
    trips = Trip.objects.all().order_by('-date_trip')
    return render(request, 'trips.html', {'trips': trips})


def about(request):
    return render(request, 'about.html', {})


def portfocategory(request, slug_text):
    # Obtener la categoria segun el slug
    category = Category.objects.filter(slug=slug_text)
    # Obtenemos los objetos de esa categoria
    objetos = Object.objects.filter(category__slug=slug_text)
    return render(request, 'portfocategory.html', {'objetos': objetos, 'category': category})


def portfolio(request):
    querycat = Category.objects.all()
    queryobj = Object.objects.all()
    return render(request, 'portfolio.html', {'categorias': querycat, 'objects': queryobj})


def detail(request, pk):
    queryobj = Object.objects.filter(pk=pk)
    return render(request, 'detail.html', {'objeto': queryobj})
