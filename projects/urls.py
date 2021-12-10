from django.urls import path


from .views import ProjectsView, ProjectCreateView, DeleteProject
# RemoveTag


app_name="projects"

urlpatterns = [
    path('', ProjectsView.as_view()),
    path('create-project/', ProjectCreateView.as_view()),
    path('delete-project/<str:pk>', DeleteProject.as_view()),
    # path('remove-tag/', RemoveTag.as_view()),
]
