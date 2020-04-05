from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
class UserListView(viewsets.ModelViewSet):
    """Get all the user list"""
    permission_classes = [AllowAny]
    queryset = MyUser.objects.all().exclude(is_superuser=True)
    serializer_class = UserListSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserListSerializer(self.queryset, many=True)
        return Response({"members":serializer.data})