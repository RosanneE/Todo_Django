from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('add_list/', views.add_list, name='add_list'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('add_list/add_listrecord/', views.add_listrecord, name='add_listrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
    path('update/<int:id>', views.update, name='update'),
    path('update_list/<int:id>', views.update_list, name='update_list'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
     path('update/update_listrecord/<int:id>', views.update_listrecord, name='update_listrecord'),
]

