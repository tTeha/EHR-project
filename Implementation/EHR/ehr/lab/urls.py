from django.conf.urls import url
from django.urls import path

from lab import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lab'

urlpatterns = [
    path('', views.labLogin, name='labLogin'),
    path('labPatientLogin/', views.labPatientLogin, name='labPatientLogin'),
    path('labPatientLogin/analyticsAndRays', views.labPatientLogin, name='labPatientLogin'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)