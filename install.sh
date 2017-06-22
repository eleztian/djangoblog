#!/bin/sh

sudo mkdir /var/www/DjangoBlog
sudo cp -R * /var/www/DjangoBlog
sudo pip3 install virtualenv
sudo mkdir /var/www/dev && cd /var/www/dev
sudo irtualenv -p /usr/bin/python3 python3 --system-site-packages
sudo source python3/bin/activate
cd /var/www/DjangoBlog
sudo pip3 install -r requirements.txt
sudo pip3 install gunicorn
python3 /var/www/DjangoBlog/manage.py makemigrations
python3 /var/www/DjangoBlog/manage.py migrate
python3 /var/www/DjangoBlog/manage.py collectstatic
sudo rm -rf /var/DjangoBlog/run
sudo ./bin/django_start
sudo apt install -y supervisor
sudo mv /var/www/DjangoBlog/bin/djangoblog.conf /etc/supervisor/conf.d
sudo supervisorctl update
sudo supervisorctl reload

sudo mv /var/www/DjangoBlog/bin/example.com.conf /etc/nginx/sites-available/djangoblog.conf
sudo ln -s /etc/nginx/sites-available/djangoblog.conf /etc/nginx/sites-enabled/djangoblog.conf

sudo service restart
