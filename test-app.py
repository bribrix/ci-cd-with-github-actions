import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        # check if the page is loaded
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_add_item(self):
        # Test adding an item
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_delete_item(self):
        item_id = 2  # Utilisez l'identifiant réel supprimé dans vos tests
        response = self.app.get(f'/delete/{item_id}', follow_redirects=True)
        # Vérifiez si la suppression et la redirection ont abouti à un code d'état 200
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        
    def test_update_item(self):
        item_id = 1  # replace with the id of the item you want to update
        new_data = {'item': 'new name'}  # replace with the new data for the item
        response = self.app.post(f'/update/{item_id}', data=new_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

if __name__ == '__main__':
    unittest.main()
