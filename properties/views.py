import logging
from rest_framework import generics, permissions
from .models import Property
from .serializers import PropertySerializer

logger = logging.getLogger(__name__)

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        logger.info(f"Creating property by user {self.request.user}")
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(f"Property retrieved: {instance} by user {request.user}")
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(f"Property deleted: {instance} by user {request.user}")
        return super().destroy(request, *args, **kwargs)

class PropertyDetailView(generics.RetrieveDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

