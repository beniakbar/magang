from rest_framework import serializers, viewsets
from masterdata.models import Satpam

class SatpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satpam
        fields = '__all__'

class SatpamViewSet(viewsets.ModelViewSet):
    queryset = Satpam.objects.all()
    serializer_class = SatpamSerializer
