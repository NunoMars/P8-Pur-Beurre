from django.test import TestCase
from .forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):

    def test_custom_user_creation_form_email_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields['email'].label == None or form.fields['email'].label == 'Email')
    
    def test_custom_user_creation_form_first_name_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')

    def test_custom_user_creation_form_second_name_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields['second_name'].label == None or form.fields['second_name'].label == 'Second name')

    def test_custom_user_creation_form_password1_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields['password1'].label == None or form.fields['password1'].label == 'Mot de passe')

    def test_custom_user_creation_form_password2_field_label(self):
        form = CustomUserCreationForm()
        self.assertTrue(
            form.fields['password2'].label == None or form.fields['password2'].label == 'Confirmation du mot de passe')

    def test_custom_user_creation_form(self):
        form_data = {
            'email': 'remi@purbeurre.com',
            'first_name': 'Remi',
            'second_name': 'PetitChef',
            'password1': 'Some.hi1',
            'password2': 'Some.hi1',
            }

        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())