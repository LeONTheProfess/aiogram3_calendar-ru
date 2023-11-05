# Date Selection tool for Aiogram Telegram Bots

## Description
A simple inline calendar, date selection tool for [aiogram](https://github.com/aiogram/aiogram) telegram bots written in Python.
Offers two types of date pickers:
Navigation calendar - user can either select a date or move to the next or previous month/year by clicking a singe button.
Dialog calendar - user selects year on first stage, month on next stage, day on last stage

## Usage
1. Clone this repo into your project;
2. 
```python  
from aiogram3_calendar_ru import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar 
```

A full working example on how to use aiogram-calendar is provided in *example_bot.py*. 
You create a calendar and add it to a message with a *reply_markup* parameter and then you can process it in a ```callback_query``` method using the *process_selection* method.

## Gif demo:

![aiogram_calendar](https://j.gifs.com/nRQlqW.gif)
