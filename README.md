# Intern Assignment
 Customer Dealer Django Login


Requirements :
Django==1.9 ,
django-crispy-forms==1.6.0 ,
Pillow==6.2.1

A common login page is provided for both Customer And Dealer. 

Registeration form and Login form used Crisp forms and Boostrap3 for frontend styling.

Any person can register with a unique gmail account. He selects his user type as Customer or Dealer during the registeration. Several other information such as profile picture and content imformation is asked in registeration.

Once the user is registerd, he will be logged in and redirected to respective Dashboard depending upon the user type.
The dashboard is User specific and contains information of the user and features as per user type, who logged in. 
Clicking "Power Button" in bottom of the dashboard template will logout the user and redirect to "Login" page. 

Customer's dashboard can also be edited using writing HTML in dash2.html in templates folder.

Some of the features taken care are :
1. User cannot access login page if already loggedin
2. User cannot access register page if already loggedin
3. User cannot access DASHBOARD_PAGE (through url) if logged out.
3. Email is unique.
4. User to Profile table are one to one mapped so if user is deleted, all the details related to it in other table also gets deleted to keep Database Consistant.

Features that can be added:

1. Input Phone number and Authentication using 2 - factor.
2. Verifying Gmail account by send Confirmation Email.


Dash1.html Template used - https://github.com/azouaoui-med/pro-sidebar-template/
