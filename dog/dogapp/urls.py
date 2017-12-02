from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView),
    url(r'^about_us/', views.AboutView),
    url(r'^stats/', views.StatsView),
    url(r'^shelter/', views.ShelterView),
]
