"""mainapp URL Configuration

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
from .views import index, base, about_us, partners, by_type, by_category, by_sub_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('mainapp/index', index, name='index'),
    path('mainapp/base', base, name='base'),
    path('mainapp/about_us', about_us, name='about us'),
    path('mainapp/partners', partners, name='partners'),
    path('mainapp/category/<int:category_id>', by_category, name='by_category'),
    path('mainapp/sub_category/<int:sub_category_id>', by_sub_category, name='by_sub_category'),
    path('mainapp/type/<int:type_id>', by_type, name='by_type'),

]
