# DKJ Business - A Flask-Based E-Commerce Platform

## Overview
DKJ Business is a e-commerce platform built using Flask, designed to provide users with a seamless experience for buying and selling products. The application supports user authentication, product management while ensuring security and ease of use. With features like balance management, image uploads, and a structured database, DKJ Business aims to offer a solid foundation for an online marketplace.

The platform leverages Flask for its backend, Flask-Login for authentication, Flask-SQLAlchemy for database interactions, and Bootstrap for a responsive and user-friendly frontend. While the core functionalities are implemented, there are several planned enhancements to improve user experience and expand feature capabilities.

## Technologies Used

This project utilizes a combination of backend and frontend technologies to provide a seamless user experience.

### Backend Technologies

- **Python** – Core programming language for the project.

**Flask** – Web framework for handling routes and backend logic.

**Flask-Login** – Manages user authentication and session handling.

**Flask-WTF** – Enables form validation and handling.

**Flask-SQLAlchemy** – ORM for database interactions.

**Werkzeug** – Utility for password hashing and request handling.

### Database & ORM

**SQLite** – Stores user and product data.

**SQLAlchemy** – ORM used to interact with the database.

### Frontend Technologies

**HTML** – Provides the structure for web pages.

**CSS** – Styles the UI elements.

**Bootstrap** – Enhances responsive design.

**JavaScript** – Adds interactivity and dynamic features.

### Other Tools & Utilities

**Jinja2** – Templating engine for rendering dynamic content.

**Poetry** – Dependency management for the project.

## Features
- **User Authentication**: Users can register, log in, and log out securely.
- **Profile Management**: Users can modify their profiles and change passwords (backend implemented, frontend pending).
- **Product Management**: Users can add, list, buy, and delete products from the marketplace.
- **Balance Management**: Users can add funds to their accounts to facilitate purchases.
- **Image Uploads**: Supports user profile pictures and product images with validation.

## Project Structure and File Descriptions

### `run.py`
This is the entry point of the application. It initializes the Flask app and starts the development server. Running this script will launch the web application, allowing users to interact with the platform.

### `dkj_business/__init__.py`
This module initializes the Flask application, configures the database, and sets up necessary extensions such as Flask-Login. It ensures that the necessary environment settings are correctly loaded before the application starts.

### `dkj_business/models.py`
This file defines the SQLAlchemy models for the project. The two primary models are:
- **User**: Stores user details such as username, email, password hash, balance, and profile image.
- **Product**: Stores product details including name, price, owner ID, and image.

These models help structure the database and enable efficient data retrieval and manipulation.

### `dkj_business/forms.py`
Defines WTForms-based forms used in the application. The forms provide a secure way to handle user input for various functionalities, including:
- Registration
- Login
- Product addition
- Profile modification

### `dkj_business/helpers.py`
Contains utility functions that support the main application logic, including:
- Password validation to ensure strong credentials.
- File type validation to restrict image uploads to acceptable formats.

### `dkj_business/routes.py`
This is the core of the application, defining the various routes and their corresponding functionalities:
- `index()`: Displays available products on the homepage.
- `UserIndex()`: Provides a dashboard for logged-in users.
- `login()`: Handles user authentication.
- `logout()`: Logs out the user securely.
- `register()`: Manages new user registrations.
- `add_product()`: Allows users to add new products.
- `myProducts()`: Displays a user's listed products.
- `profil()`: Loads the user profile page.
- `modifyProfil()`: Enables profile modification (UI pending).
- `modifyPassword()`: Allows password updates (UI pending).
- `delete_item()`: Facilitates product deletion.
- `buyItem()`: Processes product purchases.
- `increaseBalance()`: Adds funds to the user's balance.

### `dkj_business/templates/`
Holds all HTML templates used for rendering views. These templates are built using Flask’s Jinja2 templating engine to dynamically display content based on user actions and database queries.

### `dkj_business/static/`
Contains static files, including CSS and JavaScript, to enhance the frontend appearance and functionality.

## Design Choices

### Flask for Backend
Flask was chosen for its simplicity, flexibility, and strong community support. It provides an excellent foundation for building scalable web applications while allowing seamless integration with third-party extensions.

### Flask-Login for Authentication
Flask-Login simplifies user authentication, session management, and route protection, ensuring only authorized users can access certain parts of the application.

### Flask-SQLAlchemy for Database Management
Using SQLAlchemy as an Object-Relational Mapper (ORM) makes database interactions more efficient and Pythonic, reducing the complexity of raw SQL queries.

### Bootstrap for Frontend
Bootstrap was utilized for its responsive design capabilities, providing a clean and modern interface with minimal effort.

## Security Considerations
- **Password Hashing**: User passwords are stored securely using hashing techniques to prevent unauthorized access.
- **File Upload Validation**: Only specific file types are allowed to prevent security vulnerabilities related to malicious uploads.
- **User Authentication & Authorization**: Ensures that protected routes can only be accessed by logged-in users.

## Known Issues and Unimplemented Features
While the core functionalities are operational, a few aspects remain incomplete:
- **Profile and Password Modification UI**: While the backend logic exists, the user interface for modifying profiles and changing passwords is not yet implemented.
- **Limited Payment Processing**: The balance system is manually adjusted instead of integrating with a real payment gateway.
- **Enhanced Product Search and Filtering**: Currently, there are no advanced search options to filter products based on criteria like price range, category, or seller.

## How to Run the Project
To get started with DKJ Business, follow these steps:

1. **Install Dependencies**
   Ensure you have Python installed.
   Setup a virtual environement, activate it & install Poetry
    then run:
   ```bash
   poetry install
   ```

2. **Set Up the Database**
   Apply database migrations using:
   ```bash
   poetry run flask --app dkj_business:create_app db upgrade
   ```

3. **Run the Application**
   Start the Flask server by executing:
   ```bash
   poetry run python run.py
   ```

4. **Access the Platform**
   Open `http://127.0.0.1:5000` in your web browser to start using DKJ Business.

## Future Improvements
To enhance the platform’s capabilities, the following features are planned for future development:
- **Frontend Forms for Profile Modification and Password Change**: Implement UI elements to allow users to update their profiles and change passwords easily.
- **Payment Gateway Integration**: Connect the balance system to real payment processors (e.g., Stripe or PayPal) for seamless transactions.
- **Improved Product Search & Filtering**: Enhance the user experience with better navigation and filtering options.
- **Admin Panel**: Introduce an administrative interface for managing users, products, and transactions.

## Conclusion
DKJ Business is a functional and scalable Flask-based e-commerce platform that lays the groundwork for a fully-featured online marketplace. While several key features are in place, there are still improvements to be made to enhance usability, security, and functionality. This README provides an in-depth look at the project's architecture, design decisions, and future roadmap, ensuring clear documentation for developers and contributors.