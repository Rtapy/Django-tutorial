from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='productsList'),
    path('<int:product>', views.dynamic_chis_num),
    path('<str:product>', views.dynamic_chis, name='products')
]

