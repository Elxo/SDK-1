# Pinned to the exact PHP patch release so every student builds an identical image.
# PHP 8.4 is supported until 2028-12-31; 8.2 goes fully end-of-life on 2026-12-31.
FROM php:8.4.25-apache

RUN a2enmod rewrite

COPY . /var/www/html

# Composer is pinned too - "composer:latest" would silently change between builds.
COPY --from=composer:2.10.3 /usr/bin/composer /usr/bin/composer

RUN apt-get update && apt-get install -y --no-install-recommends unzip libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install pdo pdo_pgsql

RUN composer install --no-interaction

# Configure Apache DocumentRoot to public
ENV APACHE_DOCUMENT_ROOT /var/www/html/public

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf
RUN sed -ri -e 's!AllowOverride None!AllowOverride All!g' /etc/apache2/apache2.conf
