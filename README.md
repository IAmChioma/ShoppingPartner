# ShoppingPartner
This will be a site that shows the similar items and details (such as prices, source) based on a search parameter
![ShoppingPartner](https://github.com/user-attachments/assets/8a37706e-d736-4c5d-8548-2d8a407432c6)

## Insipiration
While shopping, especially as a student, it will be great to see similar products and compare prices, nutritional information e.t.c., from different vendors(Walmart, Target) to know which to shop for as far as cost goes.

## Technologies
- Web scraping using Python (Backend)
- Display product and its details using Html, CSS, JavaScript (Frontend)

## More information
Product details will include name, source, price and image if possible

## Features
#### Backend
- Create request session
- Send a get request using url and search parameter
- Return json data

#### Frontend
- Create a search box
- Add a button beside the search box
- Clicking on the search button should send a request to the backend 
- Check that the search parameter is not empty, if do not call the backend service, display message to the user that search parameter should be set.
- Display json data returned from the backend in an orderly manner (For example, as cards)

#### Future Addition
- Add pagination
- Add a button to navigate to the source page of product showing details about the product 


