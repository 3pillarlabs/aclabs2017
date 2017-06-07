from django.test import TestCase
from django.core.urlresolvers import reverse

from polls_app.models import Poll, Question, Choice


class ClearTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(name='example',
                                        slug='example')
        self.question = Question.objects.create(
            question_text="Example?"
        )
        self.poll.questions.add(self.question)
        self.choice = self.question.choice_set.create(
            choice_text="asdf",
            votes=1
        )

    def test_clear(self):
        """Assures that choices are nulled for poll questions"""
        self.assertEqual(self.choice.votes, 1)
        url = reverse('clear', kwargs={'slug': self.poll.slug})
        response = self.client.get(url)
        choice = Choice.objects.get(pk=self.choice.pk)
        self.assertEqual(choice.votes, 0)


class IncrementTest(TestCase):
    def setUp(self):
        self.poll1 = Poll.objects.create(name="Poll-1", slug="poll1")
        self.q1 = Question.objects.create(question_text="Q Text 1")
        self.choice = self.q1.choice_set.create(choice_text="Choice 1", votes=0)
        self.poll1.questions.add(self.q1)

    def test_vote(self):
        poll_url = reverse('detail', args=(self.poll1.slug,))
        data = {'question-{}'.format(self.q1.pk): self.choice.pk }
        self.client.post(poll_url, data, follow=True)
        choice = Choice.objects.get(pk=self.choice.pk)
        self.assertEqual(choice.votes, 1)
