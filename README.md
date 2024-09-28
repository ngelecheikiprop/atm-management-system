# ATM Management System

## Overview
This project is a management system for ATM functionality focused on milk dispensing. Below are descriptions of the project folders and their respective functions.

## Folders

### api
- **Functionality**: Contains the API routes and logic for handling requests and responses between the client and server.
- **Key Functions**:
  - `create_transaction()`: Initiates a new transaction.
  - `get_transaction_details()`: Fetches details of a specific transaction.

### models
- **Functionality**: Defines data models representing the structure of the database tables.
- **Key Functions**:
  - `Transaction`: Class that represents a milk transaction.
  - `User`: Class for user authentication and details.

### test_examples
- **Functionality**: Provides test cases and examples to ensure the application functions correctly.
- **Key Functions**:
  - `test_create_transaction()`: Tests the transaction creation process.
  - `test_get_transaction_details()`: Verifies retrieval of transaction details.

### web_flask
- **Functionality**: Contains the main Flask application files, including routes and templates.
- **Key Functions**:
  - `index()`: Renders the main dashboard view.
  - `dispense_milk()`: Handles the logic for milk dispensing operations.

## Installation
Instructions on how to install and run the project locally.

## Usage
A guide on how to use the system and its features.

## Contributing
Information on how to contribute to the project.

## License
Details on the project's license.


![Example Image]([images/ high_leve.drawio.png](https://www.google.com/imgres?q=images&imgurl=https%3A%2F%2Fletsenhance.io%2Fstatic%2F8f5e523ee6b2479e26ecc91b9c25261e%2F1015f%2FMainAfter.jpg&imgrefurl=https%3A%2F%2Fletsenhance.io%2F&docid=-t22bY2ix3gHaM&tbnid=tYmxDgFq4MrkJM&vet=12ahUKEwjF-p3JgOWIAxVQcfEDHc9xLHUQM3oECBwQAA..i&w=1280&h=720&hcb=2&ved=2ahUKEwjF-p3JgOWIAxVQcfEDHc9xLHUQM3oECBwQAA)

make sure to set environment varibles as follows:
MYSQL_USER=atmadmin
MYSQLPWD=iamtheadmin
MYSQL_HOST=localhost
MYSQL_DB=atm_db
