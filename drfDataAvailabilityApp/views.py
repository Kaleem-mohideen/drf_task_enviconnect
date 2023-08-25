from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DataPoint
from .serializers import DataPointSerializer

class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

    @action(detail=False, methods=['get'])
    def get_data_points(self, request):
        total_data_points = DataPoint.objects.exclude(value=None).exclude(value=9999).count()
        max_data_points = DataPoint.objects.count()
        data_availability = (total_data_points / max_data_points) * 100 if max_data_points > 0 else 0
        response_data = {
            "total_data_points": total_data_points,
            "max_data_points": max_data_points,
            "data_availability": data_availability
        }
        return Response(response_data, status=status.HTTP_200_OK)
