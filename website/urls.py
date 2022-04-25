from django.urls import path
from .views import home, about, portfolio,  portfocategory, detail, trips, equipments, published, contact, links
# from django.views.generic.base import RedirectView
# from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('links/', links, name="links"),
    path('contact/', contact, name="contact"),
    path('equipment/', equipments, name="equipment"),
    path('published/', published, name="published"),
    path('trips/', trips, name="trips"),
    path('portfolio/', portfolio, name="portfolio"),
    path('detail/<int:pk>', detail, name="detail"),
    path('category/<slug:slug_text>', portfocategory, name="category"),
]
