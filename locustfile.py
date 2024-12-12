from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task
    def load_home_page(self):
        with self.client.get("https://www.n11.com/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Homepage load failed with status code {response.status_code}")

    @task
    def search_iphone(self):
        with self.client.get("https://www.n11.com/arama?q=iphone", catch_response=True) as response:
            if "iPhone" in response.text and response.status_code == 200:
                response.success()
            else:
                response.failure("Search results not as expected or failed to load.")

    @task
    def search_samsung(self):
        with self.client.get("https://www.n11.com/arama?q=samsung", catch_response=True) as response:
            if "Samsung" in response.text and response.status_code == 200:
                response.success()
            else:
                response.failure("Search results for Samsung not as expected or failed to load.")

class WebsiteUser(HttpUser):
    host = "https://www.n11.com"
    tasks = [UserBehavior]
    wait_time = between(1, 5)