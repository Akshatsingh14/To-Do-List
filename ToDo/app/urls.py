from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in, name = 'log_in'),
    path('1',views.index, name = 'home'),
    path('2',views.register, name = 'register'),
    path('one/<int:pk>',views.update, name = 'update'),
    path('add',views.create, name = 'create'),
    path('three',views.hist, name = 'hist'),
    path('four/<int:pk1>',views.delete, name = 'delete'),
    path('two/<int:pk2>',views.pdelete, name = 'pdelete'),
    path('3',views.log_out, name = 'log_out'),
]