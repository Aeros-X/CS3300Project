from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from scheduling_app.models import Employee, DayShift, WorkShift, Schedule
import datetime

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

class ScheduleTestCase(TestCase):
    def setUp(self):
        Schedule.objects.create(year_cal=12, month_cal=12, week_cal=6)
        Schedule.objects.create(year_cal=1, month_cal=1, week_cal=1)
    
    def test_schedules_created(self):
        schedule = Schedule.objects.get(year_cal=12)
        schedule2 = Schedule.objects.get(year_cal=1)
        self.assertEqual(schedule.__str__(), "6, 12/12")
        self.assertEqual(schedule2.__str__(), "1, 1/1")

class DayshiftTestCase(TestCase):
    def setUp(self):
        scheduleDS = Schedule.objects.create(year_cal=12, month_cal=12, week_cal=6)
        scheduleDS2 = Schedule.objects.create(year_cal=1, month_cal=1, week_cal=1)


        DayShift.objects.create(schedule=scheduleDS, schedule_day=1, day_start_time=datetime.time(10, 00, 00), min_employees_per_department=300)
        DayShift.objects.create(schedule=scheduleDS2, schedule_day=2, day_start_time=datetime.time(10, 00, 00), min_employees_per_department=200)
    
    def test_employees_created(self):
        test = DayShift.objects.get(schedule_day=1)
        test2 = DayShift.objects.get(schedule_day=2)
        self.assertEqual(test.get_min(), 300)
        self.assertEqual(test2.get_min(), 200)

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name="test", department="LDR")
        Employee.objects.create(name="test2", department="CC")
    
    def test_employees_created(self):
        test = Employee.objects.get(name="test")
        test2 = Employee.objects.get(name="test2")
        self.assertEqual(test.get_department(), 'LDR')
        self.assertEqual(test2.get_department(), 'CC')
"""
class LoginFormTest(LiveServerTestCase):
    def testform(self):
        site = webdriver.Firefox()
        site.get('http://127.0.0.1:8000/accounts/login/')

        name = site.find_element(By.NAME, 'username')
        password = site.find_element(By.NAME, 'password')

        submit = site.find_element(By.NAME, 'login')

        name.send_keys('abcdefgh')
        password.send_keys('!@#123QWEqwe')

        submit.click()

        assert 'abcdefgh' in site.page_source

class EmployeeFormTest(LiveServerTestCase):
    def testform(self):
        site = webdriver.Firefox()
        site.get('http://127.0.0.1:8000/accounts/login/')

        name = site.find_element(By.NAME, 'username')
        password = site.find_element(By.NAME, 'password')

        submit = site.find_element(By.NAME, 'login')

        name.send_keys('abcdefgh')
        password.send_keys('!@#123QWEqwe')

        submit.click()

        site.find_element(By.NAME, "employeesTab").click()
        site.find_element(By.NAME, "createEmployee").click()

        name = site.find_element(By.NAME, 'name')
        department = site.find_element(By.NAME, 'department')

        submit = site.find_element(By.NAME, 'submit')

        name.send_keys('yuh')
        depSelect = Select(department)
        depSelect.select_by_visible_text('Leadership')

        submit.click()

        assert 'yuh' in site.page_source
"""