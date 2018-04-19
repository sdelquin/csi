import config
import datetime
import locale


def handle_dates(year):
    event_datetime = datetime.datetime.strptime(
        config.EDITIONS[year]["EVENT_DATETIME"],
        "%d/%m/%YT%H:%M"
    )
    days_to_go = (event_datetime - datetime.datetime.now()).days
    locale.setlocale(locale.LC_TIME, "es_ES")
    event_datetime_as_string = event_datetime.strftime(
        "%A %d de %B de %Y @ %H:%Mh"
    ).title().replace("De", "de")
    limitdate_signup = event_datetime - datetime.timedelta(
        days=config.EDITIONS[year]["DAYS_TO_SIGNUP"]
    )
    limitdate_signup_as_string = limitdate_signup.strftime(
        "%d de %B de %Y"
    ).title().replace("De", "de")
    return (
        days_to_go,
        event_datetime_as_string,
        limitdate_signup_as_string
    )
