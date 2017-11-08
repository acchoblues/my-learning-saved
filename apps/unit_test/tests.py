from django.test import TestCase
from unit_test.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar", population=12)
        Animal.objects.create(name="cat", sound="meow", population=22)

    def test_animals_cange_number(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        lion.name = "Cat"
        lion.sound = "HAHA"
        lion.population = 13
        lion.save()
