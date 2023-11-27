import unittest
import pymysql

class DBTests(unittest.TestCase):

    def test_connection(self):
        conn = pymysql.connect(host="localhost", user="root", password="mysql@123", db="slash")
        self.assertNotEqual(conn, None)
    
    def test_valid_login(self):
        conn = pymysql.connect(host="localhost", user="root", password="mysql@123", db="slash")
        username = "testUser"
        password = "testPassword"
        values = (username, password)
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) values (%s, %s)"
        x = cursor.execute(query, values)
        conn.commit()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, values)
        record = cursor.fetchone()
        self.assertNotEqual(record, None)
        query = "DELETE FROM users where (username=%s)"
        value = (username)
        x = cursor.execute(query, value)
        conn.commit()

    def test_invalid_login(self):
        conn = pymysql.connect(host="localhost", user="root", password="mysql@123", db="slash")
        username = "testUser"
        password = "testPassword"
        values = (username, password)
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) values (%s, %s)"
        x = cursor.execute(query, values)
        conn.commit()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        incorrectValues = ("p", "d")
        cursor.execute(query, incorrectValues)
        record = cursor.fetchone()
        self.assertEqual(record, None)
        query = "DELETE FROM users where (username=%s)"
        value = (username)
        x = cursor.execute(query, value)
        conn.commit()

if __name__ == "main":
    unittest.main()