from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from apps.models import Car, Brand
from apps.filters import CarFilter
from apps.forms import RegisterUserForm
from apps.decorators import required_login_custom


def main(request):
    search = request.GET.get('search', None)
    if search:
        cars = Car.objects.filter(model__icontains=search)
        return render(request, 'search_page.html', { 'cars_list': cars })
    else:
        cars = Car.objects.all().order_by('-id')

    filter_set = CarFilter(request.GET, queryset=cars)

    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 2)
    paginator = Paginator(filter_set.qs, limit)
    cars = paginator.get_page(offset)
    return render(request, 'index.html', {'cars_list': cars, 'filter': filter_set})


def detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'detail.html', {'car': car, })


def cars_by_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    cars = Car.objects.filter(brand=brand)
    return render(request, 'search_page.html', { 'cars_list': cars, })


def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            return render(request, 'auth/login.html', {'message': 'Enter required fields'})
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'auth/login.html', {'message': 'The user is not found or invalid password'})
    return render(request, 'auth/login.html')


class RegisterUser(CreateView,):

    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_context_data(title='Registration')
        return dict(list(context.items()))


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'auth/profile.html')
    return redirect('/')
