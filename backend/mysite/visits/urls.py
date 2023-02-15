from django.urls import path, include
from .models import CurrentVisits
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class CurrentVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrentVisits
        fields = ["country", "visits"]


# ViewSets define the view behavior.
class CurrentVisitsViewSet(viewsets.ModelViewSet):
    queryset = CurrentVisits.objects.all()
    serializer_class = CurrentVisitSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"current_visits", CurrentVisitsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
