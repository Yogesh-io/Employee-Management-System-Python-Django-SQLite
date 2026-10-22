from django.urls import path
from .views import *

urlpatterns = [
    path('add_emp/', add_emp , name='add_emp'),
    path('view_emp/', view_emp , name="view_emp"),
    path('update_emp/<int:id>/', update_emp , name="update_emp"),
    path('delete_emp/<int:id>/', delete_emp , name="delete_emp"),
    path('',  user_login , name="user_login"),
    path('logout/', user_logout, name='user_logout')
]