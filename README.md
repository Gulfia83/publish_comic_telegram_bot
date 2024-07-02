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

5. Run the script using the `python main.py` command on the command line.

### Code Description

1. The `get_last_comic_number` function gets the number of the last comic on the XKCD website.
4. The `get_random_comic` function retrieves information about a random comic, including the image URL and comment.
5. The `send_comic_to_TG_chat` function sends a comment and an image of a random comic to the specified Telegram channel. After publication, the photo of the comic is removed from the directory.

### Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).