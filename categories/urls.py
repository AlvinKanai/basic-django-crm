from django.urls import path
from .views import *

app_name = 'categories'

urlpatterns = [
    path('',CategoryListView.as_view(),name = 'category-list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name = 'category-detail'),
    path('<int:pk>/lead-category-update/', LeadCategoryUpdateView.as_view(),name = 'lead-category-update'),
    path('create/',CategoryCreateView.as_view(), name = 'category-create'),
    path('<int:pk>/update/',CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/delete/',CategoryDeleteView.as_view(), name='category-delete'),
]

