# yaraProject
**A django rest API test project.**

A user can register to the site by visiting http://localhost:8000/register. After registeration, User is redirected to login page.

A token-based authentication is provided for the site. User can login by sending a POST request entering username and password as JSON (http://localhost:8000/login/). After logging in, the assigned token to the user would be shown on the screen. From this point, users can perform CRUD by including their token in the request's Authentication header unless they will get an error saying **"Authentication credentials were not provided."**

### CRUD Instructions:

* Create: Sending a POST request to http://localhost:8000/api/orders/ to create an order.

* Read: Sending a GET request to http://localhost:8000/api/orders to retrieve orders.

* Update: Sending a PUT request to http://localhost:8000/api/orders/<order_ID> to update an order.

* Delete: Sending a DELETE request to http://localhost:8000/api/orders/<order_ID> to delete an order.


