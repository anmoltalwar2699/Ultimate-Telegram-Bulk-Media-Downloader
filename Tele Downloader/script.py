import os
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv

# Load environment variables from Credentials.env
load_dotenv(dotenv_path='Credentials.env')

# Retrieve API credentials and session name
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

# Debugging: Print the loaded API credentials to verify
print(f"API_ID: {api_id}, API_HASH: {api_hash}, SESSION_NAME: {session_name}")

# Create Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Create the downloads folder if it doesn't exist
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
    print(f"Created folder: {DOWNLOAD_FOLDER}")

async def download_media(message):
    """Download media from a Telegram message if it contains any."""
    try:
        if message.media:
            # Define the path to download the media into the downloads folder
            file_path = await message.download_media(file=DOWNLOAD_FOLDER)
            print(f"Downloaded media to: {file_path}")
        else:
            print("No media found in this message.")
    except Exception as e:
        print(f"Failed to download media from message: {e}")

async def download_from_chat(chat_id):
    """Iterate through messages in a chat and download all media files."""
    print(f"Starting to download media from chat: {chat_id}")

    # Convert the chat_id to an integer if it's a chat ID (starts with -100)
    if chat_id.startswith('-100'):
        chat_id = int(chat_id)

    # Try to fetch the entity to check if it exists and is accessible
    try:
        entity = await client.get_entity(chat_id)
        print(f"Successfully fetched entity: {entity}")
    except ValueError as e:
        print(f"Failed to fetch entity: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    tasks = []
    message_count = 0  # Track how many messages have been processed
    last_message_id = 0  # Start from the most recent message

    while True:
        try:
            # If last_message_id is None, start from the latest message
            async for message in client.iter_messages(entity, offset_id=last_message_id):
                if message.media:
                    tasks.append(download_media(message))
                    message_count += 1
                    last_message_id = message.id  # Update last processed message ID

                # Print a progress update for every 100 messages processed
                if message_count % 100 == 0:
                    print(f"Processed {message_count} messages so far...")

            # Break the loop if all messages have been processed
            break
        except Exception as e:
            print(f"Connection error or limit reached: {e}. Retrying from message ID: {last_message_id}")
            await asyncio.sleep(5)  # Wait 5 seconds before retrying
            continue

    # Use asyncio.gather for parallel downloads
    await asyncio.gather(*tasks)
    print(f"Finished downloading media from chat: {chat_id}")

async def main():
    """Main function to start the Telegram client and manage media downloads."""
    print("Starting Telegram Client...")
    await client.start()

    # Handle login and 2FA if needed
    if not await client.is_user_authorized():
        try:
            phone = input("Enter your phone number (with country code): ")
            await client.sign_in(phone)
            # If 2FA is enabled, prompt for the password
            code = input("Enter the code you received: ")
            await client.sign_in(code=code)
        except SessionPasswordNeededError:
            password = input("Please enter your 2FA password: ")
            await client.sign_in(password=password)
    
    print("Logged in as:", await client.get_me())
    
    # Get chat ID or username
    chat_id = input("Enter the chat ID, username, or invite link (for public groups): ")

    # Download media from the chat
    await download_from_chat(chat_id)

with client:
    client.loop.run_until_complete(main())
