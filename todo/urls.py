from django.urls import include, path
from .views import TodoCreate, TodoList, TodoDetail, TodoUpdate, TodoDelete


urlpatterns = [
    path('create/', TodoCreate.as_view(), name='create-todo'),
    path('', TodoList.as_view()),
    path('<int:pk>/', TodoDetail.as_view(), name='retrieve-todo'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update-todo'),
    # path('delete/<int:pk>/', TodoDelete.as_view(), name='delete-todo')
]