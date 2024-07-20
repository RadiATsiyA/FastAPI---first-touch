from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email["Subject"] = "Booking confirmation"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            You booked a room in hotel: Bugu Hotel, Bishkek, Chuy avenue from {booking["date_from"]} to {booking["date_to"]}
            <h1>Confirm your booking by clicking on the link bellow
            within 30 minutes or your booking will be canceled</h1>
            <h2>[% user.confirmation_token %]</h2>
        """,
        subtype="html"
    )

    return email

