

[![Build status](https://travis-ci.org/Simbadeveloper/Fast-Food-Fast.io.svg?branch=feature-endpoints)](https://travis-ci.org/Simbadeveloper)
[![Coverage Status](https://coveralls.io/repos/github/Simbadeveloper/Fast-Food-Fast.io/badge.svg)](https://coveralls.io/github/Simbadeveloper/Fast-Food-Fast.io)
[![Maintainability](https://api.codeclimate.com/v1/badges/1333f01f9415bd674e32/maintainability)](https://codeclimate.com/github/Simbadeveloper/Fast-Food-Fast.io/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1333f01f9415bd674e32/test_coverage)](https://codeclimate.com/github/Simbadeveloper/Fast-Food-Fast.io/test_coverage)
[![Build status](https://ci.appveyor.com/api/projects/status/mx1qjmm4icbt308l/branch/master?svg=true)](https://ci.appveyor.com/project/Simbadeveloper/fast-food-fast-io/branch/master)
[ ![Codeship Status for Simbadeveloper/Fast-Food-Fast.io](https://app.codeship.com/projects/8cf12870-9463-0136-1cf0-0a2ae3ab87c0/status?branch=master)](https://app.codeship.com/projects/304674)
[![GitHub issues](https://img.shields.io/github/issues/Simbadeveloper/Fast-Food-Fast.io.svg)](https://github.com/Simbadeveloper/Fast-Food-Fast.io/issues)

[![GitHub license](https://img.shields.io/github/license/Simbadeveloper/Fast-Food-Fast.io.svg)](https://github.com/Simbadeveloper/Fast-Food-Fast.io/blob/master/LICENSE)

Fast-Food-Fast is a delivery service app for a restaurant

# Process
I create a repository at github page<br>
used git clone https://github.com/Simbadeveloper/Fast-Food-Fast.io.git 
to clone the repository to my personal computer<br>
added UI folder which will be used to store my HTML files am working on my project.<br>
Created a branch feature then added the UI folder then commited.<br>
used the following command for the above process<br>

$touch UI<br>
$git checkout -b branch feature<br>
$git status<br>
$git add UI<br> 
$git commit -m "initial commit added UI folder"<br>
$git push origin feature<br>

# Adding my work ptogress on html/css/javascript
i clone the repository to my personal computer again<br>
created two branches<br>
1. feature-user branch for the user work<br>
2. feature-admin branch for the admi work<br>
added the user work (user folder) to feature-user branch,commit the push to the branch.<br>
added the admin work (admin folder) to feature-admin branch,commit then pushed to the branch.<br>

# Pivotal tracker link
https://www.pivotaltracker.com/n/projects/2193586

# This project is hosted at the following url:
admin route:https://simbadeveloper.github.io/didactic-adventure.io/UI/Adminpage.html

user route:https://simbadeveloper.github.io/didactic-adventure.io/UI/userpage.html

landing route:https://simbadeveloper.github.io/didactic-adventure.io/UI/index.html
 

# Addition files


Files that i added include the following<br>


1.coveralls.yml to test the climate cahnges of my repository<br>

2.Travis to test my tests on my repository<br>

3.README.md contain details of my repository<br>

4.Requirements.txt contains my dependencies<br>

5.my python file(Fast_Food_Fast.py) and the test (test_Fast_Food_Fast.py)<br>



# PostMan



https://www.getpostman.com/collections/12c4ea47a629178e16c1 <br>

i test my endpoints using postman<br>


* copy the given url(http://127.0.0.1:5000/) and post it on postman

### Endpoints

* To test the endpoints, from the table bellow, copy the endpoint and add it to the url.

Endpoint                          | description         | Method
----------------------------------|---------------------|--------
/api/v1/                          | Home                | GET
/api/v1/auth/signup               |signup               | POST
/api/v1/auth/confirmation         | Confirm a user      | GET
/api/v1/v1/auth/login             | login a user        | POST
/api/v1/auth/admin                | admin route alone   | POST
/api/v1/auth/user/<name>          | Guest user /admin   | POST
/api/v1/auth/guest/<guest>        | Guest route         | GET
/api/v1/auth/forgetpassword       | Retrieve a passwor  | GET
/api/v1/account                   |Details of a user    | GET
/api/v1/order                    | Make an an order    | POST
/api/v1/order/<int:orderid>       | Delete an order     |DELETE
 /api/v1/order/<int:orderid>      | Modify an order     | PUT
 /api/v1/order/                   |Get all orders made  | GET
 /api/v1/order/<int:orderid>      | Get a specific order|GET
 /api/v1/logout                   | logout              |GET

