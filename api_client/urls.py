from django.urls import path
from .views import (
    UserLoginView,
    ProcessTemplateView,
    UserProjectsView,
    CreateUserView,
    UploadTemplateView,
    DownloadTemplateView,
    AdminOnlyView,
    ListTemplatesView,
    GetTemplateJsonView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('process-template/', ProcessTemplateView.as_view(), name='process-template'),
    path('user-projects/<str:email>/', UserProjectsView.as_view(), name='user-projects'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('upload-template/', UploadTemplateView.as_view(), name='upload-template'),
    path('download-template/<int:project_id>/', DownloadTemplateView.as_view(), name='download-template'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('list-templates/', ListTemplatesView.as_view(), name='list-templates'),
    path('get-template-json/<int:project_id>/', GetTemplateJsonView.as_view(), name='get-template-json'),
]
