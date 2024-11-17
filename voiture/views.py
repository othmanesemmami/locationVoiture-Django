from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Car


def signup_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not username or not password or not confirm_password:
            error_message = "Tous les champs doivent être remplis."
        elif password != confirm_password:
            error_message = "Les mots de passe ne correspondent pas."
        elif User.objects.filter(username=username).exists():
            error_message = "Le nom d'utilisateur est déjà pris."
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
            except:
                error_message = "Erreur lors de la création du compte."

    return render(request, 'signup.html', {'error_message': error_message})


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_menu')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'auth.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main_menu_view(request):
    return render(request, 'main_menu.html')

@login_required
def create_car_view(request):
    error_message = None  # Initialize error_message to None

    if request.method == 'POST':
        matricule = request.POST['matricule']
        marque = request.POST['marque']
        kilometrage = request.POST['kilometrage']
        prix_jours = request.POST['prix_jours']
        disponibilite = request.POST['disponibilite']

        # Check for empty fields
        if not matricule or not marque or not kilometrage or not prix_jours or not disponibilite:
            error_message = "Tous les champs sont obligatoires."

        # Check for positive values
        elif int(kilometrage) < 0 or int(prix_jours) < 0:
            error_message = "Kilométrage et Prix/Jour doivent être positifs."

        # Check for unique matricule
        elif Car.objects.filter(matricule=matricule).exists():
            error_message = "Le matricule doit être unique."

        if error_message:
            return render(request, 'car_form.html', {'error_message': error_message})

        new_car = Car(matricule=matricule, marque=marque, kilometrage=kilometrage, prix_jours=prix_jours, disponibilite=disponibilite)
        new_car.save()
        return redirect('car_list')

    return render(request, 'car_form.html')

@login_required
def car_list_view(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(marque__icontains=query) | Car.objects.filter(matricule__icontains=query)
    else:
        cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

@login_required
def update_car_view(request, car_id):
    
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.matricule = request.POST['matricule']
        car.marque = request.POST['marque']
        car.kilometrage = request.POST['kilometrage']
        car.prix_jours = request.POST['prix_jours']
        car.disponibilite = request.POST['disponibilite']
        car.save()
        return redirect('car_list')
    return render(request, 'car_form.html', {'car': car})

@login_required
def delete_car_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})

@login_required
def delete_all_cars_view(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        return redirect('car_list')
    return render(request, 'confirm_delete_all.html')
