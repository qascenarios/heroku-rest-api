# RestAPI Heroku App

A Python REST API automation project that tests the [Restful Booker](https://restful-booker.herokuapp.com) API — a publicly available booking management API hosted on Heroku.

## Project Structure

```
RestAPI_heroku_app/
│
├── Requests1/               # Single-booking CRUD operations
│   ├── GET_Request.py       # GET all bookings / GET single booking by ID
│   ├── POST_Request.py      # Create a new booking (returns booking_id)
│   ├── PUT_Request.py       # Update an existing booking by booking_id
│   └── DELETE_Request.py    # Delete a booking by booking_id
│
├── Request2/                # Batch (multi-booking) CRUD operations
│   ├── GET2_Request.py      # GET multiple bookings by their IDs
│   ├── POST2_Request.py     # Create multiple bookings (returns booking_ids list)
│   ├── PUT2_Request.py      # Update multiple bookings in a loop
│   └── DELETE2_Request.py   # Delete multiple bookings in a loop
│
├── Token/                           # Authentication module (gitignored)
│   ├── Authentication.py            # Generates a session token (local use only)
│   └── Authentication.py.example   # Safe template tracked in Git
│
├── Utilities/               # Shared helper functions
│   └── Generic.py           # Uses Faker to generate random last names
│
└── requirements.txt         # Python dependencies
```

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd RestAPI_heroku_app
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## API Under Test

**Base URL:** `https://restful-booker.herokuapp.com`

| Endpoint        | Method | Description                       |
| --------------- | ------ | --------------------------------- |
| `/booking`      | GET    | Retrieve all booking IDs          |
| `/booking/{id}` | GET    | Retrieve a specific booking       |
| `/booking`      | POST   | Create a new booking              |
| `/booking/{id}` | PUT    | Update an existing booking (auth) |
| `/booking/{id}` | DELETE | Delete a booking (auth)           |
| `/auth`         | POST   | Generate an authentication token  |

### Authentication

The PUT and DELETE endpoints require a session token. `Token/Authentication.py` posts credentials to `/auth` and returns the token.

Credentials are read from environment variables, falling back to placeholder strings:

```bash
export BOOKER_USERNAME="admin"
export BOOKER_PASSWORD="password123"
```

For local setup, copy the example file and fill in your credentials:

```bash
cp Token/Authentication.py.example Token/Authentication.py
```

> The real `Token/Authentication.py` is gitignored. Only `Authentication.py.example` is tracked in the repository.

## Running the Scripts

### Requests1 — Single Booking Flow

```bash
# GET all bookings
python -m Requests1.GET_Request

# POST — create one booking (prints booking ID)
python -m Requests1.POST_Request

# PUT — update the booking created by POST_Request
python -m Requests1.PUT_Request

# DELETE — delete the booking created by POST_Request
python -m Requests1.DELETE_Request
```

### Request2 — Batch Booking Flow

```bash
# POST — create 3 bookings
python -m Request2.POST2_Request

# GET — fetch all 3 bookings created above
python -m Request2.GET2_Request

# PUT — update all 3 bookings
python -m Request2.PUT2_Request

# DELETE — delete all 3 bookings
python -m Request2.DELETE2_Request
```

> **Note:** `PUT_Request`, `DELETE_Request`, `PUT2_Request`, and `DELETE2_Request` import `booking_id(s)` from their corresponding POST scripts, so they automatically use the IDs created in that session.

## Dependencies

| Package  | Version | Purpose                            |
| -------- | ------- | ---------------------------------- |
| requests | 2.31.0  | HTTP client for API calls          |
| Faker    | 19.6.2  | Generates random test data (names) |

## Notes

- `Token/Authentication.py` is gitignored to keep credentials out of version control. Use `Token/Authentication.py.example` as the starting template.
- The Restful Booker API is a public sandbox — data may be reset periodically.
- All scripts can be run directly with `python -m <module>` from the project root.
