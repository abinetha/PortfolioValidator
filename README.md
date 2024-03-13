# Portfolio Validator

The Portfolio Validator is a Flask-based web application designed to assist users in validating the structure and content of their portfolio websites' HTML and CSS files. It provides a user-friendly interface for uploading files, performing validation checks, and viewing validation results. The application employs a backend validation mechanism to ensure that uploaded files meet specific criteria, providing users with feedback on any errors encountered.

## Table of Contents

1. [Key Features](#key-features)
2. [Components](#components)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Key Features

- **HTML/CSS Validation:** The application validates the uploaded HTML and CSS files to ensure they adhere to predefined criteria, such as the presence of required sections and elements.
- **User-Friendly Interface:** The interface allows users to easily upload their files, initiate validation checks, and view the validation results in a clear and concise manner.
- **Feedback Mechanism:** Validation results are presented to users, highlighting any errors found in the uploaded files and providing guidance on resolving them.
- **Customizable Criteria:** Users can customize the validation criteria based on their specific requirements, allowing for flexibility in the validation process.

## Components

The Portfolio Validator consists of the following components:

- **Flask Application:** Handles the web interface and file validation process.
- **HTML/CSS Validator:** Validates the uploaded HTML and CSS files to ensure they meet specific criteria.
- **Frontend Interface:** Provides users with a simple interface to upload their files and view validation results.

## Installation

**To use the Portfolio Validator locally, follow these steps:**

**Clone the Repository**

   ```bash
   git clone https://github.com/abinetha/PortfolioValidator.git
   ```
**Navigate to the project directory**

```bash
cd portfolio-validator
```
**Create a virtual environment (optional but recommended)**

```bash
python3 -m venv venv
```
**Activate the virtual environment**

**For Windows:**

```bash
venv\Scripts\activate
```
**For macOS/Linux:**

```bash
source venv/bin/activate
```
**Install the required Python packages**

```bash
pip install -r requirements.txt
```

## Usage

**Follow these steps to use the Portfolio Validator:**

1. Run the Flask application

```bash
python app.py
```
2. Access the application through a web browser by navigating to http://127.0.0.1:5000/.

3. Upload your HTML and CSS files using the provided form. The HTML and CSS files for testing can be found within the test_portfolio folder.

4. Click the "Validate" button to initiate the validation process.

5. View the validation results, which will indicate any errors found in your uploaded files.

## Example

An example usage scenario is provided in the Flask application. You can follow the steps outlined in the Usage section to upload your HTML and CSS files and validate them.
