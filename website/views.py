from django.shortcuts import render, redirect
from website.models import Category, Object, ImageHome, Trip, Equipment, Published, Links
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Envio de mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def entry_not_found(request, exception):
    return render(request, '404.html')
    
def paginacion(in_object_list, in_per_page, request):
## Funcion para manejar la paginacion.
## Recibe la lista y devuelve el objeto
#Paginacion
    paginator = Paginator(in_object_list, per_page=in_per_page)
    page = request.GET.get('page')
    try:
        paginat = paginator.page(page)
    except PageNotAnInteger:
# If page is not an integer deliver the first page
        paginat = paginator.page(1)
    except EmptyPage:
# If page is out of range deliver last page of results
        paginat = paginator.page(paginator.num_pages)

    return paginat

def home(request):
    homeimage = ImageHome.objects.all().order_by('-rating')
    return render(request, 'home.html', {'homeimage': homeimage})


def equipments(request):
    Object_list = Equipment.objects.all().order_by('name')
# Resolver Paginacion
    equipments = paginacion(Object_list, 2, request)

    return render(request, 'equipment.html', {'equipments': equipments})


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
    Object_list = Trip.objects.all().order_by('-date_trip')
#Paginacion
    paginator = Paginator(Object_list, per_page=10)
    page = request.GET.get('page')
    try:
        trips = paginator.page(page)
    except PageNotAnInteger:
# If page is not an integer deliver the first page
        trips = paginator.page(1)
    except EmptyPage:
# If page is out of range deliver last page of results
        trips = paginator.page(paginator.num_pages)

    context = {'page': page, 'trips': trips}
    return render(request, 'trips.html', context)


def about(request):
    return render(request, 'about.html', {})


def portfocategory(request, slug_text):
    # Obtener la categoria segun el slug
    category = Category.objects.filter(slug=slug_text)
    # Obtenemos los objetos de esa categoria. 
    # Lo ordenamos por Warning del Paginator
    Object_list = Object.objects.filter(category__slug=slug_text).order_by('id')
#Paginacion
    paginator = Paginator(Object_list, per_page=10)
    page = request.GET.get('page')
    try:
        objetos = paginator.page(page)
    except PageNotAnInteger:
# If page is not an integer deliver the first page
        objetos = paginator.page(1)
    except EmptyPage:
# If page is out of range deliver last page of results
        objetos = paginator.page(paginator.num_pages)

    return render(request, 'portfocategory.html', {'objetos': objetos, 'category': category})


def portfolio(request):
    querycat = Category.objects.all()
    queryobj = Object.objects.all()
    return render(request, 'portfolio.html', {'categorias': querycat, 'objects': queryobj})


def detail(request, pk):
    queryobj = Object.objects.filter(pk=pk)
    return render(request, 'detail.html', {'objeto': queryobj})
