import imaplib
import email


class EmailClient:
    def __init__(self):
        self.imap_dict = {
            "Gmail": "imap.google.com",
            "Yahoo": "imap.mail.yahoo.com",
            "Yahoo Plus": "plus.imap.mail.yahoo.com",
            "Mail": "imap.mail.com",
            "Zoho": "imap.zoho.com",
            "MSN": "imap-mail.outlook.com",
            "Outlook": "outlook.office365.com"
        }

    def authentication(self):
        """Prompts the user to enter their email address, password, and IMAP server.
        Then, it logs in to the IMAP server and returns the connection object.
        """
        imap_user = input("""
        ----- Choose Your Platform -----
        1. Gmail
        2. Yahoo 
        3. Yahoo Plus
        4. Mail.com
        5. Zoho
        6. MSN
        7. Outlook
        --------------------------------

        Enter (for e.g., if you have an account in Google Mail, just type "Gmail"):  """)

        imap_server = self.imap_dict.get(imap_user, "")
        if not imap_server:
            print("Invalid choice. Please choose a valid platform.")
            return

        email_address = input("Email Address: ")
        password = input("Password: ")

        try:
            # port
            self.imap = imaplib.IMAP4_SSL(imap_server)
            self.imap.login(email_address, password)
        except Exception as e:
            print("Error connecting to the server:", e)
            return

        return self.imap

    def get_messages(self):
        """Fetches all messages from the Inbox and prints out the sender, recipient, date, and subject.
        """
        try:
            self.imap.select("Inbox")

            _, msgnums = self.imap.search(None, "ALL")

            for msgnum in msgnums[0].split():
                _, data = self.imap.fetch(msgnum, "(RFC822)")

                message = email.message_from_bytes(data[0][1])

                print(f"Message Number {msgnum}")
                print(f"From: {message.get('From')}")
                print(f"To: {message.get('To')}")
                print(f"BCC: {message.get('BCC')}")
                print(f"Date: {message.get('Date')}")
                print(f"Subject: {message.get('Subject')}")

                print("Content: ")
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        print(part.as_string())

            self.imap.close()

        except Exception as e:
            print("Error while searching new messages: ", e)

    def logout(self):
        """Logs out from the IMAP server."""
        self.imap.logout()


if __name__ == '__main__':
    email_client = EmailClient()
    imap = email_client.authentication()
    email_client.get_messages()
    email_client.logout()
