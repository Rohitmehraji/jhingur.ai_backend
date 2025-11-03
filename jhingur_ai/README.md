# Jhingur.ai Backend

This is the backend for Jhingur.ai, a powerful AI SaaS platform. Built with FastAPI, this backend is designed for high performance, security, and scalability.

## Features

- **Modular Architecture:** Services are decoupled for maintainability and scalability.
- **Secure Authentication:** JWT-based authentication with OAuth2 support for Google and GitHub.
- **Payment Integration:** Seamlessly integrated with Stripe and Razorpay for subscriptions.
- **AI/ML Ready:** Endpoints for serving and running inference on AI/ML models.
- **User Management:** Full CRUD operations for user profiles.
- **Scalable by Design:** Ready for global deployment and unicorn growth.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL (with SQLAlchemy)
- **Authentication:** JWT, OAuth2
- **Payments:** Stripe, Razorpay
- **AI/ML:** OpenAI

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- An OpenAI account
- Stripe and/or Razorpay accounts

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/jhingur.ai.git
   cd jhingur.ai
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Integrated Application

To run the integrated application, you'll need to run both the frontend and backend servers concurrently.

### Backend

1. **Set up your environment variables** (see below).

2. **Run the backend server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at `http://127.0.0.1:8000`.

### Frontend

1. **Clone the frontend repository:**
   ```bash
   git clone https://github.com/Rohitmehraji/Jhingur.ai_frontend.git
   cd Jhingur.ai_frontend
   ```

2. **Install the dependencies:**
   ```bash
   npm install
   ```

3. **Run the frontend server:**
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`.

## Environment Variables

Create a `.env` file in the root directory and add the following environment variables. Use the `.env.example` file as a template.

| Variable                  | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `DATABASE_URL`            | The connection string for your PostgreSQL database. |
| `OPENAI_API_KEY`          | Your API key for the OpenAI API.                 |
| `STRIPE_SECRET_KEY`       | Your secret key for Stripe.                      |
| `RAZORPAY_KEY_ID`         | Your key ID for Razorpay.                        |
| `RAZORPAY_KEY_SECRET`     | Your key secret for Razorpay.                    |
- **`GOOGLE_CLIENT_ID`**: Your Google OAuth2 client ID.
- **`GOOGLE_CLIENT_SECRET`**: Your Google OAuth2 client secret.
- **`GITHUB_CLIENT_ID`**: Your GitHub OAuth2 client ID.
- **`GITHUB_CLIENT_SECRET`**: Your GitHub OAuth2 client secret.
| `SECRET_KEY`              | A secret key for signing JWTs.                   |
| `ALGORITHM`               | The algorithm to use for JWTs (e.g., `HS256`).    |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | The expiration time for access tokens in minutes. |

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Testing

1. **Install the development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run the tests:**
   ```bash
   pytest
   ```

## Deployment

The application is ready for deployment to any cloud platform that supports Python, such as Render, Vercel, or AWS. You can also containerize the application using Docker.

## Scalability

The application is built with scalability in mind. Here are a few tips for scaling the application:

- **Database:** Use a managed database service like Amazon RDS or Google Cloud SQL.
- **Caching:** Implement a caching layer with Redis or Memcached.
- **Load Balancing:** Use a load balancer to distribute traffic across multiple instances of the application.
- **Asynchronous Tasks:** Use a task queue like Celery to handle long-running tasks.
