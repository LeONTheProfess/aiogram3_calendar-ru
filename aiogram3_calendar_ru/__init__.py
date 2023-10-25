# flake8: noqa
import aiogram
assert aiogram.__version__.split('.')[0] == '3', 'Current module requires aiogram package version 3.x.x'

from aiogram3_calendar_ru.simple_calendar import SimpleCalendarCallback as simple_cal_callback, SimpleCalendar
from aiogram3_calendar_ru.dialog_calendar import DialogCalendarCallback as dialog_cal_callback, DialogCalendar
