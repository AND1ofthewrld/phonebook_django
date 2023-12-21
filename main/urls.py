"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from phonebook.views import main_list, edit_main,edit_firstname,edit_street, edit_patronymic, edit_lastname, index, first_name_list, last_name_list, delete_byname_street, street_list, patronymic_list, search_by_phone, search_byfirstname, search_bylastname, search_bypatronymic, search_bystreet, add_data, add_data_firstname, add_data_lastname, add_data_patronymic, add_data_street, delete_byphone_main, delete_byname_firstname,delete_byname_lastname, delete_byname_patronymic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('main-list/', main_list, name='main_list'),
    path('first_name_list/', first_name_list, name='first_name_list'),
    path('last_name_list/', last_name_list, name='last_name_list'),
    path('patronymic_list/', patronymic_list, name='patronymic_list'),
    path('street_list/', street_list, name='street_list'),

    path('search-by-phone/', search_by_phone, name='search_by_phone'),
    path('search-by-firstname/', search_byfirstname, name='search_byfirstname'),
    path('search-by-lastname/', search_bylastname, name='search_bylastname'),
    path('search-by-patronymic/', search_bypatronymic, name='search_bypatronymic'),
    path('search-by-street/', search_bystreet, name='search_bystreet'),

    path('add-data/', add_data, name='add_data'),
    path('add-data-firstname/', add_data_firstname, name='add_data_firstname'),
    path('add-data-lastname/', add_data_lastname, name='add_data_lastname'),
    path('add-data-patronymic/', add_data_patronymic, name='add_data_patronymic'),
    path('add-data-street/', add_data_street, name='add_data_street'),

    path('delete_by_phone/', delete_byphone_main, name='delete_by_phone'),
    path('delete_by_firstname/', delete_byname_firstname, name='delete_byfirstname'),
    path('delete_by_lastname/', delete_byname_lastname, name='delete_bylastname'),
    path('delete_by_patronymic/', delete_byname_patronymic, name='delete_bypatronymic'),
    path('delete_by_street/', delete_byname_street, name='delete_bystreet'),

    path('edit_main/<int:main_id>/', edit_main, name='edit_main'),
    path('edit_firstname/<int:main_id>/', edit_firstname, name='edit_firstname'),
    path('edit_lastname/<int:main_id>/', edit_lastname, name='edit_lastname'),
    path('edit_patronymic/<int:main_id>/', edit_patronymic, name='edit_patronymic'),
    path('edit_street/<int:main_id>/', edit_street, name='edit_street'),




]
