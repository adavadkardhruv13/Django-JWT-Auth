# Django JWT Authentication Project

This Django project provides a simple authentication system using JSON Web Tokens (JWT). Users can register, obtain access tokens, refresh tokens, and access a protected dashboard.

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
