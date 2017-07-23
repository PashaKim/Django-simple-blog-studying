"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import article
from django.conf.urls import url, include
from django.contrib import admin
from article.views import basic_one, template_two, template_three



admin.autodiscover()

urlpatterns = [url(r'^admin/',admin.site.urls),
               url(r'^basicview/1', article.views.basic_one),
               url(r'^basicview/2', article.views.template_two),
               url(r'^basicview/3', article.views.template_three),
               url(r'^', include('article.urls')),
]