# athletitrack/production_settings.py

from .settings import * # Import all settings from the base settings.py

# --- SECURITY SETTINGS FOR DEPLOYMENT ---

# WARNING W020: Set this to the domain name(s) of your live server.
# For example: ALLOWED_HOSTS = ['athletitrack.evsu.edu.ph', 'www.athletitrack.evsu.edu.ph']
ALLOWED_HOSTS = ['*'] # Use ['*'] for initial testing, but replace with your actual domain later.

# WARNING W018: Never have DEBUG = True in production.
DEBUG = False

# WARNING W009: Replace this with a new, long, random key.
# You can generate one here: https://djecrety.ir/
#SECRET_KEY = 'YOUR_NEW_LONG_RANDOM_SECRET_KEY_GOES_HERE'
SECRET_KEY = 'y#v$b!n@w*z5x+q6m_c-e=f)g[h]k{j}p;s,t.u/a'


# WARNING W012: Ensure session cookies are only sent over HTTPS.
SESSION_COOKIE_SECURE = True

# WARNING W016: Ensure the CSRF cookie is only sent over HTTPS.
CSRF_COOKIE_SECURE = True

# WARNING W008: Redirect all non-HTTPS traffic to HTTPS.
SECURE_SSL_REDIRECT = True

# WARNING W004: Enable HTTP Strict Transport Security (HSTS).
# This tells browsers to only communicate with your site over HTTPS.
# Start with a small value (e.g., 3600 for 1 hour) for testing.
# Once you are sure everything works, you can increase it to a large value like 31536000 (1 year).
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --- EMAIL CONFIGURATION (Example for Production) ---
# You would replace the console backend with a real SMTP backend.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.your-email-provider.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'

EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": "YOUR_SENDGRID_API_KEY",
}