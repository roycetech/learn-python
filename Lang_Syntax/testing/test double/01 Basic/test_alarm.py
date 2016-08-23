import unittest

from alarm import Alarm


class AlarmTest(unittest.TestCase):


    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)


    def test_check_with_too_low_pressure_sounds_alarm(self):            
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)


    def test_check_with_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)


    def test_check_normal_pressure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)


class TestSensor:
    def __init__(self, pressure):
        self.pressure = pressure
    def sample_pressure(self):
        return self.pressure
