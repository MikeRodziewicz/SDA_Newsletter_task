"""newslet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from website import views as website_views
from users import views as user_views
from surveys import views as surveys_views
from django.conf import settings
from django.conf.urls.static import static
from surveys.models import Company, Product, Survey

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Survey)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('users.urls')),
    path('', include('surveys.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
