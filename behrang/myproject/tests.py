from .calc import add
from django.test import TestCase

class CalcTest(TestCase):
    """
    to run in docker
    sudo docker-compose run appi sh -c "python manage.py test"
    """

    def test_calcs(self):
        self.assertEqual(add(3, 4),7)
