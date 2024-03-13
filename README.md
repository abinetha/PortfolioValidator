# Portfolio Validator

## Overview

The Portfolio Validator is a web application built using Flask, designed to help users validate the structure and content of their portfolio websites' HTML and CSS files. This README provides detailed instructions on how to set up, use, and contribute to the project.

## Components

The Portfolio Validator consists of the following components:

- **Flask Application:** Handles the web interface and file validation process.
- 
- **HTML/CSS Validator:** Validates the uploaded HTML and CSS files to ensure they meet specific criteria.
- 
- **Frontend Interface:** Provides users with a simple interface to upload their files and view validation results.

## Installation

**To use the Portfolio Validator locally, follow these steps:**

**Clone the Repository**

   ```bash
   git clone https://github.com/abinetha/PortfolioValidator.git
   
**Navigate to the project directory**

```bash
cd portfolio-validator

**Create a virtual environment (optional but recommended)**

```bash
python3 -m venv venv

**Activate the virtual environment**

**For Windows:**

```bash
venv\Scripts\activate

For macOS/Linux:

```bash
source venv/bin/activate

**Install the required Python packages**

```bash
pip install -r requirements.txt

## Usage

Follow these steps to use the Portfolio Validator:

Run the Flask application

```bash
python app.py

Access the application through a web browser by navigating to http://127.0.0.1:5000/.

Upload your HTML and CSS files using the provided form. The form can be found within the test_portfolio folder.

Click the "Validate" button to initiate the validation process.

View the validation results, which will indicate any errors found in your uploaded files.

Example

An example usage scenario is provided in the Flask application. You can follow the steps outlined in the Usage section to upload your HTML and CSS files and validate them.
