from django.test import TestCase
from .models import Address, Letting
from django.core.exceptions import ValidationError
from django.urls import reverse


class AddressModelTest(TestCase):

    def setUp(self):
        self.address_data = {
            "number": 123,
            "street": "Main Street",
            "city": "New York",
            "state": "NY",
            "zip_code": 10001,
            "country_iso_code": "USA",
        }

    def test_create_address(self):
        address = Address.objects.create(**self.address_data)
        self.assertEqual(address.number, 123)
        self.assertEqual(address.street, "Main Street")
        self.assertEqual(str(address), "123 Main Street")

    def test_number_max_value_validation(self):
        self.address_data["number"] = 10000  # supérieur à 9999
        address = Address(**self.address_data)
        with self.assertRaises(ValidationError):
            address.full_clean()  # full_clean déclenche les validations

    def test_state_length_validation(self):
        self.address_data["state"] = "NYC"  # plus de 2 caractères
        address = Address(**self.address_data)
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_country_iso_code_length_validation(self):
        self.address_data["country_iso_code"] = "US"  # moins de 3 caractères
        address = Address(**self.address_data)
        with self.assertRaises(ValidationError):
            address.full_clean()


class LettingModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="New York",
            state="NY",
            zip_code=10001,
            country_iso_code="USA",
        )
        self.letting_data = {
            "title": "Beautiful Apartment",
            "address": self.address,
        }

    def test_create_letting(self):
        letting = Letting.objects.create(**self.letting_data)
        self.assertEqual(letting.title, "Beautiful Apartment")
        self.assertEqual(str(letting), "Beautiful Apartment")
        self.assertEqual(letting.address, self.address)

    def test_address_one_to_one_constraint(self):
        Letting.objects.create(**self.letting_data)
        # Essayer de créer une autre location avec la même adresse doit échouer
        new_letting = Letting(title="Another Apartment", address=self.address)
        with self.assertRaises(Exception):
            new_letting.save()


class LettingsViewsTest(TestCase):

    def setUp(self):
        # Création d'une adresse et d'une location pour les tests
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="New York",
            state="NY",
            zip_code=10001,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Beautiful Apartment",
            address=self.address
        )

    def test_index_view_status_code(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_index_view_context(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertIn('lettings_list', response.context)
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_letting_view_status_code(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_view_template_used(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_view_context(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.address)

    def test_letting_view_404(self):
        url = reverse('lettings:letting', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class LettingsIntegrationTest(TestCase):

    def setUp(self):
        # Création de plusieurs adresses et locations
        self.address1 = Address.objects.create(
            number=10,
            street="First Street",
            city="Paris",
            state="ID",
            zip_code=75001,
            country_iso_code="FRA"
        )
        self.address2 = Address.objects.create(
            number=20,
            street="Second Street",
            city="London",
            state="LN",
            zip_code=10001,
            country_iso_code="GBR"
        )

        self.letting1 = Letting.objects.create(
            title="Appartement Parisien",
            address=self.address1
        )
        self.letting2 = Letting.objects.create(
            title="Flat London",
            address=self.address2
        )

    def test_index_integration(self):
        """
        Test complet de l'index :
        - accès à l'URL racine
        - code 200
        - template correct
        - context contient toutes les locations
        """
        url = reverse('lettings:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn(self.letting1, response.context['lettings_list'])
        self.assertIn(self.letting2, response.context['lettings_list'])

    def test_letting_integration(self):
        """
        Test complet d'une location individuelle :
        - accès à l'URL avec id
        - code 200
        - template correct
        - context correct (title et address)
        """
        url = reverse('lettings:letting', args=[self.letting1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting1.title)
        self.assertEqual(response.context['address'], self.address1)

    def test_letting_404_integration(self):
        """
        Test d'accès à une location inexistante
        - URL invalide
        - code 404
        """
        url = reverse('lettings:letting', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
