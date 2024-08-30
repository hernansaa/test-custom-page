"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6h%a6yu=f^^yo-pb0gcu$=b*j3_jx3nq+ymb2t6v&sho=03oxh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "unfold.apps.BasicAppConfig", # <- Custom app config, not overriding default admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    'widget_tweaks',
    'tinymce',
    'smart_selects',
    'accounting',
    'students',
    'currencies',
    'django_mailbox',
    'branches',
    'providers',
    'email_client',
    'enrollments',
    'invoices',
    'quotations',
    'enquiries',
    'programs',
    'locations',
    'home',
    # 'gs_admin',
    # 'unfold',
    'django.contrib.admin',
    'gs_admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'gs_admin.middleware.CurrentRequestMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'APP_DIRS': True, # <- This will not work with custom template loader
        'OPTIONS': {
            'loaders': [
                'gs_admin.loaders.UnfoldAdminLoader', # <- New template loader
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'home.context_processors.site_context', # To process the base.html
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'

# Directory where static files will be collected
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.globalstudies.es'  # Gmail SMTP server
EMAIL_PORT = 587  # Port for TLS/STARTTLS
EMAIL_USE_TLS = True  # Enable TLS/STARTTLS
EMAIL_USE_SSL = False  # Disable SSL (not needed for TLS/STARTTLS)
EMAIL_HOST_USER = 'hernan@globalstudies.es'  # Your Gmail address
EMAIL_HOST_PASSWORD = '1988Pola'  # Your Gmail password or app password

# Optionally, set a default email address for the 'From' header in outgoing emails
DEFAULT_FROM_EMAIL = 'hernan@globalstudies.es'

# Security settings (ensure you keep your password secure)
# It's recommended to use environment variables to store sensitive information


# Smart Selects Package 
# Includes jQuery in every page that includes a field from smart_selects.
 
USE_DJANGO_JQUERY = True

# Unfold Admin configuration

UNFOLD = {
    "SITE_TITLE": 'GS Manager',
    "SITE_HEADER": 'GS Manager',
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
    },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/jquery-3.6.0.min.js"),
    #     lambda request: static("js/chainedfk.js"),
    # ],
    "DASHBOARD_CALLBACK": "gs_admin.utils.dashboard_callback",
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("CRM"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:index"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Enquiries"),
                        "icon": "people",
                        "link": reverse_lazy("gs-admin:enquiries_enquiry_changelist"),
                    },
                    {
                        "title": _("Quotations"),
                        "icon": "request_quote",
                        "link": reverse_lazy("gs-admin:quotations_quotation_changelist"),
                    },
                    {
                        "title": _("Invoices"),
                        "icon": "receipt_long",
                        "link": reverse_lazy("gs-admin:invoices_invoice_changelist"),
                    },
                    {
                        "title": _("Enrollments"),
                        "icon": "contract_edit",
                        "link": reverse_lazy("gs-admin:enrollments_enrollment_changelist"),
                    },
                    {
                        "title": _("Students"),
                        "icon": "people",
                        "link": reverse_lazy("gs-admin:students_studentprofile_changelist"),
                    },
                ],
            },
            {
                "title": _("Email (soon)"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Inbox"),
                        "icon": "inbox",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:enquiries_contact_changelist"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Sent"),
                        "icon": "outbox",
                        "link": reverse_lazy("gs-admin:enquiries_contact_changelist"),
                    },
                ],
            },
            {
                "title": _("Chat (soon)"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Inbox"),
                        "icon": "inbox",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:enquiries_contact_changelist"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Sent"),
                        "icon": "outbox",
                        "link": reverse_lazy("gs-admin:enquiries_contact_changelist"),
                    },
                ],
            },
            {
                "title": _("Providers"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Programs"),
                        "icon": "surfing",
                        "link": reverse_lazy("gs-admin:programs_experience_changelist"),
                    },
                    {
                        "title": _("Schools"),
                        "icon": "school",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:providers_school_changelist"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    # {
                    #     "title": _("Accommodation"),
                    #     "icon": "apartment",
                    #     "link": reverse_lazy("gs-admin:programs_experience_changelist"),
                    # },
                ],
            },
            {
                "title": _("Accounting"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Balance"),
                        "icon": "account_balance",
                        "link": reverse_lazy("about_us"),
                    },
                    {
                        "title": _("Invoices"),
                        "icon": "receipt_long",
                        "link": reverse_lazy("about_us"),
                    },
                    {
                        "title": _("Reports"),
                        "icon": "bar_chart",
                        "link": reverse_lazy("about_us"),
                    },
                ],
            },
            {
                "title": _("Website"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Home"),
                        "icon": "home",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:home_homepage_changelist"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("About us"),
                        "icon": "account_balance",
                        "link": reverse_lazy("gs-admin:home_aboutus_changelist"),
                    },
                    {
                        "title": _("Contact"),
                        "icon": "receipt_long",
                        "link": reverse_lazy("gs-admin:home_contactpage_changelist"),
                    },
                ],
            },
            {
                "title": _("Configuration"),
                "separator": False,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Home"),
                        "icon": "home",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("gs-admin:home_homepage_changelist"),
                        # "badge": "sample_app.badge_callback",
                        # "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
        ],
    },
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    "COLORS": {
        "primary": {
            "50": "240 245 250",   
            "100": "230 240 250", 
            "200": "210 225 245",
            "300": "180 205 240",
            "400": "120 165 230",
            "500": "80 130 215",
            "600": "50 100 190",
            "700": "35 70 160",
            "800": "25 50 130",
            "900": "15 35 105",
            "950": "10 15 60",
        },
    },
}
