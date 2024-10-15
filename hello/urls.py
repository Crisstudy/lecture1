from django.urls import path #caminho da importação django

from . import views
#isto é a variável
urlpatterns = [
    path("", views.index, name="index"), #esta é a url e seu caminho para renderização c/ nome
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
]