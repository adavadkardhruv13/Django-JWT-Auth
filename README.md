# Django JWT Authentication Project

This Django project provides a simple authentication system using JSON Web Tokens (JWT). Users can register, obtain access tokens, refresh tokens, and access a protected dashboard.

#### Access Tokens
Access tokens carry the necessary information to access a resource. In other words, when a user logs in, the server generates an access token, which the client application then includes in its HTTP header whenever it makes a request to any protected resources.

Access tokens are short-lived. This means if an attacker steals the token, they can use it for a limited time only. When the access token expires, the server will refuse any more requests with it.

#### Refresh Tokens
Refresh tokens come into play when the access token expires. Refresh tokens are longer-lived and are used to request new access tokens. This ensures a better user experience as users aren’t logged out of their sessions and forced to re-authenticate every time their access tokens expire.

However, the caveat is that if a refresh token is stolen, it can be used to gain access for a much longer period of time. That’s why it’s essential to handle them securely and only expose them over HTTPS.

## Features

- User registration
- Token-based authentication with JWT
- Token refreshing
- Basic dashboard with authenticated access

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- Other dependencies (specified in requirements.txt)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/adavadkardhruv13/Django-JWT.git
    
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Authentication

- `/token/`: Obtain JWT access and refresh tokens.
- `/token/refresh/`: Refresh access tokens.
- `/register/`: Register a new user.
- `/dashboard/`: Access a protected dashboard using a valid token.

## Contributing

Feel free to contribute by submitting issues or pull requests. Follow the standard coding conventions specified in the project.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- Thanks to the Django and Django REST framework communities.
- Any other acknowledgments or credits.
