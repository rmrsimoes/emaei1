from django.urls import path

from .views import index, contacto, produto

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('produto/', produto, name='produto'),
]
