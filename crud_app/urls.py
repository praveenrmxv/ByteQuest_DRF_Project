
from django.urls import path
from .views import UserListCreat,UserRetriveUpdateDelete
urlpatterns = [
   path("crud_app",UserListCreat.as_view(),name="user-list-create"),
   path("crud_app/<int:pk>/",UserRetriveUpdateDelete.as_view(),name="user-view-details")
]

