#  Personify API
A simple REST API capable of CRUD operations on a "person" resource
 

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Testing](#testing)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites
All dependencies are in the [requirements.txt]("https://github.com/Ayamigah16/hngx-person-api/blob/main/person_api/requirements.txt") file


### Installation
Use the steps below to run the personif-api locally
* Clone the repository
    git clone [hngx-person-api]("https://github.com/Ayamigah16/hngx-person-api/tree/main")
* Navigate to the Project Directory
    cd **person_api"
* Activate the virtualenv
    venv\Scripts\activate
* Install Dependencies
    pip install -r requirements.txt
* Apply Database Migration
    python manage.py migrate
* Create a Superuser (optional)
    python manage.py createsuperuser
* Run the Development Server:
    python manage.py runserver



## API Endpoints
These are the list of the endpoints

- `GET /api/`: List all persons.
- `POST /api/`: Create a new person.
- `GET /api/user_id/`: Retrieve details of a person by name.
- `PUT /api/user_id/`: Update details of a person by name.
- `DELETE /api/user_id/`: Delete a person by name.

### Sample Request

```
http
GET /api/persons/Alice/
```

