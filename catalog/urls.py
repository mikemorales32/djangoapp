from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
urlpatterns += [
    path('', views.index, name='index'),
    # path('author/', views.AuthorBookList.as_view(), name = 'author'),
    path('author/<int:pk>', views.AuthorBookList.as_view(), name='author-book-list'),
    path('author/<int:pk>', views.AuthorBookDetailList.as_view(), name='author-book-list')
]
