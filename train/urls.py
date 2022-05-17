from django.urls import path
from . import views

app_name = 'train'

urlpatterns = [
    path('train/edit/<int:train_id>', views.train_view, name='train-view'),
    path('train/delete/<int:train_id>', views.delete_train_view, name='delete-train-view'),
    path('train/create/', views.create_train_view, name='create-train-view'),
    path('', views.index, name='main-view'),
]
