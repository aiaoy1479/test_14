from django.test import TestCase
from django.urls import resolve
from polls.views import home_page

class HoemPageTest(TestCase):
    def test_root_url_resolves_to_index_view(self):
        found = resolve("/polls/")
        self.assertEqual(found.func, index)

class DetailPageTest(TestCase):
    def test_root_url_resolves_to_detail_view(self):
        found = resolve("/polls/<int:question_id>")
        self.assertEqual(found.func, detail)

    def test_model_detail(self):
        pass
