from django.urls import path
from a_users.views import profile_view, profile_edit_view

urlpatterns = [
    path('', profile_view, name="profile"),
    path('edit/', profile_edit_view, name="profile-edit")
]
