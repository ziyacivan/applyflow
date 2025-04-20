from django.test import TestCase
from model_bakery import baker
from applications.models import Company
from applications.serializers import CompanySerializer
from applications.services import CompanyService


class CompanyServiceTestCase(TestCase):
    """
    TestCase class of CompanyService.
    run: python manage.py runserver --keepdb applications.tests.test_services.CompanyServiceTestCase
    """

    def setUp(self):
        self.service = CompanyService()
        self.company_instance = baker.make(Company, name="Test", country="Test")

    def test_create_object(self):
        data = {"name": "Applyflow", "country": "Türkiye"}
        serializer = CompanySerializer(data=data)

        self.assertTrue(serializer.is_valid())

        instance = self.service.create_object(**serializer.validated_data)
        self.assertIsInstance(instance, Company)

    def test_update_object(self):
        data = {"name": "Applyflow"}
        instance = self.service.update_object(self.company_instance, **data)

        self.assertIsInstance(instance, Company)
        self.assertTrue(instance.name, data.get("name"))

    def test_delete_object(self):
        self.service.delete_object(self.company_instance)
        self.assertFalse(self.company_instance.is_active)
