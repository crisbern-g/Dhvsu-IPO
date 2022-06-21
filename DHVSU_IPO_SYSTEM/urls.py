"""DHVSU_IPO_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Site.urls')),

    #Copyright
    path('copyright/', include('Copyright.urls')),

    #Patent
    path('patent/', include('Patent.urls')),

    #Utility Model
    path('utility-model/', include('Utility_Model.urls')),

    #Industrial Design
    path('industrial-design/', include('Industrial_Design.urls')),

    #Trademark
    path('trademark/', include('Trademark.urls')),

    #ISSN
    path('issn/', include('ISSN.urls')),

    # Authentication
    path('authentication/', include('Authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
