from django.contrib import admin
from django.urls import path
from helloworld import views
app_name = 'helloworld'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.bookDetail,
         name='bookDetail'),
    path('add/', views.add_book, name="add"),
    path('update/<int:id>/', views.update_book, name="update"),
    path('delete/<int:id>/', views.delete_book, name="delete")
]
