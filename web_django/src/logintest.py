from locust import HttpLocust, TaskSet, between

def product(l):
    l.client.get("product")

def products(l):
    l.client.get("products")

def index(l):
    l.client.get("")

def search(l):
    l.client.get("search")

def about(l):
    l.client.get("abouts")

def job(l):
    l.client.get("job")

def jobs(l):
    l.client.get("jobs")

def login(l):
    # login to the application
    response = l.client.get("admin/login/?next=/admin/")
    csrftoken = response.cookies['csrftoken']
    l.client.post("admin/login/?next=/admin/",
                     {'username': 'bob', 'password': 'admin'},
                     headers={'X-CSRFToken': csrftoken})

def logout(l):
    l.client.get("admin/logout")

class UserBehavior(TaskSet):
    #tasks = {index: 2, search: 2, about: 2, product: 2, products: 2, job: 2, jobs: 2}
    
    def on_start(self):
        login(self)



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
