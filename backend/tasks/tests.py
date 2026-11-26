from rest_framework.test import APITestCase

class TaskApiTests(APITestCase):
    def test_create_and_list(self):
        r = self.client.post("/api/tasks/", {"title": "Apprendre DevOps"})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(self.client.get("/api/tasks/").json()), 1)

    def test_health(self):
        self.assertEqual(self.client.get("/health/").json(), {"status": "ok"})

    def test_priority_default_and_set(self):
        r = self.client.post("/api/tasks/", {"title": "A"})
        self.assertEqual(r.json()["priority"], 1)
        r = self.client.post("/api/tasks/", {"title": "B", "priority": 3})
        self.assertEqual(r.json()["priority"], 3)