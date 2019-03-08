# yaraProject
**A django rest API test project.**

A user can register to the site by visiting http://localhost:8000/register. After registeration, User is redirected to login page.

A token-based authentication is provided for the site. User can login by sending a POST request entering username and password as JSON (http://localhost:8000/login/). After logging in, the assigned token to the user would be shown on the screen. From this point, users can perform CRUD by including their token in the request's Authentication header unless they will get an error saying **"Authentication credentials were not provided."**

### CRUD Instructions:

* Create: Sending a POST request to http://localhost:8000/api/orders/ to create an order.

* Read: Sending a GET request to http://localhost:8000/api/orders to retrieve orders.

* Update: Sending a PUT request to http://localhost:8000/api/orders/<order_ID> to update an order.

* Delete: Sending a DELETE request to http://localhost:8000/api/orders/<order_ID> to delete an order.


### Testing with Postman:

**Unauthenticated User Request**

![alt text](https://user-images.githubusercontent.com/16460505/54054271-fcc86180-41fe-11e9-80cb-1cb14d6c5293.png)

**Login**
![alt text](https://user-images.githubusercontent.com/16460505/54054396-4d3fbf00-41ff-11e9-85e8-100d0d95f961.png)


**GET Request**
![alt text](https://user-images.githubusercontent.com/16460505/54054465-78c2a980-41ff-11e9-9a2e-b484534202f7.png)


**POST Request**
![alt text](https://user-images.githubusercontent.com/16460505/54054497-8e37d380-41ff-11e9-8c05-592dafe7ebfa.png)


**PUT Request**
![alt text](https://user-images.githubusercontent.com/16460505/54054540-b3c4dd00-41ff-11e9-84a5-665568a353b6.png)


**DELETE Request**
![alt text](https://user-images.githubusercontent.com/16460505/54054573-d1924200-41ff-11e9-8a46-785bee4af27d.png)
