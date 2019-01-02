import unittest
import json
from Fast_Food_Fast import *

class Fast_Food_Fast(unittest.TestCase):

 def test_home(self):
    test = app.test_client()
    response = test.get('/api/v1/')
    response2 = test.get('/api/v2')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response2.status_code, 404)

 def test_signup(self):
        test= app.test_client()
        response = test.get('/api/v1/auth/signup')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(test.post('/api/v1/auth/signup',json={\
            "fname":"silas","lname":"omurunga","email":"silverdeltamega@gmail.com",\
        "username":"simba","password":"1234","cpassword":\
        "1234"}).status_code,200)
 def login(self):
    test = app.test_client()
    response =test.get('/api/vi/auth/login')
    self.assertEqual(response.status_code,405)
    self.assertEqual(test.post('/api/v1/auth/login', json={"username":"simba",\
    "email":"simbadeveloper@gmail.com","password":"1234"}).status_code,200)

 def test_account(self):
    test = app.test_client()
    response = test.get('/api/v1/account')
    self.assertEqual(response.status_code,200)

 def test_order(self):
    test = app.test_client()
    response = test.get('/api/v1/order')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(test.get('/api/v1/order').status_code,200)

 def test_orders_view(self):
    test= app.test_client()
    response = test.get('/api/v1/order/1')
    self.assertEqual(response.status_code, 200)

 def test_all_orders(self):
    test = app.test_client()
    response =test.get('/api/v1/order')
    self.assertEqual(response.status_code,200)

 def test_delete_orders(self):
        response = app.test_client().get('/api/v1/delete_order/1')
        self.assertEqual(response.status_code, 404)

 def test_logout(self):
        with app.test_client() as tester:
            response = tester.get('/api/v1/logout')
            self.assertEqual(response.status_code, 200)

if __name__=='__main__':
    unittest.main()


