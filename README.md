```markdown
# Budget Management Web Application

This is a budget management web application built with Django. The application allows users to track their income, expenses, and debts, providing insights into their financial situation.

## Features

- User registration and authentication
- User profile with the ability to upload a profile picture
- Income tracking with planned and actual amounts
- Expense tracking with categories and planned and actual amounts
- Debt tracking with the entity to whom the debt is owed and planned and actual amounts
- Interactive charts and tables to visualize financial data
- Separate views for registered users and guests

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

4. Start the development server:

   ```shell
   python manage.py runserver
   ```

5. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. Register a new account or log in with an existing account.
2. Navigate to the user's home page to view an overview of income, expenses, and debts.
3. Use the provided forms to add new income, expenses, and debts.
4. Navigate to the tables page to view detailed tables of income, expenses, and debts.
5. Use the interactive charts to visualize financial data.
6. Update the user profile by uploading a profile picture.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
