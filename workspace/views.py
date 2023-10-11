from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import JsonResponse, HttpResponseForbidden

from workspace.forms import CarForm
from apps.models import Car, Brand
from workspace.decorators import required_login_custom


@required_login_custom
def workspace(request):
    cars = Car.objects.filter(owner=request.user)
    brand = request.GET.get('brand', None)
    if brand:
        brand = get_object_or_404(Brand, id=int(brand))
        cars = cars.filter(brands=brand)
    search = request.GET.get('search1', None)
    message = None
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
        message = f'found news by title {search}'
    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 2)
    paginator = Paginator(cars, limit)
    cars = paginator.get_page(offset)
    brands = Brand.objects.all().order_by('name')
    return render(request, 'workspace/index.html', {'cars_list': cars, 'brands': brands,})


@required_login_custom
def filter_cars_by_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    brands = Brand.objects.all().order_by('name')
    if brand:
        car = Car.objects.filter(brand=brand).order_by('-id')
        return render(request, 'workspace/index.html', {'cars_list': car, 'brands': brands, })
    return redirect('/')


@required_login_custom
def detail_car(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'detail.html', {'car': car,})


@required_login_custom
def add_car(request,):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('/workspace/')
    return render(request, 'workspace/add_car.html', {'form': form})


def update_car(request, id):
    car = get_object_or_404(Car, id=id)
    form = CarForm(instance=car)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect(f'/workspace/')
    return render(request, 'workspace/update_car.html', {
        'form': form,
        'car': car,
    })


@required_login_custom
def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return redirect('/workspace/')


@required_login_custom
def list_of_brands(request):
    brands = Brand.objects.all().order_by('-id')
    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(brands, limit)
    brands = paginator.get_page(offset)
    return render(request, 'workspace/brands.html', {'brands': brands})


def create_brand(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name', None)
            if name is None or name == '':
                return render(request, 'workspace/create_brand.html', {'message': 'Name is required'})
            brand = Brand.objects.create(name=name)
            return redirect('/workspace/brands/')

        return render(request, 'workspace/create_brand.html')
    return redirect('/')


def update_brand(request, id):
    if request.user.is_authenticated:
        brand = get_object_or_404(Brand, id=id)
        if request.method == 'POST':
            name = request.POST.get('name', None)
            if name is None or name == '':
                return render(request, 'workspace/update_brand.html', {
                    'message': 'Name is required',
                    'brand': brand,
                })

            brand.name = name
            brand.save()
            return redirect('/workspace/brands/')

        return render(request, 'workspace/update_brand.html', {'brand': brand})
    return redirect('/')


def delete_brand(request, id):
    if request.user.is_authenticated:
        brand = get_object_or_404(Brand, id=id)
        brand.delete()
        return redirect('/workspace/brands/')
    return redirect('/')