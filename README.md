# Crowdfunding Back End
Second Leash

## Planning:
### Concept/Name
Second Leash is a crowdfunding-backed puppy adoption platform that helps connect potential adopters with puppies in need while offering an alternative way to support them financially. 

Users can swipe through available puppies, save favourites, make adoption enquiries, or contribute to individual puppy fundraisers—giving every puppy a second chance, even when adoption isn’t immediately possible.

### Intended Audience/User Stories
Two types of users
1. Normal user - a user that can swipe / donate money
   1. Can swipe left or right on puppies they are interested in adopting
   2. Swiping right on a puupy adds them to a favourites list within the users profile
   3. Once favourited, the user will be able to go into a favourites page and click on the ones they want to enquire about (this will be a puppy landing page). This page will have all the enquiry details such as phone number etc... This will also have a fund puppy CTA (call to action like a button or something) in which if the user choses not to proceed but can help with funds they donate. 

2. Admin user - user who can put up puppy for adoption / start + stop fundraiser
   1. Can upload puppy info
   2. Can set up puppy fundraiser / delete fundraiser 
   3. Can reply to enquiries

### Front End Pages/Functionality
- Home
  - Landing page
  - Purpose of fundraiser
  - Link to login page/register
- Login Page
  - Requires email and password
  - Password reset button
- Register Page
  - Fullname
  - Password
  - Confirm password
- Password Reset Page
  - Enter new password
  - Reconfirm password and commit
- Admin User
  - Add puppy
  - Delete puppy
- Puppy Discovery (Swipe) Page
    - Displays a list of puppies available for adoption in a swipe-style interface
    - Swipe right to add a puppy to the user’s favourites list
    - Swipe left to skip a puppy
    - View basic puppy details such as name, age, breed, and photo
- Pledges
  - Show list of all puppies the user has made pledges to
- Favourites Page
    - Displays all puppies the user has favourited
    - Allows users to select a puppy from their favourites to view more details
    - Provides clear navigation to each puppy’s detailed profile page
- Puppy Details Page (Fundraiser)
    - Displays full information about the selected puppy
    - Shows adoption enquiry details (e.g. contact phone number and email)
    - Includes a “Fund This Puppy” call-to-action for users who prefer to donate instead of adopt
    - Confirms successful donation or enquiry submissions with clear user feedback


### API Spec 
| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| user/login/ | POST | Validation/authentication of user | email and password | 200 | None |
| user/register | POST | Validation/authentication of user | email, password and fullname | 200 | None |
| user/password-reset | POST | Email | None | 200 | None |
| discovery| GET | Get list of available puppies | None | 200 | Logged in |
| discovery/favourite/{puppy_id} | POST | Favourite puppy ID against user ID | puppy_id | 200 | Logged |
| discovery/favourites/| GET | Get the list of all the favourited puppies of the logged in user| none | 200 | Logged in |
| detail/{puppy_id} | GET | Get puppy details | puppy_id | 200 | Logged in |
| detail/enquire/{puppy_id} | POST | User can enquire about puppy | puppy_id, fullname, email and enquiry | 200 | Logged in |
| detail/pledge/{puppy_id} | POST | Donate to puppy pledge | puppy_id, pledge_amount and user_id | 200 | Logged in |
| detail/pledges/{puppy_id} | GET | Get list of all pledges made to this puppy | puppy_id | 200 | Logged in |
| pledges | GET | Get list of all pledges the user has made | None | 200 | Logged in
| create | POST | Create a puppy item in the DB | name, description, and image | 201 | Logged in as admin |
| delete | POST | Delete a puppy item in the DB | puppy_id | 200 | Logged in as admin |
| update | POST | Update a puppy item in the DB | puppy_id | 200 | Logged in as admin |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )