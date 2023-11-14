from django.test import TestCase
from scheduling_app.models import Employee, DayShift, WorkShift, Schedule

# Create your tests here.
class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name="test", department="LDR")
        Employee.objects.create(name="test2", department="CC")
    
    def test_employees_created(self):
        test = Employee.objects.get(name="test")
        test2 = Employee.objects.get(name="test2")
        self.assertEqual(test.get_department(), 'LDR')
        self.assertEqual(test2.get_department(), 'CC')