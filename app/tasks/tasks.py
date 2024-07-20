from pydantic import EmailStr

from app.config import settings
from app.tasks.celery_con import celery
from PIL import Image
from pathlib import Path
import smtplib

from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def process_picture(path: str):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized = img.resize((1000, 500))
    img_resized.save(f"app/static/images/resized_{img_path.name}")


@celery.task
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr
):
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        try:
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
        except Exception as e:
            print(e)
        server.send_message(msg_content)
