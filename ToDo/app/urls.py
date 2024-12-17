from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('one/<int:pk>',views.update, name = 'update'),
    path('add',views.create, name = 'create'),
    path('three',views.hist, name = 'hist'),
    path('four/<int:pk1>',views.delete, name = 'delete'),
    path('two/<int:pk2>',views.pdelete, name = 'pdelete'),
]