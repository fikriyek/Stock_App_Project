STOCK APP PROJECT

MODELS
- User
- Category
- Brand
- Firm
- Product
- Purchases
- Sales
- 
ENTITY-RELATIONS DIAGRAM (ERD)

![image](https://github.com/fikriyek/Stock_App_Project/assets/140847020/c85c326e-b5e6-4bdb-a68d-89564a39434f)

USERS
- User information of the person making the request should be automatically obtained in every table that is associated with the user table.
- Every user can perform GET operation.

ADMINS
- can make CRUD operations on User table,
- can make CRUD operations on Category table,
- can make CRUD operations on Brand table,
- can make CRUD operations on Product table,
- can make CRUD operations on Firm table,
- can make CRUD operations on Purchases table,
- can make CRUD operations on Sales table.

GENERAL TODOs
- calculate the total number of products in Category table,
- add search and filter features according to name in Category table,
- define two serializer for Category: Category and Category Detail. View product details of category by product name with Category Detail serializer,
- add search feature according to name in Brand table,
- add search feature according to name in Firm table,
- add search feature according to name and filter feature according to category and brand in Product table,
- stock field in Product table shall be read only,
- calculate price total field in Purchases and Sales tables (price total = quantity * price),
- add search feature according to firm and filter feature according to firm and product in Purchases table,
- increase stock in Product table when the product is purchased,
- decrease stock in Product table when the purchase is deleted,
- update stock in Product table when the purchase is updated,
- add search feature according to brand and filter feature according to brand and product in Sales table,
- decrease stock in Product table when the product is saled,
- increase stock in Product table when the sale is deleted,
- update stock in Product table when the sale is updated.
