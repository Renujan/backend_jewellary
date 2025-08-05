from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Items, ItemExtraImages
from .serializer import ItemsSerializer, ItemExtraImagesSerializer



# API View for listing all items
class ItemsListView(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API View for retrieving a single item
class ItemDetailView(APIView):
    def get(self, request, pk):
        try:
            item = Items.objects.get(pk=pk)
            serializer = ItemsSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)