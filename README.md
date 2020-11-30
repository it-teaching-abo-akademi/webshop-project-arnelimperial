# WebShop Web Application
[![backend-python-django](https://img.shields.io/badge/Backend-Python/Django-green)](https://www.djangoproject.com)
[![frontend-reactjs](https://img.shields.io/badge/Frontend-Javascript/React-blue)](https://reactjs.org)
[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-9cf.svg)](http://unlicense.org/)

E-commerce web application project coded in Python(Django) for creating API([Django Rest Framework](https://www.django-rest-framework.org)) and for the backend  and Javascript(React) on the client side. Assignment submitted in partial fulfillment of the requirements for the online course in  IT00CD40 Web Technologies, Åbo Akademi University.

---

### Site architecture
- Landing Page (https://nurtsrx.herokuapp.com/): Serve as the home page of the application and for   triggering the automatic DB population that generates six users and with three users already have ten items created available for sale. Re-population of users and items owned by users was initiated by using Django's signals in the users app.

- Shop Page (https://nurtsrx.herokuapp.com/shop): The page to view the available products available for sale that return ten items per page. Paginated using DRF's PageNumber pagination class with page size of 10.




### Python Virtual Environment
```
python -m venv
```

### Project setup
```
pip install
```
React
```
yarn install
```

### Compiles and hot-reloads for development

```
python manage.py runserver
```

```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### React Boilerplate
[Create React App](https://github.com/facebook/create-react-app).