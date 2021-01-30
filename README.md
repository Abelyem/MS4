# Masked

## UX

The design of the site is bootstrap influenced in the use of the navbar, and other components of bootstrap such as 
cards, and jumbotrons. The site itself is kept to be simple with a beige background colour on the index.html (landing) page,
and a single image rendered. Within this initial page, any user who comes across the site will be able to figure out the
purpose/reason the site exists - to sell face masks, and be guided directly to the products with a clickable link.

### User Stories
- As a user, I want to be able to use the site on any device
- As a user, I want to be able to filter through all face masks available on the site
- As a user, I want to be able to see all face masks set by price (low-high/high-low)
- As a user, I want to be able to be able to filter the face masks by dark and light shades
- As a user, I want to be able to search for specific face masks that suit my needs
- As a user, I want to be able to add individual items to my bag and continue shopping
- As a user, I want to be able to remove any items from my bag before proceeding to checkout
- As a user, I want any items added to my bag to remain there unless removed by myself 
- As a user, I want to be able to register and log into my individual account
- As a user, I want the option to save my details when purchasing items 
- As a user, I want to be able to see a history of all my previous purchases

## Wireframes

[Landing page - ](https://github.com/Abelyem/MS4/blob/master/static/wireframes/img/landing_page_wireframe.png)

The landing page was designed with this template in mind. In terms of usage of colour, and the simple image + text
combined to create a simple landing page which explains the purpose of the site whilst not overpopulating the user 
with content / information when first visitng (or re-visitng) the site.

The navbar was made to have a white background so it remains visible on all pages despite the content / colours that 
may be shown, take a different approach than the wireframe as I wanted the search feature to be clearly visible at all
times, and not hidden behind an image / other components.


[Items added to bag page - ](https://github.com/Abelyem/MS4/blob/master/static/wireframes/img/bag_wireframe.png)

In a table format, the bag.html page, was designed with the above wireframe in mind. In my project, the items are each 
placed on a row showing the image, name and description, price, quantity, and that item's total within a single row with
an 'x' button at the end of each row allowing the user to remove any item added prior to proceeding to checkout.

[Checkout page - ](https://github.com/Abelyem/MS4/blob/master/static/wireframes/img/checkout_wireframe.png)

The checkout page was designed in a slightly different way to the wireframe shown above so that there was more space
for the user to fill in all their information, whilst provoding an order summary on the right of the page which would
again show each item in the bag (in the process of being purchased), with the name + quantity shown, as well as the total
figures for the order, any delivery charges, and finally the grand total the customer would have to pay.

[User profile - ](https://github.com/Abelyem/MS4/blob/master/static/wireframes/img/user_profile.png)

The user profile was designed/based off the boutique_ado project as the features within that project were relevant to my own.
The page shows the user's entered delivery details on one side (right), and an order summary of all previous purchases on the 
the left side of the page.

[Checkout success - ](https://github.com/Abelyem/MS4/blob/master/static/wireframes/img/checkout_success_wireframe.png)

The checkout success page was created using a jumbotron, with additions so that the order summary, and billing details
would be splitinto two, using more space on the page whilst showing the customer all relevant information. It confirms
the purchase was successful, then after a break shows the order summary which contains the full order number, name of the
item bought (and quantity), purchased date, and again the details of the amounts paid - delivery, order total, and the grand
total.


# Features

## Existing features

### Navigation bar
Bootstrap navbar used added to base.html - sticked at the top across all pages so that any user new or existing will
always have the ability to navigate from any page to any page at all times. 

The navbar has the name of the site, and an icon (person with a mask) to reflect what the site is/does - the name/icon is 
also a clickable link which takes the user back to the home page (index.html). The options on the nav bar are 'Home', 
'Shop' -> with a dropdown of the option to look at all products, or by shade (options of dark and light).
The next option listed is 'My Account' with a dropdown of Profile, and Logout for users with existing accounts.
If the user does not have a login, the options would instead be: Login, and Register. A further dropdown added was that to
'Manage Products' - this link allows any authenticated superuser to add new products which would then be displayed on the
all products page, and saved in the database. These features were added through if statements within base.html, and only show
the relevant link/option to the relevant user.

The search feature addedon the far right side of the page works by taking in key words from the description of any products,
as well as the colour from the product model. It's been made in this way as the description field will contain more information on
any given product, more so than the name field and so would allow any potential customers to search for specific items /
items specific to their needs.

The bag icon shows the user how much the items currently in their bag come to (figure shown is the grand total), and by
clicking on this, the user goes directly to the /bag/ page, where all items added to the bag are shown, and the user can 
then continue shopping, or proceed to checkout from this page.

When hovered over, there is a change in shade of the buttons / bag icon so that the user is aware those links are clickable.



- Session cookies used to keep items within customer's bag


- About section of the website to be visible within index.html - this will be side by side with the reviews submitted by registered users.

## Features to implement

- A feature to show the user items he/she had previously placed in their bag but never bought / has looked at more than once
on separate occasions and refer that item to them again, as well as other similar items to that (similar items to be compared
by colour / make / style).


# Technologies Used


# Testing 


# Deployment


# Credits

## Content
## Media
## Acknowledgements 