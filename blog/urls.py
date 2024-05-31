from django.urls import path, include
from .views import *

app_name = "blog"

urlpatterns = [
    path("list/", TodoList.as_view(), name="todo_list"),
    path("<int:pk>/create/", TodoCreate.as_view(), name="todo_create"),
    path("<int:pk>/", TodoDetail.as_view(), name="todo_detail"),
    path("<int:pk>/update/", TodoUpdate.as_view(), name="todo_update"),
    path("<int:pk>/delete/", TodoDelete.as_view(), name="todo_delete")
]
