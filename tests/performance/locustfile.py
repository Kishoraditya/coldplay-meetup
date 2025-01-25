from locust import HttpUser, task, between
import random

class ConcertUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Register and login
        response = self.client.post("/api/auth/register", json={
            "name": f"User_{random.randint(1000, 9999)}",
            "email": f"user_{random.randint(1000, 9999)}@example.com",
            "seat_section": f"Section_{random.randint(1, 10)}",
            "attendance_date": "2025-01-01"
        })
        self.token = response.json()["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task(3)
    def view_profiles(self):
        self.client.get("/api/profiles", headers=self.headers)

    @task(2)
    def create_match(self):
        self.client.post(
            f"/api/matches/match/{random.randint(1, 100)}",
            headers=self.headers
        )

    @task(1)
    def update_profile(self):
        self.client.put(
            "/api/profiles/me",
            headers=self.headers,
            json={
                "bio": f"Updated bio {random.randint(1, 100)}",
                "interests": ["music", "travel"]
            }
        )
