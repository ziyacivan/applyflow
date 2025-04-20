from applications.models import Company
from utils.services import BaseService


class CompanyService(BaseService):
    def create_object(self, name: str, country: str, **kwargs: dict) -> Company:
        return Company.objects.create(name=name, country=country, **kwargs)

    def update_object(self, instance: Company, **kwargs: dict) -> Company:
        for key, value in kwargs.items():
            setattr(instance, key, value)

        instance.save(update_fields=[key for key in kwargs.keys()])
        return instance

    def delete_object(self, instance: Company):
        instance.soft_delete()
