# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTestCases(TestCase):
    def test_case_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,404)