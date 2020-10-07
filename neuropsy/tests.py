from django.test import TestCase
from neuropsy.models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(label="Bilan 1", description="Court", amount=460.00)
        Article.objects.create(label="Bilan 2", description="Long", amount=260.00)

    def test_article_label(self):
        a1 = Article.objects.get(label="Bilan 1")
        a2 = Article.objects.get(label="Bilan 2")

