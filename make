python3 manage.py runserver
celery -A subscription_service worker -l info
sudo python3 -m smtpd -n -c DebuggingServer localhost:25

