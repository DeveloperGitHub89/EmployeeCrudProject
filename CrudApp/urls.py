from django.urls import path
from . import views

urlpatterns = [
    path('',views.openIndexPage),
    path('employee-form',views.openEmployeeForm),
    path('save-employee',views.saveEmployee),
    path('employees-list',views.openEmployeesList),
    path('delete/<int:id>',views.deleteEmployee),
    path('edit/<int:id>',views.openEditForm),
    path('update/<int:id>',views.updateEmployee),
]