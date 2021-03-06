from django.test import TestCase
from vectra_vts.models import Person,Users,Vehicle,GpsDevice
from django.test import Client
import unittest

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="lion", middle_name="roar",last_name='aoids',birthday='1995-03-03')
    def test_person(self):
    	self.assertEqual(Person.objects.get(first_name='lion').first_name, 'lion')
        
class UsersTestCase(TestCase):
    def setUp(self):
        Users.objects.create(email="lion@yahoo.com",username="lion", password="roar")
    def test_users(self):
    	self.assertEqual(Users.objects.get(username='lion').username, 'lion')

class VehicleTestCase(TestCase):
    def setUp(self):
        Vehicle.objects.create(plate_number="6678878")
    def test_vehicle(self):
    	self.assertEqual(Vehicle.objects.get(plate_number="6678878").plate_number, '6678878')

class GpsDeviceTestCase(TestCase):
    def setUp(self):
        GpsDevice.objects.create(device_id="346556",status="A",being_used="A",)
    def test_device(self):
    	self.assertEqual(GpsDevice.objects.get(device_id="346556").device_id ,"346556")
  
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/home/')
        response = self.client.get('/login/')
        


        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        #self.assertEqual(len(response.context['login']), 5)
