from django.urls import path
from django.conf import settings
from django.conf .urls.static import static
from . import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('header/',views.header,name='header'),
    path('customer/',views.customer,name='customer'),
    path("rental/",views.rental, name="rental"),
    path("",views.home, name="home"),
    path("Register/",views.register, name="Register"),
    path("contact/",views.contact, name="contact"),
    path("about/",views.about, name="about"),
    path("login/",views.login, name="login"),
    path("display/",views.display, name="display"),
    path("search/",views.search, name="search"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)

