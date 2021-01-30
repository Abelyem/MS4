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
- Bootstrap navbar used added to base.html - sticked at the top across all pages so that any user new or existing will
always have the ability to navigate from any page to any page at all times. 

- The navbar has the name of the site, and an icon (person with a mask) to reflect what the site is/does - the name/icon is 
also a clickable link which takes the user back to the home page (index.html). The options on the nav bar are 'Home', 
'Shop' -> with a dropdown of the option to look at all products, or by shade (options of dark and light).

- The next option listed is 'My Account' with a dropdown of Profile, and Logout for users with existing accounts.
If the user does not have a login, the options would instead be: Login, and Register. A further dropdown added was that to
'Manage Products' - this link allows any authenticated superuser to add new products which would then be displayed on the
all products page, and saved in the database. These features were added through if statements within base.html, and only show
the relevant link/option to the relevant user.

- The search feature addedon the far right side of the page works by taking in key words from the description of any products,
as well as the colour from the product model. It's been made in this way as the description field will contain more information on
any given product, more so than the name field and so would allow any potential customers to search for specific items /
items specific to their needs.

- The bag icon shows the user how much the items currently in their bag come to (figure shown is the grand total), and by
clicking on this, the user goes directly to the /bag/ page, where all items added to the bag are shown, and the user can 
then continue shopping, or proceed to checkout from this page.

- When hovered over, there is a change in shade of the buttons / bag icon so that the user is aware those links are clickable.

## Clickable link in landing page / index.html
- A clickable link is included within the landing page with the words 'Start Shopping'. Although the link sends you to all
products (the same way the navbar option would), this is included in the landing page as the text signifies what the website
offers, and then proceeds to allow the user to go straight into it as opposed to having to search around for any button
that could lead them to the products page.

## My Profile (for registered users)
- Upon logging in, the user is taken straight to the profile page where the page is split into two. One half of the page
contains the users delivery address information, whilst the second contains a table with the users historic orders. 

- The table has headings of order number, item name, date item was purchased, and the order total. The order number has been truncated 
so that the full number is not shown on the page. All order numbers are clickable links which take you to the checkout_success.html
page.

## Item purchased successfully / checkout_success.html
- Referenced above briefly, the checkout_success page is accesible once a user has purchased an item, or they can also reach this page
from the 'My Profile' page, when reviewing historic orders.

- The page contains a jumbotron which confirms the purchase, and states an email confirmation has been sent. Below this (and a break tag), 
the page is split into two divs with one containing the order number shown in full, and also a breakdown of the payment made for that item 
(delivery fee, order total, and the grand total this comes to). The details provided during the purchase are shown on the second div, both 
these items are centered.

## Product management (for superuser/admin) and CRUD functionalities
- Accessible via the 'My Account' --> 'Manage Products' option, only to superusers who are authenticated to add / remove / edit products.

### Add item
- Clicking on the 'Manage Products' option takes the superuser to a page which has a form with the input being identical to the products information.
On this page, the user is able to add new products which are then displayed directly on the all products page. 

### Edit / Delete items
- The edit and delete product options are again only accessible to superusers who are authenticated. These features are shown on the all products page,
as well as the specific page made to view individual products (mask_detail.html). 

- The edit option would take the user to a page which is identical to the 'Manage Products' page, with the entries already filled in with that items
specific information. You can then on this page make any required edits to an existing product and save this.

- The delete option works from the page you are on and is not rendered on any separate page, simply clicking 'Delete' on any particular item will delete/
remove that item from the list of products. Deleting an item from the mask_detail page will return you to the all products page.


# Bag
- Any products added to the bag from the mask_detail (where individual products are shown) are rendered on this page.


## Session cookies
- Session cookies used to keep items within customer's bag unless removed. This allows the user to shop over the course
of any time period, and the items will remain in the bag until cookies are cleared / items are manually removed. 

## Features to implement
- A feature to show the user items he/she had previously placed in their bag but never bought / has looked at more than once
on separate occasions and refer that item to them again, as well as other similar items to that (similar items to be compared
by colour / make / style).

- Reviews on each product, and a rating system through which items can then be rendered. This would provide new capabilities
on the all products page, where any user would be able to search through items based on their reviews (e.g via a star rating system).


# Technologies Used

## HTML
## CSS
## Javascript
## jQuery
## Python/Django/Jinga

# Testing 


# Deployment


# Credits

## Content
## Media
## Acknowledgements 