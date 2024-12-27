from django.urls import path
from . import views

urlpatterns = [
    path('main/', view = views.BookListView.as_view(), name = 'main'),
    path('create/', view = views.CreateBook.as_view(), name = 'create'),
    path('update/<int:pk>', view = views.BookUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', view = views.DeleteBook.as_view(), name = 'delete'),
]
