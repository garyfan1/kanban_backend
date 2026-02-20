from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer, UserSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"msg": "pong"})

@api_view(["GET"])
def health_check_jwt(request):
    return Response({"msg": "jwt_pong"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    username = request.user.username
    return Response({"username": username})

class TaskViewSet(viewsets.ModelViewSet):
    # for router to determine URL names such as task-list task-details
    # overwritten by get_queryset in runtime
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]