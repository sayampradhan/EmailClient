# Email Client

The **Email Client** is a Python program that allows users to connect to their email accounts using IMAP (Internet Message Access Protocol). It provides a simple interface to fetch and display email messages from the user's Inbox.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Email Platforms](#supported-email-platforms)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Email Client** is a command-line based application written in Python. It is designed to facilitate email retrieval and display for various email platforms that support IMAP.

## Features

- Authenticate with the user's email address, password, and IMAP server.
- Fetch and display all messages from the user's Inbox.
- Show sender, recipient, date, and subject of each email.
- Decode base64-encoded content to display the email text in plain format.

## Installation

To use the **Email Client**, follow these steps:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your_username/email-client.git
   ```

2. Navigate to the project directory:

   ```
   cd email-client
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:

   ```
   python email_client.py
   ```

2. Choose your email platform from the provided options (Gmail, Yahoo, Yahoo Plus, Mail.com, Zoho, MSN, Outlook).

3. Enter your email address and password when prompted.

4. The program will then connect to your IMAP server and fetch all the messages from your Inbox.

5. The email messages will be displayed on the command-line interface, showing sender, recipient, date, subject, and the content of the email.

6. The content of the email will be automatically decoded if it is base64-encoded.

7. The program will automatically log out from the IMAP server after displaying the messages.

## Supported Email Platforms

The **Email Client** currently supports the following email platforms:

- Gmail
- Yahoo
- Yahoo Plus
- Mail.com
- Zoho
- MSN
- Outlook

## Contributing

Contributions to the **Email Client** project are welcome! If you find a bug, have a suggestion, or want to add a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to the terms of the license.
