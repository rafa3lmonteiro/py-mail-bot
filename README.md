# py-mail-bot – simple python gmail SMTP 

**py-mail-bot** is a small Python script that sends an email using Gmail’s SMTP service.  
It’s meant for learning and testing how to send emails programmatically with Python.

The script:

- Reads the email body from a local file called `email`
- Sends the message via Gmail SMTP over SSL
- Uses a Gmail App Password (token-like) stored in a local `secret.py` file

> ⚠️ **Important:** This project is for testing and learning only.  
> Do **not** commit your real credentials or secrets to any public repository.

---

## 1. How it works

Main script (simplified):

```python
#!/usr/bin/env python3

import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from secret import passwd

EMAIL_ADDRESS = 'your-email-here@gmail.com'
EMAIL_PASSWORD = passwd
EMAIL_TO = 'your-email-destination@gmail.com'

msg = EmailMessage()
with open('./email') as fp:
    msg.set_content(fp.read())

msg['Subject'] = 'Your email subject here'
msg['From'] = formataddr(("Rafael Conte Monteiro", EMAIL_ADDRESS))
msg['To'] = formataddr(("Recipient's name", EMAIL_TO))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
```

The script:

1. Loads your Gmail email and secret password from local variables.
2. Reads the email body from the file `./email`.
3. Builds the email message (subject, from, to, body).
4. Connects to Gmail’s SMTP server (`smtp.gmail.com:465` via SSL).
5. Logs in and sends the email.

---

## 2. Prerequisites

- Python **3.8+**
- A **Gmail** account
- 2-Step Verification enabled on your Google account
- A **Gmail App Password** (this will act as your “token” for the script)

No external Python libraries are required; everything uses the standard library (`smtplib`, `email`, etc.).

---

## 3. Getting a Gmail App Password (Token)

Gmail no longer supports “less secure apps” with your normal password.  
Instead, you must create an **App Password**, which works like a token specifically for this script.

Steps to create it:

1. Go to your Google Account:  
   https://myaccount.google.com

2. In the left menu, go to **Security**.

3. Under **“Signing in to Google”**, make sure:
   - **2-Step Verification** is **ON**.  
     If it is not, enable it first (you will need to configure a second factor such as SMS, Authenticator app, etc.).

4. After 2-Step Verification is enabled, you will see an option **“App passwords”**.
   - Click **App passwords**.
   - You may need to confirm your password again.

5. In the **Select app** menu, choose:
   - `Mail` (or `Other (Custom name)` and type something like `py-mail-bot`)

6. In **Select device**, you can choose:
   - `Other` and type a name (e.g. `PythonScript`), or select an existing device.

7. Click **Generate**.

8. Google will show you a 16-character App Password (something like `abcd efgh ijkl mnop`).
   - **Copy** this password; this is what you will use as `passwd` in the script.
   - Treat it like a secret token – do not share it or commit it to Git.

This App Password is what the script uses as `EMAIL_PASSWORD`.

---

## 4. Project structure

A minimal project layout could look like this:

```text
.
├── email          # text file containing the email body
├── main.py        # your Python script (the one shown above)
└── secret.py      # stores the Gmail App Password
```

Example `secret.py`:

```python
# secret.py
# DO NOT COMMIT THIS FILE TO GIT

passwd = "your-16-char-app-password-here"
```

> 💡 Add `secret.py` to your `.gitignore` to avoid committing secrets by accident.

Example `.gitignore`:

```gitignore
secret.py
__pycache__/
*.pyc
```

---

## 5. Creating the email body file

Create a file named `email` (no extension) in the same directory as `main.py`.

Example content:

```text
Hello,

This is a test message sent automatically by a Python email-sending script developed by Rafael Monteiro.

The purpose of this email is only to validate that the SMTP configuration and the script are working as expected.

Please ignore this message. No action is required.

Best regards,
Rafael Monteiro
```

You can change this text to anything you like; the whole file will be used as the email body.

---

## 6. Configuration

Edit the values in `main.py`:

```python
EMAIL_ADDRESS = 'your-email-here@gmail.com'         # your Gmail address
EMAIL_TO = 'your-email-destination@gmail.com'       # recipient email
```

And make sure `secret.py` contains:

```python
passwd = "your-16-char-app-password-here"
```

Optional: customize the “From” and “To” display names:

```python
msg['From'] = formataddr(("Rafael Conte Monteiro", EMAIL_ADDRESS))
msg['To'] = formataddr(("Recipient's name", EMAIL_TO))
```

---

## 7. Running the script

Inside the project directory, run:

```bash
python3 main.py
```

If everything is correct, you should receive an email at `EMAIL_TO`.

If you see authentication errors:

- Double-check that:
  - You are using the **App Password**, not your normal Gmail password.
  - 2-Step Verification is enabled.
  - `EMAIL_ADDRESS` matches the Gmail account you generated the App Password for.

---

## 8. Security notes

- Never commit `secret.py` or any credential files to Git (especially in public repositories).
- Treat the App Password as a secret token.  
  If it leaks, revoke it in your Google Account (**Security → App passwords**) and generate a new one.
- This script is intentionally simple and not meant for production use.

---

## 9. Future improvements (ideas)

Some ideas to extend **py-mail-bot**:

- Read configuration (email, password, recipients) from environment variables
- Use `dotenv` to manage configuration in a `.env` file
- Add support for HTML emails
- Add CLI arguments for subject, recipient, and body file
- Switch to OAuth2-based authentication (more secure and modern)

---





## License

This project is provided for learning and testing purposes.  
Feel free to fork and adapt it to your needs.
