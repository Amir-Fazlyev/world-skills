from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete')
]
