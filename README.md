# Nurtsrx
[![backend-python-django](https://img.shields.io/badge/Backend-Python/Django-green)](https://www.djangoproject.com)
[![frontend-reactjs](https://img.shields.io/badge/Frontend-Javascript/React-blue)](https://reactjs.org)
[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-9cf.svg)](http://unlicense.org/)
![Heroku](https://pyheroku-badge.herokuapp.com/?app=nurtsrx&style=flat)


An E-commerce and CRUD web application project coded in __Python(Django)__ for creating API([Django Rest Framework](https://www.django-rest-framework.org)) and for the backend  and __Javascript(React)__ on the client side as single page application. Assignment submitted in partial fulfillment of the requirements for the online course in  IT00CD40 Web Technologies, Åbo Akademi University. The [project](https://nurtsrx.herokuapp.com) was deployed in __Heroku__ platform.

---

### Directories
- _webshop_: Django config settings folder.
- _src_: React main folder that contains the Javascript entry point, app, page components(pages) reusable components(partials).
- _core_: Django app as an entry point template view to React's __src__ folder.
- _templates_: Django HTML templates files. 
- _public_: React static files directory.
- _tmp/notifications_: Folder where the emails generated by `django.core.mail.backends.filebased EmailBackend` resides.
- _users_: Django user app folder
- _merchandises_: Django item/products app folder
- _cart_: Django cart app when login users added item in the shop page.
- _purchases_: Django app directory that create an object to all paid items in the cart.
- _initial_: Django app for re-population of defaults users and item.
- _build_: React build files.
- _en_: Python virtual environment.


### Site architecture and Routing
- _Landing Page_ https://nurtsrx.herokuapp.com/: Serve as the home page of the application and for   triggering the automatic DB population that generates six users and with three users already have ten items created available for sale. Re-population of users and items owned by users was initiated by using Django's *post_save [signals](https://docs.djangoproject.com/en/3.1/topics/signals/)* in the `users` app.

- _Shop Page_ https://nurtsrx.herokuapp.com/shop: The page to view the available products available for sale that return ten items per page. Paginated using DRF's [rest_framework.pagination.PageNumberPagination](https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination) with `page_size = 10` and [react-js-pagination](https://www.npmjs.com/package/react-js-pagination) on the frontend. Authenticated and anonymous users can view all of the items for sales but only the login users can shop and can create _merchandise_ objects as item for sale. Login users can only select and buy `merchandises` that they don't owned/created otherwise it will raise `ValidationError` if that event will happen, but it unlikely to happened because the `add to cart` button was disabled for the current user's item. Items are ordered by `created_date`field as `date added`.

- _Login Page_ https://nurtsrx.herokuapp.com/login: User must provide email and password to be submitted in the form.

- _Signup Page_ https://nurtsrx.herokuapp.com/signup: To register a user, username, email, and password with confirmation must be fullfilled. Username and email are unique model field.

- _Account Page_ https://nurtsrx.herokuapp.com/account: For editing user's password, `request.user`must provide the current password and new password entry with confirmation. */account* is a `protected route`.

- _MyItem Page_ https://nurtsrx.herokuapp.com/myitems: Page where authenticated users can view their own items, sold items and bought item. The add item form and edit item form was also found in this page. Only the user that created the `merchandise object` can modify the required field by patch method. */myitems* is a `protected route`.

- _Logout Page_ https://nurtsrx.herokuapp.com/logout: Logout page. Logout page has `confirmation` and must be confirmed by the authenticated user to be successfully sign out from the system. */logout* is a `protected route`.

- _SingleItem Page_ https://nurtsrx.herokuapp.com/{params.slug}: Pages for every items in the store that redirects when user searches for `merchandise title` as single object.   

- _404 Page_ : Catch all unavailable routes.

### API Endpoints
BASE URI: __https://nurtsrx.herokuapp.com/api/__<br />

__/api/users/__ (GET, POST, PATCH, PUT, DELETE)<br />
Retrieve all users. Customizing Django's default `User` model using `AbstractUser`.<br />
Environment variable: REACT_APP_ENDPOINT_AUTH_USERS<br />
Permission: Admin user<br />
Django app name: *users*

- username(required)
- email(required)
- password(required)
- name(non-mandatory profile Char field)
- is_staff(default to False)
- is_active(default to True)
- is_superuser(default to False)
- last_login(login timestamp)
- date_joined(date registered timestamp)
- groups(default to blank)
- user_permissions(default to blank)
- id(auto-field)



**/api/merchandises/?search=** (GET)<br />
Search endpoint by title.<br />
Environment variable: REACT_APP_ENDPOINT_ITEM_SEARCH<br />
Permission: Read only<br />
Django app name: *merchandises*


**/api/merchandises/** (POST, PATCH)<br />
Create and edit merchandise object.<br />
Environment variable: REACT_APP_ENDPOINT_ITEM_DISPLAY<br /> 
Permission: Authenticated user<br />
Django app name: *merchandises*
- title(required)
- description(required)
- price(required)
- id(auto-field)
- product_image(image placelder for item added)
- date_created(timestamp for new item added)
- date_updated(timestamp for item edited)
- price_dec(generated decimal value of price)
- slug(lookup field generated from title)
- url(merchandise url)
- merchant(Vendor foreign key related field)
- merchant_username
- merchant_email


**/api/merchandise-counts/** (GET)<br />
Count all merchandise objects.<br />
Environment variable: REACT_APP_ENDPOINT_PRODUCTS_COUNT<br />
Permission: Admin user<br />
Django app name: *merchandises*


**/api/merchandise-owned/** (GET)<br />
Merchandise objects created by user. Returns pk, title, price, description, price_dec, slug, product_image, created_date, updated_date, merchant.<br />
Environment variable: REACT_APP_ENDPOINT_USER_ITEMS<br />
Permission: Authenticated user<br />
Django app name: *merchandises*

**/api/carts/** (POST)<br />
Add merchandise object to cart
Environment variable: REACT_APP_ENDPOINT_CART<br /> 
Permission: Authenticated user<br />
Django app name: *carts*

- item(required)
- id(auto-field)
- item_name
- customer
- customer_email
- merchant
- item_price
- item_price_dec
- item_merchant_email
- on_stock
- created


**/api/customers-cart/** (GET, DELETE)<br />
Cart object created by user. Return id, item_name, customer, customer_email, merchant, item_price, item_price_dec, item_merchant_email, on_stock, created, item.<br />
Environment variable: REACT_APP_ENDPOINT_USER_CART<br /> 
Permission: Authenticated user<br />
Django app name: *carts*


**/api/users-cart/** (DELETE)<br />
Delete all cart object by user.<br />
Environment variable: REACT_APP_ENDPOINT_USER_CART_DELETE_ALL<br /> 
Permission: Authenticated user<br />
Django app name: *carts*


**/api/purchases/** (POST)<br />
Delete all cart object by user.<br />
Environment variable: REACT_APP_ENDPOINT_PURCHASE<br /> 
Permission: Authenticated user<br />
Django app name: *purchases*

- purchases(Foreign key Cart model required field)
- purchased_item_id
- purchased_item_name
- purchased_item_description
- purchased_item_product_image
- buyer
- buyer_username
- sellers
- purchased_price_dec
- on_stock
- created


__/api/purchases-buyer/__ (GET)<br />
Retrieve user's purchases as buyer.<br />
Environment variable: REACT_APP_ENDPOINT_BUYER<br /> 
Permission: Authenticated user<br />
Django app name: *purchases*


__/api/purchases-sellers/__ (GET)<br />
Retrieve user's purchases objects as seller.<br />
Environment variable: REACT_APP_ENDPOINT_SELLERS<br /> 
Permission: Authenticated user<br />
Django app name: *purchases*


__/api/initial/__ (POST)<br />
Create default users and merchandise.<br />
Environment variable: REACT_APP_ENDPOINT_INITIAL<br /> 
Permission: Admin user<br />
Django app name: *initial*


### User Authentication
The app uses  [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/) for authenticating users with API. Login, signup, change password, and logout are handled by this module. Some configuration are set by [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) in the backend. The default DRF authentication class used was `rest_framework.authentication.TokenAuthentication`.


### Search
Anonymous and login users can search the items by the item's title and by implementing DRF's [search filters](https://www.django-rest-framework.org/api-guide/filtering/#searchfilter) on the backend.


### Security
_Content Security Policy_ and _Permissions Policy_ protection was added to boost the security features of the application. CSP was initiated by installing [django-csp](https://django-csp.readthedocs.io/en/latest/) and set directives such as `default-src`, `script-src`, `style-src`, `connect-src`and etc. with there respective configuration. Permissions policy was implemented by [django-feature-policy](https://pypi.org/project/django-feature-policy/). Built-in security settings was carried out on deployment as well as during development stage.

- [SECURE_PROXY_SSL_HEADER](https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header)
- [SECURE_SSL_REDIRECT](https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect)
- [SECURE_HSTS_SECONDS](https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds)
- [SECURE_HSTS_INCLUDE_SUBDOMAINS](https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains)
- [SECURE_HSTS_PRELOAD](https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload)
- [SECURE_CONTENT_TYPE_NOSNIFF](https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff)
- [SECURE_REFERRER_POLICY](https://docs.djangoproject.com/en/3.1/ref/settings/#secure-referrer-policy)
- [SESSION_COOKIE_SECURE](https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure)
- [SESSION_COOKIE_HTTPONLY](https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly)
- [CSRF_COOKIE_HTTPONLY](https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly)
- [SECURE_BROWSER_XSS_FILTER](https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter)
- [X_FRAME_OPTIONS](https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options)

To secure the site admin interface, One-Time Password was implemented with [django-otp](https://django-otp-official.readthedocs.io/en/stable/) as well as updating the default admin url path. Web app HTTP headers scanned and graded A+ by [Mozilla Observatory](https://observatory.mozilla.org/) and [Security Headers](https://securityheaders.com/). Production check was carried out by running `heroku run python manage.py check --deploy` with no system issue identified.


### Database
Database used on development was `psql (PostgreSQL) 12.4` and `Heroku Postgres Hobby Dev` on production.


### Styling
The website was styled using Bootstrap, Bootswatch(Spacelab theme), Jquery, media queries and custom CSS.


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