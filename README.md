## Bilting
Bilting is a soft clone of the nike e-commerce website. it's an application where user can add items to their cart, they can also add items to their favorite pages. Users can also leave review for any items as lons as they are log in.

You can take a look at Bilting [here](https://bilting.onrender.com)

## Index
[MVP Feature List](https://github.com/giovanyv02/bilting/wiki/MVP-Feature-List) |
[Database Schema](https://github.com/giovanyv02/bilting/wiki/Bilting-diagram)|
[User Stories](https://github.com/giovanyv02/bilting/wiki/User-Stories)|

## Technologies Used
<img src ="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" /><img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /><img src="https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white" /><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />

## Splash Page
![splash](https://cdn.discordapp.com/attachments/1130957424296198224/1134283239683534930/Screenshot_58.png?ex=65ea5d96&is=65d7e896&hm=e611d936dd6882a521d62d7b5c801de9f737849b26329504426ad4f203dc0d08&)


## Products Page
![product](https://cdn.discordapp.com/attachments/1130957424296198224/1140601633231884339/Screenshot_61.png)

## Reviews Page
![Review](https://cdn.discordapp.com/attachments/1130957424296198224/1140601632984403978/Screenshot_62.png)

## Getting started
1. Clone this repository:


   `
      https://github.com/giovanyv02/bilting
   `

3. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

4. Create a **.env** file based on the example with proper settings for your
   development environment

5. Make sure the SQLite3 database connection URL is in the **.env** file

6. This starter organizes all tables inside the `flask_schema` schema, defined
   by the `SCHEMA` environment variable.  Replace the value for
   `SCHEMA` with a unique name, **making sure you use the snake_case
   convention**.

7. Get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

8. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

# Features

## Cart
* Users can add items to their cart s
* Users can view their carts
* Users can delete an item on their carts
* Users can update the quantity of items in their carts

## Review
* Users can write reviews
* Users can read/view reviews for items
* Users can delete their reviews
* Users can update their reviews

## Favorites
* Users can add items to their favorite page
* Users can view their favorite page
* Users can remove items to their favorite page

# Future Features

## Orders
* Users can order items they have in their carts.
* User can view their order page.
* User can update/delete their order.
