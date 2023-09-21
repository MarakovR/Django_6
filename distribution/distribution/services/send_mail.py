import django.utils.timezone

from django.core.mail import send_mail
from django.conf import settings

from distribution.models import Logs, MailingSettings, Message


def _send_email(client, mailing, message):
    result = send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email],
        fail_silently=False,
    )
    print(result)
    Logs.objects.create(
        mailing_list=mailing,
        client=client,
        status=result,
    )


def send_mails():
    now = django.utils.timezone.datetime.now()
    now_time = now.time()

    for mailing in MailingSettings.objects.filter(status=MailingSettings.STARTED):
        print(mailing)

        if mailing.start_time < now_time < mailing.end_time:

            for mailing_client in mailing.client.all():

                message = mailing.message_set.filter(status=Message.TO_BE_SENT).first()
                print(message)

                if message is None:
                    return

                log = Logs.objects.filter(
                    client=mailing_client,
                    mailing_list=mailing
                )

                if log.exists():

                    last_try_date = log.order_by('-time').first().time.replace(tzinfo=None)

                    if mailing.periodicity == MailingSettings.DAILY:
                        if (now - last_try_date) >= MailingSettings.DAILY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingSettings.WEEKLY:
                        if (now - last_try_date) >= MailingSettings.WEEKLY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingSettings.MONTHLY:
                        if (now - last_try_date) >= MailingSettings.MONTHLY:
                            _send_email(mailing_client, mailing, message)

                else:
                    _send_email(mailing_client, mailing, message)

            message.status = Message.SHIPPED
            message.save()
