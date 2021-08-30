"""coursovaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"AdminMain/",views.AdminMain),
    path(r"AddCinema/",views.AddCinemaTheater),
    path(r"AddPerson/", views.AddPerson),
    path(r"AddSeans/", views.AddSeans),
    path(r"AddFilm/", views.AddFilm),
    path(r"DeleteCinema/", views.DeleteCinema),
    path(r"DeleteFilm/", views.DeleteFilm),
    path(r"DeleteSeans/", views.DeleteSeans),
    path(r"DeletePerson/", views.DeletePerson),
    path(r"AddInFilm/", views.AddInFilm),
    path(r"DeleteFromFilm/", views.DeleteFromFilm),
    path(r'', views.index),
    path(r"Registration/", views.Registration),
    path(r"ChangeStatus/", views.ChangeStatus),
    path(r"CinemaList/", views.CinemaList),
    path(r"CinemaTemplate/", views.CinemaTemplate),
    path(r"FilmList/", views.FilmList),
    path(r"FilmTemplate/", views.FilmTemplate),
    path(r"PersonList/", views.PersonList),
    path(r"PersonTemplate/", views.PersonTemplate),
    path(r"autorization/",views.autorization),
    path(r"exit/",views.exit)
]
