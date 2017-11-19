# coding:utf-8
"""
Django settings for minicms project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eaatdw+e9!o16&)@esloy%hr91yw!%l=v3csmd$6ayv=8x^@lx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'news',
    'userdata',
    'column',
    'meeting',
    'article',
    'guide',
    'expert',
    'other',
    'universal',
    'nursing',
    'sruco',
    'recommend',
    'subject',
    'association',
    'magazine',
    'video',
    'DjangoUeditor',
)
COMMENTS_APP = 'column'
SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'minicms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'news.nav_processor.nav_column',
            ],
        },
    },
]

WSGI_APPLICATION = 'minicms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'miniao',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
SUIT_CONFIG = {
    'ADMIN_NAME': '苹果树',
    'HEADER_DATE_FORMAT': 'Y年m月j日 l',
    'HEADER_TIME_FORMAT': 'H:i',
    'MENU': ({'label': 'ABC',
              'app': 'news',
              'models': ('Article', 'Column',)
              },
             {'label': '轮播图',
              'app': 'other',
              'models': ('Lunbopic',)
              },
             {'label': '用户',
              'app': 'userdata',
              'models': ('Userinfo',)
              },
             {'label': '资讯',
              'app': 'column',
              'models': ('Infoarticle',)
              },
             {'label': '会议',
              'app': 'meeting',
              'models': ('Meetarticle', 'Meetspecial',)
              },
             {'label': '文章',
              'app': 'article',
              'models': ('Artiarticle',)
              },
             {'label': '视频',
              'app': 'video',
              'models': ('Videoarticle',)
              },
             {'label': '指南速递',
              'app': 'guide',
              'models': ('Guidearticle',)
              },
             {'label': '专家风采',
              'app': 'expert',
              'models': ('Interviewarticle', 'Expertarticle', 'Comment',)
              # 'models': ('Interviewarticle', 'Doctorarticle', 'Expertarticle', 'Comment',)
              },
             {'label': '其它',
              'app': 'other',
              'models': ('Friend', 'Standardarticle',)
              # 'models': ('Friend', 'Standardarticle', 'Resourcearticle',)
              },
             {'label': '科普园地',
              'app': 'universal',
              'models': ('Universalarticle',)
              },
             {'label': '护理园地',
              'app': 'nursing',
              'models': ('Nursingarticle',)
              },
             {'label': 'SRUCO',
              'app': 'sruco',
              'models': ('Srucoarticle',)
              },
             {'label': '泌尿学会',
              'app': 'association',
              'models': ('Peoplearticle', 'Assocarticle', 'Dynamicarticle',)
              },
             {'label': '药械推荐',
              'app': 'recommend',
              'models': ('Recommendarticle',)
              },
             {'label': '优势学科',
              'app': 'subject',
              'models': ('Subjectarticle',)
              },
             {'label': '杂志',
              'app': 'magazine',
              'models': ('Mageinfo', 'Magearticle',)
              },
             ),

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "common_static"),
#)
STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "common_static"),
    ("admin", os.path.join(STATIC_ROOT, 'admin')),
    ("cms", os.path.join(STATIC_ROOT, 'cms')),
    ("suit", os.path.join(STATIC_ROOT, 'suit')),
    ("ueditor", os.path.join(STATIC_ROOT, 'ueditor')),
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
