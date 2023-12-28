# Food Truck Finder App

Welcome to the Food Truck Finder app! This application helps you discover hidden gems of street food in San Francisco. The app consists of a Django backend serving a RESTful API for food trucks and a simple HTML frontend.

## Running the App

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### 1. Clone the Repository

```bash
git clone [<repository_url>](https://github.com/habeeb03/food_trucks.git)https://github.com/habeeb03/food_trucks.git
cd food_trucks
```

### 1. Build and run the docker image
```
docker-compose build
docker-compose up
```

Access the Django app at <url>http://localhost:8080, it will serve the landing (home) page.
You can enter the lat, lng respectvely (as comma seperated) in the serach box and submit to browse the nearby trucks

API end point is live at http://localhost:8080/api/trucks/


You can use CLI to get the truck list

``` python manage.py list_trucks <lat> <lng> ```


