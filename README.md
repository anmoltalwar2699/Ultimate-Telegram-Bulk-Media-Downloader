Ultimate Telegram Bulk Media Downloader
A straightforward Telegram media downloader that allows you to download media from public and private groups with ease. Follow the steps below to get started.

Download the Source Code
Pre-Requisites
Python: Version 3.11 or higher
pip: Version 24.2 or higher
To verify your installations, run the following commands in your command prompt:

$python --version
$ pip --version

Required Libraries
After installing Python and pip, install the necessary libraries using these commands:

$pip install telethon

$pip install python-dotenv

Installation
Download the Tele Downloader folder from the repository.
Open the command prompt and navigate to the Tele Downloader folder. Example:
cd C:\Users\"User"\Downloads\Tele Downloader
Alternatively, you can open the Tele Downloader folder, type cmd in the address bar at the top, and press Enter. This will open the command prompt directly in the folder.

Usage
In the Tele Downloader folder, open the Credentials.env file using Notepad.

Replace the API ID and API Hash with the credentials you obtain from Telegram. To get these credentials, follow the instructions here: Obtaining Telegram API ID & Hash.

For Session Name, you can use any name you like. This will create a session file that allows you to avoid logging in every time you use the script unless the session expires.

Save the Credentials.env file after making the changes and close it.

Open the command prompt and navigate to the folder again:

cd C:\Users\"User"\Downloads\Tele Downloader
Alternatively, open the Tele Downloader folder and type cmd in the address bar, then press Enter.

Run the script using the following command:
$ python script.py

The script will prompt you to log in. Enter your phone number in the format:
+(country code) phone number
Example for the USA: +11234567890

Enter the code you receive for login. If you have 2FA enabled, you will also need to enter your 2FA password. The password input will be hidden for security, so just type it and press Enter.

The script will then ask you to enter the Chat ID or group link. For public groups, enter the link. For private groups, you will need the Chat ID, which you can find using a Telegram bot like @getidsbot.

Note: We do not own or take responsibility for any third-party bots or tools used to obtain Chat IDs.

After entering the Chat ID or link, the script will begin downloading media. It will create a downloads folder inside the Tele Downloader folder, where all the media will be saved.
Important Note:
This script complies with Telegram’s Terms of Service. It is a simple tool for downloading media from groups. Any misuse of this tool in violation of Telegram’s rules could result in suspension or banning of your account. Please use this tool responsibly.

