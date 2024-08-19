# What's Your Favorite Programming Language

A simple web application that allows users to submit their favorite programming language and visualize the popularity of each language using a pie chart.

## Features

- Users can choose and submit their favorite programming language.
- The application displays a pie chart showing the distribution of favorite languages.
- Data is stored in a MongoDB database.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Chart.js)
- **Backend**: Flask
- **Database**: MongoDB

## Setup

### Prerequisites

- Python 3.x
- MongoDB

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tommasocerruti/whats-your-favorite-programming-language.git
    cd whats-your-favorite-programming-language
    ```

2. Create a virtual environment (not mandatory, but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start MongoDB if it's not already running:

    ```bash
    mongod
    ```

5. Run the Flask application:

    ```bash
    python app.py
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

- Select your favorite programming language from the dropdown menu.
- Click "Submit" to send your choice.
- The pie chart will update to show the popularity distribution of all submitted languages.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss the changes first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please contact [Tommaso](mailto:tommasocerruti@gmail.com).