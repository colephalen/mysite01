from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post  # add this import at the top


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


"""
Results: Seemed to pass, but shouldnt have and it looks weird

(.env) (base) 
22:44 ~/python-cert-q3/Lesson06/Assignment/mysite
$ python manage.py test blogging
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.020s

OK
Destroying test database for alias 'default'...

"""