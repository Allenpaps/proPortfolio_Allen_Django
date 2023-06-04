from django.contrib import admin
from django.urls import path
from mainDashApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.baseView, name='baseView'),
    path('aboutMe/', views.aboutView, name='about'),
    path('history/', views.historyView, name='history'),
    path('contacts/', views.contactView, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
