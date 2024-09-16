from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')

    rentals = None
    group = None

    if request.user.is_superuser:
        rentals = ForRent.objects.all()
    else:
        groups = request.user.user_groups.all()
        if groups:
            leader_groups = groups.filter(leader=request.user)
            if leader_groups:
                rentals = ForRent.objects.filter(group__in=leader_groups)
            else:
                rentals = ForRent.objects.filter(group__in=groups)
        else:
            rentals = ForRent.objects.none()

    context = {
        'rentals': rentals,
        'group': group,
    }
    return render(request, 'index.html', context)
    
def addForRent(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    else:
        if request.method == 'POST':
            form = ForRentForm(request.POST)
            if form.is_valid():
                new_rent = ForRent()
                new_rent.author = request.user
                try:
                    new_rent.group = request.user.user_groups.first()
                except:
                    pass
                new_rent.agent = f"{request.user.first_name} {request.user.last_name}"
                new_rent.mobile = form.cleaned_data['mobile']
                new_rent.myhomelink = form.cleaned_data['myhomelink']
                new_rent.myhomeid = form.cleaned_data['myhomeid']
                new_rent.sslink = form.cleaned_data['sslink']
                new_rent.ssid = form.cleaned_data['ssid']
                new_rent.area = form.cleaned_data['area']
                new_rent.price = form.cleaned_data['price']
                new_rent.address = form.cleaned_data['address']
                new_rent.limitations = form.cleaned_data['limitations']
                new_rent.save()
                return redirect('index')
        else:
            form = ForRentForm()
        context = {
            'form': form
        }
        return render(request, 'addforrent.html', context)

def deleteForRent(request, rent_id):
    if not request.user.is_authenticated:
        return redirect('loginUser')

    rent = get_object_or_404(ForRent, pk=rent_id)

    if request.user.is_superuser:
        rent.delete()
        return redirect('index')

    elif request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("Staff users cannot delete rents.")
    elif rent.author == request.user:
        rent.delete()
        return redirect('index')

    elif request.user.has_perm('deleteRent', rent.group):
        rent.delete()
        return redirect('index')
    else:
        return HttpResponseForbidden("You don't have permission to delete this rent.")

def forSale(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')

    sales = None
    group = None

    if request.user.is_superuser:
        sales = ForSale.objects.all()
    else:
        groups = request.user.user_groups.all()
        if groups:
            leader_groups = groups.filter(leader=request.user)
            if leader_groups:
                sales = ForSale.objects.filter(group__in=leader_groups)
            else:
                sales = ForSale.objects.filter(group__in=groups)
        else:
            sales = ForSale.objects.none()

    context = {
        'sales': sales,
        'group': group,
    }
    return render(request, 'forsale.html', context)
    
def addForSale(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    else:
        if request.method == 'POST':
            form = ForSaleForm(request.POST)
            if form.is_valid():
                new_sale = ForSale()
                new_sale.author = request.user
                try:
                    new_sale.group = request.user.user_groups.first()
                except:
                    pass
                new_sale.agent = f"{request.user.first_name} {request.user.last_name}"
                new_sale.mobile = form.cleaned_data['mobile']
                new_sale.myhomelink = form.cleaned_data['myhomelink']
                new_sale.myhomeid = form.cleaned_data['myhomeid']
                new_sale.sslink = form.cleaned_data['sslink']
                new_sale.ssid = form.cleaned_data['ssid']
                new_sale.area = form.cleaned_data['area']
                new_sale.price = form.cleaned_data['price']
                new_sale.percentage = form.cleaned_data['percentage']
                new_sale.address = form.cleaned_data['address']
                new_sale.save()
                return redirect('forSale')
        else:
            form = ForSaleForm()
        context = {
            'form': form
        }
        return render(request, 'addforsale.html', context)

def deleteForSale(request, sale_id):
    if not request.user.is_authenticated:
        return redirect('loginUser')

    sale = get_object_or_404(ForSale, pk=sale_id)

    if request.user.is_superuser:
        sale.delete()
        return redirect('forSale')

    elif request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("Staff users cannot delete sales.")
    elif sale.author == request.user:
        sale.delete()
        return redirect('forSale')

    elif request.user.has_perm('deleteSale', sale.group):
        sale.delete()
        return redirect('forSale')
    else:
        return HttpResponseForbidden("You don't have permission to delete this sale.")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('forSale')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('forSale')
                else:
                    messages.error(request, 'Username or password is wrong!')
        else:
            form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')