
# Outlook Email Processor

## Overview

The Outlook Email Processor is a Python tool designed to automate the extraction and processing of email attachments from a specified Outlook account. This project focuses on filtering emails based on specific keywords and date ranges, saving relevant attachments into a structured directory hierarchy, and logging actions for auditing and troubleshooting. It's particularly useful for individuals or businesses looking to streamline the management of email attachments such as reports, invoices, or specific document types.

## Features

- **Email Filtering:** Selects emails based on specified keywords and date ranges.
- **Attachment Handling:** Saves attachments from filtered emails into a user-defined directory structure.
- **Action Logging:** Generates logs for each processed email and action taken, facilitating easy auditing and troubleshooting.
- **Customization:** Allows for easy customization to fit various use cases through simple configuration.

## Requirements

- Python 3.6 or later
- `win32com.client` library for interaction with Outlook
- Access to an Outlook account with permissions to read emails and attachments

## Installation

To use this project, clone the repository to your local machine:

```
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

Then, install the required dependencies:

```
pip install -r requirements.txt
```

## Configuration

Edit the `config.py` file to set up your email account details, keywords for email filtering, and the directory path for saving attachments.

Example configuration:

```python
# config.py
config = {
    "account_email": "your-email@example.com",
    "base_dir_path": "C:\\Path\\To\\Save\\Attachments",
    "keywords": ["Keyword1", "Keyword2"],
    # Add more configuration options as needed
}
```

## Usage

Run the `email_processor.py` script to begin processing emails:

```
python email_processor.py
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for more details.

## Acknowledgements

- This project utilizes the `win32com.client` library for Microsoft Outlook interaction.
- Thanks to the Python community for their invaluable resources and documentation.

```
