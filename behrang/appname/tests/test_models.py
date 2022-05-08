from django.test import TestCase
from django.contrib.auth import get_user_model
"""
instead of using User model directly it is better to use get_user_model and django recommend this also
because if you want to change user model you can easily change from settings AUTH_USER_MODEL
"""


class ModelTest(TestCase):

    def test_create_user_by_mail_successfull(self):
        """Test for creating user with email is successfull"""
        email = 'test@gmail.com'
        password= 'test12345'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_extention(self):
        email= 'my@Gmail.COM'
        password= 'reihsaf23'
        new_user = get_user_model().objects.create_user(
            email=email,password=password
        )
        self.assertEqual(new_user.email, 'my@gmail.com')

    def test_new_mail_error(self):
        with self.assertRaises(ValueError):
             get_user_model().objects.create_user(None,'sfs42jkljk')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'ad@admin.com',
            'wrwfs'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)