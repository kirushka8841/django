from django.urls import path
from measurement.views import MeasurementView, SensorView

urlpatterns = [
    path('measurement/', MeasurementView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('sensors/', SensorView.as_view())
]
