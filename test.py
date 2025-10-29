import requests

# Option 1: Inline HTML string
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome!</title>
</head>
<body>
    <h1>Hello John!</h1>
    <p>Congrats for sending a <strong>test email with HTML</strong> using Mailtrap!</p>
    <p style="color: green;">You are awesome!</p>
</body>
</html>
"""

# Option 2: Load HTML from a file (uncomment if preferred)
# with open("email_template.html", "r") as f:
#     html_content = f.read()

url = "https://sandbox.api.mailtrap.io/api/send/4134638"

payload = {
    "from": {
        "email": "hello@example.com",
        "name": "Mailtrap Test"
    },
    "to": [
        {"email": "johnpatrickcamposano@gmail.com"}
    ],
    "subject": "You are awesome!",
    "text": "Congrats for sending test email with Mailtrap!",  # Plain text fallback
    "html": html_content,  # 👈 Your custom HTML here
    "category": "Integration Test"
}

headers = {
    "Authorization": "Bearer 9dfaaab3ee38d4e9eb0c1a3467c05445",  # ⚠️ Replace "test" with real token!
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)