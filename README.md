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
  - Links to Puppy Discovery Page
- Puppy Discovery (Swipe) Page
    - Displays a list of puppies available for adoption in a swipe-style interface
    - Swipe right to add a puppy to the user’s favourites list
    - Swipe left to skip a puppy
    - View basic puppy details such as name, age, breed, and photo
    - Prompt users to sign in or create an account to save favourites
- Favourites Page
    - Displays all puppies the user has favourited
    - Allows users to select a puppy from their favourites to view more details
    - Provides clear navigation to each puppy’s detailed profile page
- Puppy Details Page (Fundraiser)
    - Displays full information about the selected puppy
    - Shows adoption enquiry details (e.g. contact phone number and email)
    - Includes a “Fund This Puppy” call-to-action for users who prefer to donate instead of adopt
    - Confirms successful donation or enquiry submissions with clear user feedback
- Login Page
  - Requires email and password
- Signup Page
  - Fullname
  - Email 
  - Password
  - Confirm password

### API Spec 
| URL                        | HTTP Method | Purpose       | Request Body | Success Response Code | Authent/Author |
| fundraisers/home/          | GET         | Get home page | N/A          | 200                   | None           |
| fundraisers/discovery/     | GET         | Get puppy discovery page | N/A          | 200                   | None                         |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )