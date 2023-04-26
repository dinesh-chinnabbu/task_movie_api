from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from datetime import date
from movie.models import CinemaProgram


class CinemaProgramTests(APITestCase):

    def setUp(self):
        self.test_cinema_data = {
            'name': 'Test Cinema',
            'protagonists': 'Test Protagonists',
            'start_date': date.today(),
            'status': 'coming-up',
            'poster': SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        }
        self.test_error_cinema_data = {
            'name': 'Test Cinema',
            'protagonists': 'Test Protagonists',
            'start_date': date.today(),
            'status': 'test',
            'poster': SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        }
        self.test_cinema_program = CinemaProgram.objects.create(**self.test_cinema_data)

    def tearDown(self):
        self.test_cinema_program.delete()

    def test_create_cinema_program(self):
        response = self.client.post('/api/v1/cinema_program', data=self.test_cinema_data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('id' in response.json())

    def test_create_error_cinema_program(self):
        response = self.client.post('/api/v1/cinema_program', data=self.test_error_cinema_data, format='multipart')
        self.assertEqual(response.status_code, 422)
        self.assertTrue('status' in str(response.json()))

    def test_read_cinema_program(self):
        response = self.client.get('/api/v1/cinema_program')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
