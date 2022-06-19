from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrademarkHome.as_view(), name='trademark-home'),
    path('add/', views.AddTrademarkView.as_view(), name='add-trademark'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks-trademark'),
    path('<slug:slug>/', views.TrademarkDetailView.as_view(), name='trademark-detail'),
    # path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file-industrial-design'),
    # path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file-industrial-design'),
    path('delete-industrial-design/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole-trademark'),
    path('search', views.SearchView.as_view(), name='search-trademark')
]
