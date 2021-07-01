from django.urls import path
from .views import *

app_name = 'categories'

urlpatterns = [
    path('',CategoryListView.as_view(),name = 'category-list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name = 'category-detail'),
    path('<int:pk>/lead-category-update/', LeadCategoryUpdateView.as_view(),name = 'lead-category-update'),
]

