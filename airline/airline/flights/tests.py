from django.test import TestCase,Client
from django.db.models import Max

from . models import Airport, Flights, Passenger

# Create your tests here.
class FlightTestCase(TestCase):
    def setUp(self):

        # Create airports
        a1= Airport.objects.create(code= "AAA", city="City A")
        a2= Airport.objects.create(code= "BBB", city="City B")
        
        # Create Flights
        f1= Flights.objects.create(origin=a1, destination=a2, duration=100)
        f2= Flights.objects.create(origin=a1, destination=a1, duration=200)
        f3= Flights.objects.create(origin=a2, destination=a1, duration=-100)
    
    def test_departures_count(self):
        a= Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),2)

    def test_arrivals_count(self):
        a= Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),2)

    def test_valid_flight(self):
        a1= Airport.objects.get(code="AAA")
        a2= Airport.objects.get(code="BBB")
        f= Flights.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())  

    def test_invalid_flight_destination(self):
        a1= Airport.objects.get(code="AAA")
        a2= Airport.objects.get(code="BBB")
        f= Flights.objects.get(origin=a1, destination=a1, duration=200)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1= Airport.objects.get(code="AAA")
        a2= Airport.objects.get(code="BBB")
        f= Flights.objects.get(origin=a2, destination=a1, duration=-100)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["flights"].count(),3)