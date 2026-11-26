from rest_framework.test import APITestCase

class TaskApiTests(APITestCase):
    def test_create_and_list(self):
        r = self.client.post("/api/tasks/", {"title": "Apprendre DevOps"})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(self.client.get("/api/tasks/").json()), 1)

    def test_health(self):
        self.assertEqual(self.client.get("/health/").json(), {"status": "ok"})