Technology City
Electronics store
Powering Your Passion for Electronics


Team
Mahmoud Elbehery
Safeya Yasien




*Architecture


User Interface (UI)
Interface for users to interact with the application.
Includes web pages for browsing products and viewing details
Frontend
Client-side logic responsible for handling user interactions.
Utilizes HTML, CSS, and JavaScript frameworks like React.js.
Server
Backend responsible for processing client requests.
Implemented using Python and Flask framework.
Backend API
Handles requests related to user authentication, product data retrieval, and order processing.
Implemented using Python and Flask framework.
Database
Stores persistent data such as product info, name, description, price, img
Utilizes a relational database management system (RDBMS) like MySQL with SQLAlchemy ORM.



*APIs and Methods

For the web client to communicate with the web server:
/api/products
Returns a list of available products in the store.
List and describe any API endpoints or function/methods that you will be creating to allow any other clients to use
class: product
function: getPorduct(productId)
description: Retrieves details of a specific product identified by its ID.
product_id: The unique identifier of the product.
Returns: Details of the product including its name, description ,price, reviews.

