from django.urls import path
from .views import index, produto, contato, cliente, mostra_cliente

urlpatterns =[
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('contato/', contato, name='contato'),
    path('cliente/', cliente, name='cliente'),
    path('mostra_cliente/', mostra_cliente, name='mostra_cliente')
]