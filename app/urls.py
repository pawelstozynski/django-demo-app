from django.urls import path

from .views import article_views, todo_views

urlpatterns = [
    path('', article_views.index, name='index'),
    path('article/<int:article_id>/', article_views.article_show, name='article-show'),
    path('article/create/', article_views.article_create, name='article-create'),
    path('article/<int:article_id>/edit/', article_views.article_edit, name='article-edit'),
    path('article/<int:article_id>/delete/', article_views.article_delete, name='article-delete'),
    path('todo/', todo_views.todo_list, name='todo-list'),
    path('todo/create/', todo_views.todo_create, name='todo-create'),
    path('todo/<int:todo_id>/delete/', todo_views.todo_delete, name='todo-delete'),
]