# Python URL Shortener

A simple URL shortener built with Python using the Flask framework and SQLite as the database. This application allows users to enter a long URL and receive a shortened version that can redirect back to the original URL.

## Description

This URL shortener is a full-stack web application that takes long URLs and generates short, unique URLs that are easier to share and manage. The application uses Flask for the backend, SQLite for storing URLs, and ShortUUID for generating unique short URLs. The front-end is built using simple HTML forms.

## Quick Start

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-url-shortener.git
   cd python-url-shortener

2. Set up a virtual environment:

   ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate

  Or, do so with IDE like Pycharm.

3. Install the required dependencies:
   ```bash
   pip install flask shortuuid

  It could be done with the IDE like Pycharm.
4. Initialize the SQLite database:
The database will be automatically initialized when you first run the app.

Running the Application
Start the Flask development server:
    ```bash
    python app.py

### Usage
Shorten a URL:
1. Visit http://127.0.0.1:5000/.
- Enter a long URL into the provided form and click "Shorten".
- A short URL will be generated and displayed.
2. Redirect using the Short URL:
- Click on the generated short URL or enter it into your browser.
- You will be redirected to the original long URL.

Example
- Input: https://www.example.com/very/long/url
- Output: http://127.0.0.1:5000/abc123
- When you navigate to http://127.0.0.1:5000/abc123, you will be redirected to https://www.example.com/very/long/url. 


