from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView),
    url(r'^home/', views.HomeView),
    url(r'^matching/', views.MatchingView),
    url(r'^about_us/', views.AboutView),
    url(r'^stats/', views.StatsView),
    url(r'^shelter/', views.ShelterView),
    url(r'^membership/', views.MembershipView),
    url(r'^login', views.LoginView),
    url(r'^validate_username/', views.validate_username),
    url(r'^result_dog/', views.result_dog),
]
