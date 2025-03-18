from django.urls import path
from .apps import HabitTrackerConfig
from . import views


app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habit_create/", views.HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit_list/", views.HabitListAPIView.as_view(), name="habit_list"),
    path("habit_list/public/", views.HabitPublicListAPIView.as_view(), name="habit_public_list"),
    path("habit_retrieve/<int:pk>/", views.HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit_update/<int:pk>/", views.HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit_delete/<int:pk>/", views.HabitDestroyAPIView.as_view(), name="habit_delete"),
]
