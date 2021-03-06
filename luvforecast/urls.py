"""luvforecast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import feedpage.views
import accounts.views
from django.conf.urls import include
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.login, name='login'),
    path('home/', include('feedpage.urls')), #이름 설정 논의해보기
    path('accounts/', include('accounts.urls')),
]
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)