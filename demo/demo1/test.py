from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from demo1.views import history
from demo1.views import game
from demo1.views import auth_view
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import Client
from demo1.models import History
from django.utils import timezone
class SimpleTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='sudhir',password='root')
		poll=History.objects.create(user=self.user,name='eminem',hist_date=timezone.now())
		
		
	def test_details(self):
		request = self.factory.get('/history/')	
		request.user = self.user
		response = history(request)
		self.assertEqual(response.status_code, 200)
		
		
	def test_game(self):
		request = self.factory.post('/game/',{'username':'dire'})
		request.user = self.user
		response = game(request)
		self.assertEqual(response.status_code, 200)
		
	def test_auth_false(self):
		request = self.factory.post('/auth_view/',{'username':'d','password':'root'})
		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()
		response=auth_view(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content,'invalid')
	def test_auth_pass(self):
		c=Client()
		response=c.post('/auth_view',{'username':'sudhir','password':'root'})
		#self.assertRedirects(response, '/game')
		self.assertEqual(response.status_code,301)
		print response["Location"]
		
	def test_model(self):
		sp=History.objects.get(user=self.user)
		self.assertEqual(sp.name,'eminem')
		self.assertTrue(sp.hist_date,timezone.now())
	
		
		
		
	
		
		
		
    
