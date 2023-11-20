from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("file-requests/", views.open_file_requests, name='file-requests'),
    path("edit-file-request/<str:id>/", views.file_request_item, name="edit-file-request"),
    path("file-request-email/<str:id>/", views.send_file_request_email, name="send-file-email")
]
