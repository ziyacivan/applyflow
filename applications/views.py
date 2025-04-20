from rest_framework.viewsets import ModelViewSet
from applications.models import Company
from applications.serializers import CompanySerializer
from applications.services import CompanyService


class CompanyViewSet(ModelViewSet):
    queryset = Company.active.order_by("-created_at")
    serializer_class = CompanySerializer
    service = CompanyService()

    def perform_create(self, serializer):
        serializer.instance = self.service.create_object(**serializer.validated_data)

    def perform_update(self, serializer):
        serializer.instance = self.service.update_object(
            serializer.instance, **serializer.validated_data
        )

    def perform_destroy(self, instance):
        return self.service.delete_object(instance)
