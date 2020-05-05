from django.test import TestCase
from .models import House


class HouseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        House.objects.create(name='first house')
        House.objects.create(description='a description here')

    def test_name_content(self):
        house = House.objects.get(id=1)
        expected_object_name = f'{house.name}'
        self.assertEquals(expected_object_name, 'first house')

    def test_description_content(self):
        house = House.objects.get(id=2)
        expected_object_name = f'{house.description}'
        self.assertEquals(expected_object_name, 'a description here')