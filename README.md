
# My mommy and me blog

![Responsive display of the blog](path)

[View the live project here](https://my-mommy-and-me.herokuapp.com/ "Link to deployed link - My mommy and me blog")

## Table of contents

1. [Introduction](#Introduction)

2. [UX](#UX)

	A. [Ideal User Demographic](#Ideal-User-Demographic)

	B. [User Stories](#User-Stories)

	C. [Development Plans](#Development-Plans)

	D. [Design](#Design)

3. [Features](#Features)

	A. [Existing Features](#Existing-Features)

	B. [Features to Implement in the future](#Features-to-Implement-in-the-future)

4. [Issues and Bugs](#Issues-and-bugs)

5. [Technologies Used](#Technologies-used)

	A. [Main Languages Used](#Main-Languages-Used)

	B. [Additional Languages Used](#Additional-Languages-Used)

	C. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

6. [Testing](#Testing)

	A. [Testing.md](TESTING.md)

7. [Deployment](#Deployment)

	A. [Deploying on Heroku](#Deploying-on-Heroku)

	B. [Forking the Respository](#Forking-the-repository)

	C. [Creating a Clone](#Creating-a-Clone)

8. [Credits](#Credits)

	A. [Content](#Content)

	B. [Media](#Media)

	C. [Code](#Code)

9. [Acknowledgments](#Aknowledgements)


## Introduction

My mommy and me blog was designed to displayed simple recipes for parents with their children. The site's goal is to allow users to share their recipes and experiences for other users to read and use. I got the inspiration in my 4-years-old daughter, she doesn't go to preschool once a month, and she calls our time together: "My mommy and me".

Users will also be able to comment on recipes, and upload their own images. They can like or unlike the recipe. And they will have the CRUD functionality to post recipes, so they can Create, Read, Update and Delete.

This is the fourth of five projects for completing the Full Stack Software Development program at the Code Institute.

## UX

### Ideal User Demographic

The ideal user of this website is:
• Parents
• Cooking Enthusiasts

### User Stories 

#### Users
1. As a site user I can view a paginated list of posts so that I can select one to read.
2. As a site user I can click on a recipe so that I can read the full text.
3. As a site user/ admin I can view the number of likes on each recipe so that I can see which is the most popular or viral.
4. As a site user/admin I can view comments on an individual recipe so that I can read the conversation.
5. As a site user I can register an account so that I can comment and like posts.
6. As a site user I can leave comments on a recipe so that I can be involved in the conversation.
7. As a site user I can like or unlike a recipe so that I can interact with the content.
8. As a site user I can register with other account (google, facebook, twitter) so that I can sign in quickly.
9. As a site admin I can create, read, update and delete posts so that I can manage my blog content.
10.  As a site admin I can create draft posts so that I can finish writing the content later.
11.  As a site user I can want to save my favorite recipe so that I can find them easily whenever I want.
12.  As a site user I can receive updates so that I can keep reading new recipe.
13.  As a site user I can reply comments from other users so that I can keep track of the same conversation.
14.  As a site user I can want to save my favorite recipe so that I can find them easily whenever I want.
15. As a site user I can reply comments from other users so that I can keep track of the same conversation.
16. As a site user I can view a list of posts so that I can select one to read.
17. As a site user I can see my username displayed so that I know that I log in.
18.  As a Site user I can create a profile so that I can interact with other user.
19.  As a Site user I can edit or update any recipe I posted so that I can add or change something.
20. As a Site user I can delete my own posts so that I can control the information I recipe.

#### Site Admin
1. As a site admin I can create draft posts so that I can finish writing the content later.

### Development Plans

To create an appeling website with a great UX and UI, the developer make a research throughout the best cooking blogs, with the best and worst features.

#### Strategy
- **Roles**
    - User
    - Admin

- **Demographic**
    - Parents
    - Cooking Enthusiasts

- **Psycographics**
    - Personality & Attitude:
        - Patient
        - Creative
        - Curious
    - Values:
        - Love for quality time in family
    - Lifestyle:
        - Parents
        - Interested in homemade food

The website needs to enable the *user* to:
- search for recipes.
- make comments to a recipe.
- like and unlike recipes.
- upload images from their experiences when adding a recipe.
- register and log in to participate in the blog.
- save recipes to a favorite page.

The website needs to enable the *admin* to:
- Create drafts for finishing later.

#### Scope
the scope was defined to be able to determine the work that needed to be done in terms of the features and of the strategies described.

- *Content Requirements*
The user will be expecting:
    - A comprehensive list of recipes.
    - A detailed list with ingredients and procedure.
    - A list of comments.
    - A page to find the saved recipes.

- *Functionality Requirements*
The user will be able to:
    - Navigate the site easily.
    - Select recipes for trying.
    - Add comments to every recipe.
    - Like or unlike recipes.


#### Structure

#### Skeleton
balsamiq wireframes

### Design

#### Color Scheme
The colors were chosen for a soft look of the website and focusing mainly on the images. The terra cotta gives a warm sensation and the cultured color gives a clean and clear sensation without overwhelming the user.

#### Typography
The font chosen for the heading tags was 'Architects Daughter' as it is a cool and soft typography, and for the rest of the text was 'Open Sans' as it is clear and concise for big texts.

#### Imagery
To match the color scheme, the default images for the recipes and the hero image were chosen to complement each other.


## Features

### Existing Features

- **Navigation Bar**

The navbar is presented on all the pages of the site. When the user scrolls, it will remain to the top because it uses a bootstrap's built-in class sticky-top.
On the left-hand side of the navbar is presented the name of the blog: 'My mommy & me' that redirects the user to the home page.
On the right-hand side is presented the navigation links: About, Register and Login. And if the user is logged in, it will be added the 'Add Recipe' link.

* Not logged in: About, Register, Login

![Not logged in navbar](path)

* Logged in: About, Logout, Add Recipe

![Logged in navbar](path)

The navbar is fully responsive, on the smaller devices the navbar will collapse and the navigation links are accessed using a "hamburger menu".

* Hamburger menu

![Hamburger menu](path)

- **Home page:**

Home page - Hero section:

At the top of the page is positionated the hero image, that shows a mom with her daughter cooking together. This is the first visible image to the user. The image is responsive, and it was selected because it represents the goal of the blog. This image is only shown on the home page and in the about page.

![Hero image ](path)

Home page - Recipe posts:

On this section, cards with the main information is displayed to the user. Only is shown 6 cards, and if another recipe is added, it shows a site pagination at the bottom of the section.

![Recipe list ](path)

Home page - Recipe Cards:

Each card has the same style: On the top is an image that can be uploaded by the user, or if the user forgets or doesn't have an image, a default image is shown. Then, it ocmes the title of the recipe, the author, and a small description. And at the bottom, it is the date when the post was created or updated, and the number of likes.

* Card with the chosen image by the user:

![Card with uploaded image](path)

* Card with the default image:

![Card with default image](path)

Home page - Site Pagination:

The home page has a limit of 6 posts, if more posts are added, it will appear a pagination nabvar telling in what page is the user, and links for going to the next page or the previous one.

![Site Pagination](path)

Home page - Footer:

This section has the social media icons from Font Awewsome: Facebook, Twiter, Instagram, and Youtube. Each icon redirects to their respective home page in a new tab. 

![Footer with social media icons](path)

- **About page:**

This section is very similar to the home page, but instead of showing a list of recipes for the main content, it is shown a small description about the blog and how the user can be part of it.

![about section with the main information](path)

- **Add Recipe:**

After the user is logged in, he has a link on the navbar for adding a recipe. If he clicks on this link, he will be redirected to the 

If the user isn't logged in, but knows the URL for this action, a message is shown as a reminder to login or sign up.


- **Comment Form**

- **Comment Section**

- **Like/Unlike Button**


- **Recipe Page**

- **Add/Edit Recipe Page**

- **Sign In Page**

- **Sign Up Page**

- **Sign Out Page**

### Features to Implement in the future

- **Favorite Page**
    - Feature:
    - Readon for not featuring in this release:
- **Saving Drafts to a Profile Page**
    - Feature:
    - Readon for not featuring in this release:
- **Third-Party Authentication**
    - Feature:
    - Readon for not featuring in this release:

## Issues and Bugs

**Bug:**

- **Solution:**

## Technologies Used

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
-  [Cloudinary](https://cloudinary.com/ "Link to Cloudinary Page")
- [Summernote](https://summernote.org "Link to Summernote page")
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
- [Git](https://git-scm.com/ "Link to Git homepage")
- [GitHub](https://github.com/ "Link to GitHub")
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
- [Google Translate](https://translate.google.com/ "Link to Google Translate")
- [Coolors](https://coolors.co/ "Link to Coolors")

## Testing

## Deployment

- This project was developed using a [GitPod](https://gitpod.io/ "Link ot GitPod") workspace. 
- The code was commited to [Git](https://git-scm.com/ "Link to Git").
- The code was pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.


### Deploying on Heroku

### Forking the Repository

### Creating a Clone
When you clone a repository, you copy the repository from GitHub.com to your local machine.

1. On GitHub.com, navigate to the repository's main page.
2. 

## Credits

### Content

### Media

### Code

## Acknowledgements
