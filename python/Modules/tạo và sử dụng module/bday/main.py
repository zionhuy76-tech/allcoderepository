import datetime, bday_messages

today = datetime.date.today()
next_bday = datetime.date(2026, 9, 13)
days_away = next_bday - today
if days_away.days == 0:
    print(bday_messages.random_message)
else:
    print(f"My birthday is in {days_away.days} days.")
