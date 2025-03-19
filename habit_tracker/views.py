from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerHabit
from .serializers import HabitSerializer
from .models import Habit
from .pagination import HabitListPageNumberPagination
from .tasks import create_task


class HabitCreateAPIView(generics.CreateAPIView):
    """Класс представления для создания привычки."""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Переопределенный метод создания привычки. Заполняет поле пользователя.
        При создании привычки вызывается функция создания периодической задачи
        для последующей отправки уведомлений пользователю."""

        habit = serializer.save(user=self.request.user)

        id_chat = self.request.user.id_chat_telegram_bot
        period_in_days = habit.period_in_days
        in_time = habit.notification_time
        create_task(habit, period_in_days, in_time, id_chat)


class HabitListAPIView(generics.ListAPIView):
    """Класс представления для вывода списка привычек пользователя. Имеет пагинацию."""

    serializer_class = HabitSerializer
    pagination_class = HabitListPageNumberPagination

    def get_queryset(self):
        """Метод получения списка объектов текущего пользователя."""

        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Класс представления для вывода списка публичных привычек. Имеет пагинацию."""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitListPageNumberPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Класс представления для вывода конкретной привычки. Доступен владельцу привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Класс представления для обновления привычки. Доступен владельцу привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Класс представления для удаления привычки. Доступен владельцу привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerHabit]
