from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mail import views

urlpatterns = [
	path('', views.Home, name="home"),
	# path('', views.Home.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)