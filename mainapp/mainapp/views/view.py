#!/usr/bin/env python
from django.shortcuts import render
from ..models import MyShop, Type, Category, SubCategory


def index(request):
    myshops = MyShop.objects.all()
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys}
    return render(request, 'mainapp/index.html', context)


def base(request):
    myshops = MyShop.objects.all()
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys}
    return render(request, 'mainapp/basic.html', context)


def about_us(request):
    myshops = MyShop.objects.all()
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys}
    return render(request, 'mainapp/about.html', context)


def by_type(request, type_id):
    myshops = MyShop.objects.filter(type=type_id)
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    current_type = Type.objects.get(pk=type_id)
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys,
               'current_type': current_type}
    return render(request, 'mainapp/type.html', context)


def by_category(request, category_id):
    myshops = MyShop.objects.filter(category=category_id)
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys,
               'current_category': current_category}
    return render(request, 'mainapp/category.html', context)


def by_sub_category(request, sub_category_id):
    myshops = MyShop.objects.filter(sub_category=sub_category_id)
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    current_sub_category = SubCategory.objects.get(pk=sub_category_id)
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys,
               'current_sub_category': current_sub_category}
    return render(request, 'mainapp/sub_category.html', context)


def partners(request):
    myshops = MyShop.objects.all()
    types = Type.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    context = {'myshops': myshops, 'types': types, 'categorys': categorys, 'sub_categorys': sub_categorys}
    return render(request, 'mainapp/Partners.html', context)

