from rest_framework.pagination import PageNumberPagination
from .models import Laptop
from .serializers import Serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user or request.user.id.is_staff

class StandartResultSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


# Create your views here.
class LaptopAPIview(generics.ListAPIView):
    queryset = Laptop.objects.order_by('id')
    serializer_class = Serializers
    pagination_class = StandartResultSetPagination
    permission_classes = [IsAuthenticated]
class LaptopAPIupdate(generics.UpdateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = Serializers
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()

class LaptopAPIcreate(generics.CreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = Serializers
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save()

class LaptopAPIdelete(generics.DestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = Serializers
    permission_classes = (IsAdminUser,)

    def perform_destroy(self, instance):
        instance.delete()

class LargeResultSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_description = 'page_size'
    max_page_size = 1000

