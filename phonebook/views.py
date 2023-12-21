from django.shortcuts import render, redirect, get_object_or_404
from .models import Main, FirstName, LastName, Patronymic, Street
from django.http import HttpResponse
from .forms import MainForm, FirstNameForm, LastNameForm, PatronymicForm, StreetForm, DeleteForm, MainEditForm



def index(request):
    return render(request, 'phonebook/index.html')

def main_list(request):
    main_list = Main.objects.all()
    return render(request, 'phonebook/main_list.html', {'main_list': main_list})

def first_name_list(request):
    first_name_list = FirstName.objects.all()
    return render (request, 'phonebook/first_name.html', {'first_name_list': first_name_list})

def last_name_list(request):
    last_name_list = LastName.objects.all()
    return render (request, 'phonebook/last_name.html', {'last_name_list': last_name_list})

def patronymic_list(request):
    patronymic_list = Patronymic.objects.all()
    return render (request, 'phonebook/patronymic.html', {'patronymic_list': patronymic_list})

def street_list(request):
    street_list = Street.objects.all()
    return render (request, 'phonebook/street.html', {'street_list': street_list})



def search_by_phone(request):
    phone_number = request.GET.get('phone_number', '')
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    patronymic = request.GET.get('patronymic', '')
    street = request.GET.get('street', '')
    house = request.GET.get('house', '')
    building = request.GET.get('building', '')
    apartment = request.GET.get('apartment', '')
    phone = request.GET.get('phone', '')


    if not any([phone_number, first_name, last_name, patronymic, street, house, building, apartment, phone]):
        return render(request, 'phonebook/search/search_byphone.html')


    # Start with an empty queryset
    results = Main.objects.all()

    # Добавляем фильтры только для непустых полей
    if phone_number:
        results = results.filter(phone=phone_number)
    if first_name:
        results = results.filter(first_name__value=first_name)
    if last_name:
        results = results.filter(last_name__value=last_name)
    if patronymic:
        results = results.filter(patronymic__value=patronymic)
    if street:
        results = results.filter(street__value=street)
    if house:
        results = results.filter(house__icontains=house)
    if building:
        results = results.filter(building__icontains=building)
    if apartment:
        results = results.filter(apartment__icontains=apartment)

    return render(request, 'phonebook/search/search_byphone_results.html', {
        'results': results,
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'patronymic': patronymic,
        'street': street,
        'house': house,
        'building': building,
        'apartment': apartment,
        'phone': phone,
    })
def search_byfirstname(request):
    if 'first_name' in request.GET:
        first_name = request.GET['first_name']
        results = FirstName.objects.filter(value=first_name)
        return render(request, 'phonebook/search/search_byfirstname_results.html', {'results': results, 'first_name': first_name})

    return render(request, 'phonebook/search/search_byfirstname.html')

def search_bylastname(request):
    if 'last_name' in request.GET:
        last_name = request.GET['last_name']
        results = LastName.objects.filter(value=last_name)
        return render(request, 'phonebook/search/search_bylastname_results.html', {'results': results, 'last_name': last_name})

    return render(request, 'phonebook/search/search_bylastname.html')

def search_bypatronymic(request):
    if 'patronymic' in request.GET:
        patronymic = request.GET['patronymic']
        results = Patronymic.objects.filter(value=patronymic)
        return render(request, 'phonebook/search/search_bypatronymic_results.html', {'results': results, 'patronymic': patronymic})

    return render(request, 'phonebook/search/search_bypatronymic.html')

def search_bystreet(request):
    if 'street' in request.GET:
        street = request.GET['street']
        results = Street.objects.filter(value=street)
        return render(request, 'phonebook/search/search_bystreet_results.html', {'results': results, 'street': street})

    return render(request, 'phonebook/search/search_bystreet.html')


def add_data(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_list')  
    else:
        form = MainForm()

    return render(request, 'phonebook/add/add_data.html', {'form': form})

def add_data_firstname(request):
    if request.method == 'POST':
        form = FirstNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_name_list')  
    else:
        form = FirstNameForm()

    return render(request, 'phonebook/add/add_data_firstname.html', {'form': form})

def add_data_lastname(request):
    if request.method == 'POST':
        form = LastNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('last_name_list')  
    else:
        form = LastNameForm()

    return render(request, 'phonebook/add/add_data_lastname.html', {'form': form})

def add_data_patronymic(request):
    if request.method == 'POST':
        form = PatronymicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patronymic_list')  
    else:
        form = PatronymicForm()

    return render(request, 'phonebook/add/add_data_patronymic.html', {'form': form})

def add_data_street(request):
    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('street_list')  
    else:
        form = StreetForm()

    return render(request, 'phonebook/add/add_data_street.html', {'form': form})

# def delete_byphone_main(request):
#     if request.method == 'POST':
#         form = DeleteForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data['data']
          
#             Main.objects.filter(phone=data).delete()
#             return redirect('main_list')
#     else:
#         form = DeleteForm()

#     return render(request, 'phonebook/delete/delete_byphone_mainlist.html', {'form': form})
def delete_byphone_main(request):
    phone_number = request.GET.get('phone_number', '')
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    patronymic = request.GET.get('patronymic', '')
    street = request.GET.get('street', '')
    house = request.GET.get('house', '')
    building = request.GET.get('building', '')
    apartment = request.GET.get('apartment', '')

    if not any([phone_number, first_name, last_name, patronymic, street, house, building, apartment]):
        return render(request, 'phonebook/delete/delete_byphone_mainlist.html')

    if phone_number:
        Main.objects.filter(phone=phone_number).delete()
    if first_name:
        Main.objects.filter(first_name=first_name).delete()
    if last_name:
        Main.objects.filter(last_name=last_name).delete()
    if patronymic:
        Main.objects.filter(patronymic=patronymic).delete()
    if street:
        Main.objects.filter(street=street).delete()
    if house:
        Main.objects.filter(house__icontains=house).delete()
    if building:
        Main.objects.filter(building__icontains=building).delete()
    if apartment:
       Main.objects.filter(apartment__icontains=apartment).delete()

    return redirect('main_list')


def delete_byname_firstname(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
           
            main_instances = Main.objects.filter(first_name__value=data)
            for main_instance in main_instances:
                FirstName.objects.filter(id=main_instance.first_name.id).delete()
                LastName.objects.filter(id=main_instance.last_name.id).delete()
                Patronymic.objects.filter(id=main_instance.patronymic.id).delete()
                Street.objects.filter(id=main_instance.street.id).delete()
                
            return redirect('first_name_list')  
            
    else:
        form = DeleteForm()

    return render(request, 'phonebook/delete/delete_byname_firstname.html', {'form': form})

def delete_byname_lastname(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
           
            main_instances = Main.objects.filter(last_name__value=data)
            for main_instance in main_instances:
                FirstName.objects.filter(id=main_instance.first_name.id).delete()
                LastName.objects.filter(id=main_instance.last_name.id).delete()
                Patronymic.objects.filter(id=main_instance.patronymic.id).delete()
                Street.objects.filter(id=main_instance.street.id).delete()
                
            return redirect('last_name_list')  
            
    else:
        form = DeleteForm()

    return render(request, 'phonebook/delete/delete_bylastname.html', {'form': form})

def delete_byname_patronymic(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
           
            main_instances = Main.objects.filter(patronymic__value=data)

            for main_instance in main_instances:
                FirstName.objects.filter(id=main_instance.first_name.id).delete()
                LastName.objects.filter(id=main_instance.last_name.id).delete()
                Patronymic.objects.filter(id=main_instance.patronymic.id).delete()
                Street.objects.filter(id=main_instance.street.id).delete()
                    
            return redirect('patronymic_list')  
            
    else:
        form = DeleteForm()

    return render(request, 'phonebook/delete/delete_bypatronymic.html', {'form': form})

def delete_byname_street(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
           
            main_instances = Main.objects.filter(street__value=data)

            for main_instance in main_instances:
                FirstName.objects.filter(id=main_instance.first_name.id).delete()
                LastName.objects.filter(id=main_instance.last_name.id).delete()
                Patronymic.objects.filter(id=main_instance.patronymic.id).delete()
                Street.objects.filter(id=main_instance.street.id).delete()
                    
            return redirect('street_list')  
            
    else:
        form = DeleteForm()

    return render(request, 'phonebook/delete/delete_bystreet.html', {'form': form})


def edit_main(request, main_id):
    main_instance = get_object_or_404(Main, id=main_id)

    if request.method == 'POST':
        form = MainEditForm(request.POST, instance=main_instance)
        if form.is_valid():
            form.save()
            return redirect('main_list')
    else:
        form = MainEditForm(instance=main_instance)

    return render(request, 'phonebook/edit/edit_main.html', {'form': form, 'main_instance': main_instance})


def edit_firstname(request, main_id):
    main_instance = get_object_or_404(FirstName, id=main_id)

    if request.method == 'POST':
        form = FirstNameForm(request.POST, instance=main_instance)
        if form.is_valid():
            form.save()
            return redirect('first_name_list')
    else:
        form = FirstNameForm(instance=main_instance)

    return render(request, 'phonebook/edit/edit_firstname.html', {'form': form, 'main_instance': main_instance})


def edit_lastname(request, main_id):
    main_instance = get_object_or_404(LastName, id=main_id)

    if request.method == 'POST':
        form = LastNameForm(request.POST, instance=main_instance)
        if form.is_valid():
            form.save()
            return redirect('last_name_list')
    else:
        form = LastNameForm(instance=main_instance)

    return render(request, 'phonebook/edit/edit_lastname.html', {'form': form, 'main_instance': main_instance})

def edit_patronymic(request, main_id):
    main_instance = get_object_or_404(Patronymic, id=main_id)

    if request.method == 'POST':
        form = PatronymicForm(request.POST, instance=main_instance)
        if form.is_valid():
            form.save()
            return redirect('patronymic_list')
    else:
        form = PatronymicForm(instance=main_instance)

    return render(request, 'phonebook/edit/edit_patronymic.html', {'form': form, 'main_instance': main_instance})

def edit_street(request, main_id):
    main_instance = get_object_or_404(Street, id=main_id)

    if request.method == 'POST':
        form = StreetForm(request.POST, instance=main_instance)
        if form.is_valid():
            form.save()
            return redirect('street_list')
    else:
        form = StreetForm(instance=main_instance)

    return render(request, 'phonebook/edit/edit_street.html', {'form': form, 'main_instance': main_instance})