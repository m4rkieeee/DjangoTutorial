from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('employee/', views.index, name = 'employee'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name = 'update'),
    path('update/updateData/<int:id>', views.updateData, name = 'updateData'),
    path('blog/<int:id>', views.detailsPage, name = 'blog'),

]