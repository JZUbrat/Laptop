from django.urls import path
from .views import LaptopAPIview, LaptopAPIupdate, LaptopAPIcreate, LaptopAPIdelete

urlpatterns = [
    path('laptop_list', LaptopAPIview.as_view(),name = 'laptop-list'),
    path('laptop_update', LaptopAPIupdate.as_view(), name = 'laptop-detail'),
    path('laptop_create', LaptopAPIcreate.as_view(), name = 'laptop-create'),
    path('laptop_delete', LaptopAPIdelete.as_view(), name = 'laptop-delete')
]