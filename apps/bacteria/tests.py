from rest_framework.test import APIClient
from django.test import TestCase
from apps.bacteria.api.views import GetNumberOfBacteriaView
from django.urls import reverse
from rest_framework import status
from utils.base import calculate_bacteria


class TestGetNumberOfBacteriaView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_request(self):
        # Caso de prueba: Solicitud válida
        url = reverse("bacteria:bacteria_count")
        data = {
            "days": 60,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)
        self.assertEqual(response.data["total_bacteria"], 7301991)        
        
        data = {
            "days": 23,
            "maturation_period": 2,
            "life_expectancy": 2,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)
        self.assertEqual(response.data["total_bacteria"], 15309)   
        
        
        data = {
            "days": 8,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)
        self.assertEqual(response.data["total_bacteria"], 37)

    def test_invalid_request(self):
        # Caso de prueba: Solicitud inválida
        url = reverse("bacteria:bacteria_count")
        data = {
            "days": -1,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("days", response.data)
        
        data = {
            "days": 1,
            "life_expectancy": 3,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("maturation_period", response.data)
        self.assertIn("reproduction_rate", response.data)

    def test_serializer_integration(self):
        # Caso de prueba: Integración con el serializador
        url = reverse("bacteria:bacteria_count")
        data = {
            "days": 60,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)

    def test_calculate_bacteria_integration(self):
        # Caso de prueba: Integración con la función "calculate_bacteria"
        url = reverse("bacteria:bacteria_count")
        data = {
            "days": 60,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)
        total_bacteria = response.data["total_bacteria"]
        calculated_total_bacteria = calculate_bacteria(60, 4, 3, 2)
        self.assertEqual(total_bacteria, calculated_total_bacteria)
        
        
        data = {
            "days": 8,
            "maturation_period": 4,
            "life_expectancy": 3,
            "reproduction_rate": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_bacteria", response.data)
        total_bacteria = response.data["total_bacteria"]
        calculated_total_bacteria = calculate_bacteria(8, 4, 3, 2)
        self.assertEqual(total_bacteria, calculated_total_bacteria)
