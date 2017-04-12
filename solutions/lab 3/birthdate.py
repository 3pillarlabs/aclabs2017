import datetime
import unittest


CURRENT_YEAR = 2017


class Person(object):
    def __init__(self, birthyear=1990, birthmonth=0, birthday=0):
      self._birthyear = birthyear
      self._birthmonth = birthmonth
      self._birthday = birthday

    @classmethod
    def from_datestring(cls, datestring):
      date = datetime.datetime.strptime(datestring, '%Y/%m/%d')
      return cls(birthyear=date.year,
                 birthmonth=date.month,
                 birthday=date.day)
      
    def get_age(self):
      """Subtracts current year from birth year"""
      # return CURRENT_YEAR - self._birthyear
      now = datetime.datetime.now()
      import pdb; pdb.set_trace()
      
      delta = datetime.timedelta(365 * self._birthyear + 30 * self._birthmonth + self._birthday)
      diff = now - delta
      fmt = "{years} years, {months} months, {days} days"
      output = fmt.format(years=diff.year, months=diff.month, days=diff.day)
      return output


class BirthTest(unittest.TestCase):
    def test_getage(self):
        p = Person()
        age = p.get_age()
        self.assertEqual(age, '')
