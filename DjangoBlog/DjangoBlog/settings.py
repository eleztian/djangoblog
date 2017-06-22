"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

SECRET_KEY = '9fc3jwnm$@n5zw(x4pgug=*djhv(610na1x(@e5p0ss0%7xm3z'
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['www.elezt.cn', '127.0.0.1', '115.159.98.104','example.com']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'pagedown',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'compressor'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'blog.middleware.OnlineMiddleware'
]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        #'USER': os.environ.get('DJANGO_MYSQL_USER'),
        #'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD'),
        #'HOST': os.environ.get('DJANGO_MYSQL_HOST'),
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 允许使用用户名或密码登录
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')

STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

SITE_NAME = '我不管反正我最帅'
SITE_URL = 'http://www.elezt.cn'
SITE_DESCRIPTION = '一份耕耘，一份收获.'
SITE_SEO_DESCRIPTION = '小站主要用来记录一些学习心得、笔记以及一些随笔。欢迎大家访问小站！'
SITE_SEO_KEYWORDS = 'linux,python,c,嵌入式'
ARTICLE_SUB_LENGTH = 300
SHOW_GOOGLE_ADSENSE = False
# bootstrap颜色样式
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# 侧边栏文章数目
SIDEBAR_ARTICLE_COUNT = 10
# 侧边栏评论数目
SIDEBAR_COMMENT_COUNT = 5

# 分页
PAGINATE_BY = 10
# http缓存时间
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'locmemcache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 10
CACHE_MIDDLEWARE_KEY_PREFIX = "djangoblog"
CACHE_MIDDLEWARE_ALIAS = 'default'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = 'default'

OAHUTH = {
    'sina': {
        'appkey': os.environ.get('SINA_APP_KEY'),
        'appsecret': os.environ.get('SINA_APP_SECRET'),
        'callbackurl': 'http://www.elezt.cn/oauth/authorize?type=weibo'
    },
    'google': {
        'appkey': os.environ.get('GOOGLE_APP_KEY'),
        'appsecret': os.environ.get('GOOGLE_APP_SECRET'),
        'callbackurl': 'http://www.elezt.cn/oauth/authorize?type=google'
    },
    'github': {
        'appkey': os.environ.get('GITHUB_APP_KEY'),
        'appsecret': os.environ.get('GITHUB_APP_SECRET'),
        'callbackurl': 'http://www.elezt.cn/oauth/authorize?type=github'
    }
}

SITE_ID = 1
BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=https://www.elezt.cn&token=&type=original"

# Emial:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
# 设置debug=false 未处理异常邮件通知
ADMINS = [('elezt', 'eleztian@gmail.com')]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'djangoblog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]
