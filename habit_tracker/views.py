from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerHabit
from .serializers import HabitSerializer
from .models import Habit
from .pagination import HabitListPageNumberPagination


class HabitCreateAPIView(generics.CreateAPIView):

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):

    serializer_class = HabitSerializer
    pagination_class = HabitListPageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitListPageNumberPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]


class HabitUpdateAPIView(generics.UpdateAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]


class HabitDestroyAPIView(generics.DestroyAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]
