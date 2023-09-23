import datetime

import django.utils.timezone
import django
from django.core.mail import send_mail
from django.conf import settings

from mailing.models import Logs, MailingSettings, Message


def _send_email(message_settings, message_client, message):
    print('start')
    result = send_mail(
        subject=message.theme,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[message_client.email],
        fail_silently=False,
    )

    Logs.objects.create(
        status=Logs.STATUS_OK if result else Logs.STATUS_FAILED,
        mailing=message_settings,
    )


def send_mails():
    now = django.utils.timezone.datetime.now()
    datetime_now = now.time()
    for mailing_setting in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):

        message = mailing_setting.message_set.filter(status=Message.TO_BE_SENT).first()

        if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):

            for mailing_client in mailing_setting.client.all():

                mailing_log = Logs.objects.filter(
                    client=mailing_client,
                    mailing=mailing_setting
                )

                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_try').first().last_try

                    if mailing_log.period == MailingSettings.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_email(mailing_setting, mailing_client, message)
                    elif mailing_log.period == MailingSettings.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            _send_email(mailing_setting, mailing_client, message)
                    elif mailing_log.period == MailingSettings.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 30:
                            _send_email(mailing_setting, mailing_client, message)

                else:
                    _send_email(mailing_setting, mailing_client, message)







