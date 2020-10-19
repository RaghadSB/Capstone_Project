import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = 'postgresql://postgres:raghad@'\
            + 'localhost:5432/capstoneDB_test'
        setup_db(self.app, self.database_path)
        self.course = {"name": "PHP",
                       "description": "Learn PHP in 5 weeks from A to Z",
                       "duration": "5 weeks"}
        self.teacher = {"name": "Ali", "email": "Ali124@hotmail.con",
                        "phone": "54645646",
                        "profile": "programer and maybe devloper"}
        self.classs = {"name": "anything in 5 weeks",
                       "start_time": "10-10-2020 12:34:23",
                       "teacher_id": "1", "course_id": "1"}
        self.editcals = {"name": "test",
                         "start_time": "8-8-2020 12:34:23",
                         "course_id": "2"}
        self.token = {"Content-Type": "application/json",
                      "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVkZTV2ek9tbnlEUGFxSUtHbGVvMyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lci51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4MDdmMjNhOWZhMDMwMDc1YTVmNTM4IiwiYXVkIjoib25jbGFzc2VzIiwiaWF0IjoxNjAzMDU3NjEwLCJleHAiOjE2MDMwNjQ4MTAsImF6cCI6ImdyRHJLNnlOUTNxM1NYOW9nV3IwU2llQzNScDF6c2N5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2xhc3NlcyIsInBhdGNoOmNsYXNzZXMiLCJwb3N0OmNsYXNzZXMiLCJwb3N0OmNvdXJzZXMiLCJwb3N0OnRlYWNoZXJzIl19.Fp9eHWsgp_s89MJdQqFYGbM4u_ARnVZtJ517TX_sITI4L-RDOz8JsZOYUEMmHPR9tCIQr_HRM3Qcd-hoi-RzwWeF2Jfgr5b-cRQGDEgIOCnP5WBgKbbyNAsjBoCUGZ9vzs0Yv_XJHBCH20_MQ64KVJydaAJQ5NpxNrEQN0rj-Jgt93WwgbUrKB_-mUx__iOu-5xnDVOLwP5E6GMUgOYeux_B07Do2frxPDVPrNOchNesmrNkOpUosIJ_tJs0-l7mPcrsDLdu2BdPPNCbVhJ4pOsUjBnGiXzOvvLfm1K4SGMNXUfI4ubb9D8z6e4ryrTkv2xPN2DYFMvSUInIbIY7FA"}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass
# get endpoints

    def test_get_Teachers(self):
        res = self.client().get('/Teachers')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_Classes(self):
        res = self.client().get('/Classes')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_Courses(self):
        res = self.client().get('/Courses')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
# post endpoints with no authorization

    def test_post_courseF(self):
        res = self.client().post('/Courses', json=self.course)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
# post endpoints with authorization

    def test_post_courseS(self):
        res = self.client().post('/Courses', headers=self.token,
                                 json=self.course)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_teachersS(self):
        res = self.client().post('/Teachers', headers=self.token,
                                 json=self.teacher)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_classesS(self):
        res = self.client().post('/Classes', headers=self.token,
                                 json=self.classs)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
# patch with no authorization

    def test_patch_classesF(self):
        res = self.client().patch('/Classes/1', json=self.editcals)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
# patch with authorization

    def test_patch_classesS(self):
        res = self.client().patch('/Classes/1', headers=self.token,
                                  json=self.editcals)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
# delete with  no authorization

    def test_delete_classesF(self):
        res = self.client().delete('/Classes/1', json=self.editcals)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
# delete with  authorization

    def test_delete_classesS(self):
        res = self.client().delete('/Classes/1', headers=self.token,
                                   json=self.editcals)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
