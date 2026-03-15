from django.urls import path

from tasks.views import (TaskListView,
                         TagListView,
                         TaskCreateView,
                         TaskUpdateView,
                         TaskDeleteView,
                         TaskToggleIsDoneView,
                         TagCreateView,
                         TagUpdateView,
                         TagDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("toggle/<int:pk>/", TaskToggleIsDoneView.as_view(), name="task_toggle"),

    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "tasks"
