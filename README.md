# blog_django_rest_framework
> A Vue.js and Django project

## Setup Guide


## DJANGO
``` bash

# Create Django Environment
conda create --name myEnv

# Activate Django Environment
activate myEnv

# Install Django
pip install django

# Create our Project
django-admin startproject djangovue

# Change our directory to our project
cd first_project

# Create you application
django-admin startapp app

# Install Webpack Loader
pip install django-webpack-loader

# Install Cors
pip install django-cors-headers

# TEST our DJANGO project

# Create new migration based on models changes
python manage.py makemigrations
python manage.py migrate

# Run application (will be hosted in 127.0.0.1:8000)
python manage.py runserver

# To change port of application
python manage.py runserver {portnumber}
```

## VUEjs
## Requirements
> Nodejs
> Vue-CLI

``` bash

# Create Vue project
vue init webpack-simple frontend

# Change directory to newly created vuejs project
cd frontend

# Install npm
npm install

# Install webpack-bundle-tracker
npm install --save-dev webpack-bundle-tracker

# Install write-file-webpack-plugin
npm install write-file-webpack-plugin --save-dev

# Install vue-resource
npm install vue-resource

# Install vue router
npm install --save vue-router

# Install vuex
npm install --save vuex

# Test run
npm run dev 

```

## Configurations 

### settings.py
```bash

# Under INSTALLED_APPS, register webpack-loader as:
INSTALLED_APPS=[
    '',
    '',
    '',
    'webpack_loader',
]

# also Add  mock configurations for webpack-loader
WEBPACK_LOADER={
    'DEFAULT':{
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME':'',
        'STATS_FILE': os.path.join(BASE_DIR,'frontend/webpack-stats.json'),
        'POLL_INTERVAL':0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

```

### Webpack.config.js

```bash
# import webpack-bundle-tracker and webpack-file-webpack-plugin

var BundleTracker  = require('webpack-bundle-tracker')
var WriteFilePlugin = require('write-file-webpack-plugin')

# write some plugins under modul section

plugins: [
    new BundleTracker({
      path: __dirname,
      filename: './webpack-stats.json'
    }),
    new WriteFilePlugin()
  ],

# we need to configure directory in which index.html file will fetch generated bundled js and vue frontend part
output: {
    '',
    '',
    publicPath: 'http://localhost:8080/dist/',
  },

```

## if want to try with simple display of index template follow below..
## index.html 

```bash
# this file will help to render components and changes which will be done in vue frontend part

#first we need to import our webpack bundle as
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html>
<head>
    .
    .   
    .

# Create div as index.html in vue frontend
<div id='app'></div>

# Render_bundle will render the proper <script> and <link> tags needed in our template.
{% render_bundle 'main'%}

```

## urls.py
> to configure default rout
```bash
# Add urlpatterns as:
from django.views.generic import TemplateView

urlpatterns = [
    '',
    path('',TemplateView.as_view(template_name='index.html'))
]
```

Since all files are configured. Now we will be able to access index.html through django server
