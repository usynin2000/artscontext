from pathlib import Path
import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

load_dotenv()


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    value = os.getenv(var_name)
    if value is None:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable.")
    return value


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable("DJANGO_DEBUG") == "True"

ALLOWED_HOSTS = get_env_variable("DJANGO_ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "posts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_variable("DJANGO_DB_NAME"),
        "USER": get_env_variable("DJANGO_DB_USER"),
        "PASSWORD": get_env_variable("DJANGO_DB_PASSWORD"),
        "HOST": get_env_variable("DJANGO_DB_HOST"),
        "PORT": get_env_variable("DJANGO_DB_PORT"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Yandex Cloud Backet
INSTALLED_APPS += [
    "storages",
]

# Настройки для Yandex Object Storage
AWS_ACCESS_KEY_ID = get_env_variable("YANDEX_ACCESS_KEY_ID")  # Ваш Yandex Access Key
AWS_SECRET_ACCESS_KEY = get_env_variable(
    "YANDEX_SECRET_ACCESS_KEY"
)  # Ваш Yandex Secret Key
AWS_STORAGE_BUCKET_NAME = get_env_variable(
    "YANDEX_BUCKET_NAME"
)  # Имя вашего Yandex бакета
AWS_S3_ENDPOINT_URL = (
    "https://storage.yandexcloud.net"  # Endpoint для Yandex Object Storage
)
AWS_S3_REGION_NAME = get_env_variable("YANDEX_REGION_NAME")  # Регион вашего бакета

# Установка URL для доступа к файлам
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.storage.yandexcloud.net"

# Использование Yandex Object Storage для хранения медиафайлов
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Дополнительные настройки для продакшн-среды
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Добавьте эти строки
    CSRF_TRUSTED_ORIGINS = ["https://artscontext.ru", "https://www.artscontext.ru"]
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
