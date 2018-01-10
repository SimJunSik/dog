from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

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
    url(r'^result_dog/$', views.result_dog),
    url(r'^register_marker/', views.register_marker),
    url(r'^register_dog/', views.register_dog),
    url(r'^delete_marker/', views.delete_marker),
    url(r'^change_marker/', views.change_marker),
    url(r'^notice/', views.NoticeView),
    url(r'^take_dog/', views.TakedogView),
    url(r'^take_register_dog/', views.take_register_dog),
    url(r'^getaddr/', views.GetAddr),
    url(r'^updateData/', views.UpdateData),
    url(r'^updateData2/', views.UpdateData2),
    url(r'^show_info/', views.show_info),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
