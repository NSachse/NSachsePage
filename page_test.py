import os
import page
import unittest
import tempfile

class PageTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, page.app.config['DATABASE'] = tempfile.mkstemp()
		page.app.config['TESTING'] = True
		self.app = page.app.test_client()
		page.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(page.app.config['DATABASE'])		

	def test_empty_db(self):
		rv = self.app.get(/)
		assert 'No entries here' in rv.data
		
if __name__ == '__main__':
	unittest.main()
