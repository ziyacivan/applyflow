from rest_framework.serializers import ModelSerializer
from applications.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "name",
            "country",
            "is_active",
            "created_at",
            "updated_at",
        )
