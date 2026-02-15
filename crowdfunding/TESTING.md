# Testing Second Leash API Endpoints in Insomnia

This guide walks you through how to test every API endpoint in the Second Leash project using Insomnia. Follow the steps in order — some endpoints depend on data created by earlier ones.

---

## Before You Start

### 1. Start the Server

Open your terminal and run:

```bash
source venv/bin/activate
cd crowdfunding
python manage.py runserver
```

You should see something like:

```
Starting development server at http://127.0.0.1:8000/
```

Leave this terminal running. This is your server — if you close it, none of the requests will work.

### 2. Set Up Insomnia

- Open Insomnia and create a new **Request Collection** (e.g. "Second Leash API")
- Your base URL for all requests will be: `http://localhost:8000`

### 3. Important Concepts

- **Headers**: Extra information sent with your request. We use these for authentication.
- **Body**: The data you send with POST/PUT requests. Always set the body type to **JSON**.
- **HTTP Methods**:
  - `GET` = Retrieve/read data
  - `POST` = Create new data
  - `PUT` = Update existing data
  - `DELETE` = Remove data
- **Authentication Token**: A long string of characters that proves you are logged in. You get this from the login endpoint and include it in every request that requires authentication.

---

## Endpoint 1: Register a New User

Creates a new user account.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/users/` |
| Auth Required | No |

**Body (JSON):**

```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword123"
}
```

**What to expect:**
- Status: `201 Created`
- Response: A JSON object with the new user's details (password will not be shown)

**Troubleshooting:**
- If you get `400 Bad Request`, the username might already exist. Try a different username.

---

## Endpoint 2: Log In (Get Auth Token)

Logs in and gives you a token to use for all future requests.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/api-token-auth/` |
| Auth Required | No |

**Body (JSON):**

```json
{
    "username": "testuser",
    "password": "securepassword123"
}
```

**What to expect:**
- Status: `200 OK`
- Response:

```json
{
    "token": "abc123your_token_here",
    "user_id": 1,
    "email": "testuser@example.com"
}
```

**IMPORTANT:** Copy the `token` value. You will need this for every request below.

---

## How to Add Your Token to Requests

For every endpoint below that says "Auth Required: Yes", you need to add a header:

1. Click the **Headers** tab in Insomnia
2. Add a new header:
   - **Header name:** `Authorization`
   - **Header value:** `Token abc123your_token_here`

Make sure there is a **space** between the word `Token` and your actual token string.

**Common mistake:** Do NOT name the header `Token` — the header name must be `Authorization`.

---

## Endpoint 3: Get All Users

Returns a list of all registered users.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/users/` |
| Auth Required | No |

**Body:** None (leave it empty for GET requests)

**What to expect:**
- Status: `200 OK`
- Response: A JSON array of all users

---

## Endpoint 4: Get a Single User

Returns details for one specific user.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/users/1` |
| Auth Required | No |

Replace `1` with the user ID you want to look up.

**What to expect:**
- Status: `200 OK`
- Response: A JSON object with that user's details

---

## Endpoint 5: Create a Fundraiser (Admin Only)

Creates a new puppy fundraiser. Only admin/staff users can do this.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/fundraisers/` |
| Auth Required | Yes (admin token) |

**Body (JSON):**

```json
{
    "title": "Save Buddy the Beagle",
    "description": "Buddy needs a loving home and medical care.",
    "goal": 5000,
    "image": "https://example.com/buddy.jpg",
    "is_open": true
}
```

**What to expect:**
- Status: `201 Created`
- Response: The created fundraiser object with an `id`, `owner`, and `date_created`

**Troubleshooting:**
- If you get `401 Unauthorized`, check your Authorization header is correct.
- Note the `id` in the response — you will need it for other endpoints.

---

## Endpoint 6: Get All Fundraisers

Returns a list of all puppy fundraisers.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/fundraisers/` |
| Auth Required | No |

**Body:** None

**What to expect:**
- Status: `200 OK`
- Response: A JSON array of all fundraisers

---

## Endpoint 7: Get a Single Fundraiser (Puppy Detail)

Returns full details for one fundraiser, including all its pledges.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/fundraisers/1/` |
| Auth Required | No |

Replace `1` with the fundraiser ID you want to view.

**What to expect:**
- Status: `200 OK`
- Response: A JSON object with all fundraiser fields plus a `pledges` array

**Troubleshooting:**
- If you get `404 Not Found`, that fundraiser ID doesn't exist. Check available IDs using the "Get All Fundraisers" endpoint.

---

## Endpoint 8: Update a Fundraiser (Admin Only)

Updates an existing fundraiser. Only admin/staff users can do this.

| Setting | Value |
|---|---|
| Method | `PUT` |
| URL | `http://localhost:8000/fundraisers/1/` |
| Auth Required | Yes (admin token) |

Replace `1` with the fundraiser ID you want to update.

**Body (JSON):**

You only need to include the fields you want to change:

```json
{
    "title": "Updated: Save Buddy the Beagle",
    "goal": 7500
}
```

**What to expect:**
- Status: `200 OK`
- Response: The updated fundraiser object

**Troubleshooting:**
- If you get `403 Forbidden`, your user is not an admin. See the "Making a User an Admin" section at the bottom of this guide.

---

## Endpoint 9: Delete a Fundraiser (Admin Only)

Permanently deletes a fundraiser and all its related pledges. Only admin/staff users can do this.

| Setting | Value |
|---|---|
| Method | `DELETE` |
| URL | `http://localhost:8000/fundraisers/1/` |
| Auth Required | Yes (admin token) |

Replace `1` with the fundraiser ID you want to delete.

**Body:** None

**What to expect:**
- Status: `200 OK`
- Response: Empty

**Troubleshooting:**
- If you get `403 Forbidden`, your user is not an admin.
- If you get `404 Not Found`, that fundraiser ID doesn't exist.

**Warning:** This cannot be undone! The fundraiser and all its pledges will be permanently deleted.

---

## Endpoint 10: Favourite a Puppy

Adds a puppy/fundraiser to your favourites list.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/discovery/favourite/1/` |
| Auth Required | Yes |

Replace `1` with the fundraiser ID you want to favourite.

**Body:** None (the fundraiser ID is in the URL)

**What to expect:**
- Status: `201 Created`
- Response:

```json
{
    "id": 1,
    "user": 1,
    "date_created": "2026-02-15T04:33:53.888865Z",
    "fundraiser": 1
}
```

**Troubleshooting:**
- If you get `400 Bad Request` with "You have already favourited this puppy", you've already favourited this one. Try a different fundraiser ID.
- If you get `404 Not Found`, that fundraiser doesn't exist.

---

## Endpoint 11: Get My Favourites

Returns all the puppies/fundraisers you have favourited.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/discovery/favourites/` |
| Auth Required | Yes |

**Body:** None

**What to expect:**
- Status: `200 OK`
- Response: A JSON array of your favourited puppies

```json
[
    {
        "id": 1,
        "user": 1,
        "date_created": "2026-02-15T04:33:53.888865Z",
        "fundraiser": 1
    }
]
```

**Troubleshooting:**
- If you get an empty array `[]`, you haven't favourited any puppies yet. Use Endpoint 10 first.

---

## Endpoint 12: Submit an Enquiry About a Puppy

Sends an adoption enquiry for a specific puppy.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/detail/enquire/1/` |
| Auth Required | Yes |

Replace `1` with the fundraiser ID you want to enquire about.

**Body (JSON):**

```json
{
    "fullname": "Tess Trenear",
    "email": "tess@example.com",
    "message": "I would love to adopt this puppy! Can you tell me more?"
}
```

**What to expect:**
- Status: `201 Created`
- Response: The created enquiry object

```json
{
    "id": 1,
    "user": 1,
    "fullname": "Tess Trenear",
    "email": "tess@example.com",
    "message": "I would love to adopt this puppy! Can you tell me more?",
    "date_created": "2026-02-15T05:00:00.000000Z",
    "fundraiser": 1
}
```

---

## Endpoint 13: Create a Pledge (Donate to a Puppy)

Makes a financial pledge/donation to a specific puppy's fundraiser.

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `http://localhost:8000/pledges/` |
| Auth Required | Yes |

**Body (JSON):**

```json
{
    "amount": 50,
    "comment": "Hope this helps!",
    "anonymous": false,
    "fundraiser": 1
}
```

Replace `1` in `"fundraiser": 1` with the fundraiser ID you want to donate to.

**What to expect:**
- Status: `201 Created`
- Response: The created pledge object

---

## Endpoint 14: Get My Pledges

Returns all pledges/donations that YOU (the logged-in user) have made.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/pledges/` |
| Auth Required | Yes |

**Body:** None

**What to expect:**
- Status: `200 OK`
- Response: A JSON array of your pledges

**Troubleshooting:**
- If you get an empty array `[]`, you haven't made any pledges yet. Use Endpoint 13 first.

---

## Endpoint 15: Get All Pledges for a Specific Puppy

Returns all the pledges/donations made to one specific puppy's fundraiser.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `http://localhost:8000/detail/pledges/1/` |
| Auth Required | Yes |

Replace `1` with the fundraiser ID you want to see pledges for.

**Body:** None

**What to expect:**
- Status: `200 OK`
- Response: A JSON array of all pledges for that fundraiser

---

## Suggested Testing Order

Follow this order to make sure you have the data you need at each step:

1. **Register a user** (Endpoint 1)
2. **Log in to get your token** (Endpoint 2)
3. **Create a fundraiser** (Endpoint 5) — so you have a puppy to work with
4. **Get all fundraisers** (Endpoint 6) — confirm it was created
5. **Favourite a puppy** (Endpoint 10)
6. **Get my favourites** (Endpoint 11) — confirm the favourite was saved
7. **Submit an enquiry** (Endpoint 12)
8. **Create a pledge** (Endpoint 13) — donate to the puppy
9. **Get my pledges** (Endpoint 14) — confirm your pledge shows up
10. **Get pledges for a puppy** (Endpoint 15) — see all donations for that puppy
11. **Update a fundraiser** (Endpoint 8) — change the title or goal
12. **Delete a fundraiser** (Endpoint 9) — remove it when done testing

---

## Making a User an Admin

Some endpoints (create, update, delete fundraisers) require your user to be an admin. To make a user an admin:

1. Open a new terminal (keep the server running in the other one)
2. Navigate to your project and activate the virtual environment:

```bash
source venv/bin/activate
cd crowdfunding
```

3. Run this command:

```bash
python manage.py shell -c "
from users.models import CustomUser
user = CustomUser.objects.get(username='your_username_here')
user.is_staff = True
user.save()
print(f'{user.username} is now an admin!')
"
```

Replace `your_username_here` with your actual username.

---

## Quick Reference Table

| Endpoint | Method | URL | Auth | Admin |
|---|---|---|---|---|
| Register | POST | `/users/` | No | No |
| Login | POST | `/api-token-auth/` | No | No |
| Get all users | GET | `/users/` | No | No |
| Get single user | GET | `/users/<id>` | No | No |
| Create fundraiser | POST | `/fundraisers/` | Yes | Yes |
| Get all fundraisers | GET | `/fundraisers/` | No | No |
| Get single fundraiser | GET | `/fundraisers/<id>/` | No | No |
| Update fundraiser | PUT | `/fundraisers/<id>/` | Yes | Yes |
| Delete fundraiser | DELETE | `/fundraisers/<id>/` | Yes | Yes |
| Favourite a puppy | POST | `/discovery/favourite/<id>/` | Yes | No |
| Get my favourites | GET | `/discovery/favourites/` | Yes | No |
| Enquire about puppy | POST | `/detail/enquire/<id>/` | Yes | No |
| Create a pledge | POST | `/pledges/` | Yes | No |
| Get my pledges | GET | `/pledges/` | Yes | No |
| Get puppy's pledges | GET | `/detail/pledges/<id>/` | Yes | No |
