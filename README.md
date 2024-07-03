# Comics publisher on TELEGRAM

[Russian](RU_README.md)

The project is an automatic tool for publishing random comics from the XKCD website in a specified telegram channel.

### How to install

1. Clone the repository to your local computer.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project.
4. Add the following variables to the `.env` file:
 - `TELEGRAM_BOT_TOKEN` - your bot token.
 - `TELEGRAM_CHAT_ID` - id of your telegram channel.

### Example of launching in the console and outputting in Telegram

Run the script using the `python main.py` command on the command line.

```console
python main.py
```

#### Output in Telegram

![Снимок](https://github.com/Gulfia83/publish_comic_telegram_bot/assets/168065597/b558a403-da8a-4b01-9fe7-42810beb19b4)

### Code Description

1. The `get_last_comic_number` function gets the number of the last comic on the XKCD website.
2. The `download_random_comic` function retrieves information about a random comic, including the image URL and comment.
3. The `send_comic_to_tg_chat` function sends a comment and an image of a random comic to the specified Telegram channel.

### Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).
