from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Measurement, Sensor
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementDetailSerializer


class SensorView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        Sensor.objects.create(
            name=request.POST.get('name'),
            descripcion=request.POST.get('description')
        )
        return Response({'status':'Ok'})
    

class SensorView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk): 
        sensor = Sensor.objects.get(id=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'Status':'Ok'})
    

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get('sensor'),
            temperature=request.POST.get('temperature')
        )
        return Response({'status':'Ok'})
