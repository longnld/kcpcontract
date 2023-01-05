from celery import  Celery
from celery import shared_task
from .telegram import kc_project_alert,test_msg
from .auto_email_report import send_report
@shared_task
def email_report_and_telegram_annouce():
	send_report()
	kc_project_alert()

@shared_task
def test_msg_task():
	test_msg()