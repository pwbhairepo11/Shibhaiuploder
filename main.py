from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import m3u8
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from helper import get_drm_keys
from logger import logging
import time
from pyrogram.types import User, Message
from config import *
import sys
import os
import random
import re
import tempfile
import urllib.parse
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import datetime
import aiohttp
import asyncio
import http.client
import cloudscraper
import os
from pyrogram import Client, filters

photo1 = 'https://envs.sh/PQ_.jpg'
getstatusoutput(f"wget {photo1} -O 'photo.jpg'")    
photo = "photo.jpg"

#Bot Created by @NtrRazYt
# Define the owner ID
owner_id = 6977768796

# Initialize bot with environment variables
bot1 = Client(
    "bot1",
    bot_token="8179018409:AAFJXakzOiUGV2QNBg-ZfmAAWShJhC2ifc4",
    api_id=28460032,
    api_hash="1457c3ba64719a1e442aae67217b67c2"
)

# List to store authorized users
authorized_users = [6977768796]

cookies_file_path = os.getenv("COOKIES_FILE_PATH", "youtube_cookies.txt")

# Command to authorize a user
@bot1.on_message(filters.command("auth") & filters.private)
async def authorize_user(client, message):
    global authorized_users
    if message.from_user.id == owner_id:  # Ensure only the owner can authorize
        try:
            user_id = int(message.text.split()[1])
            if user_id not in authorized_users:
                authorized_users.append(user_id)
                await message.reply("User authorized successfully.")
            else:
                await message.reply("User is already authorized.")
        except (IndexError, ValueError):
            await message.reply("Please provide a valid user ID.")
    else:
        await message.reply("You are not authorized to use this command.")
    
@bot1.on_message(filters.command("cookies") & filters.private)
async def request_cookies(client, message):
    if message.from_user.id == owner_id:
        await message.reply("Please send me the new cookies as a text file (e.g., `cookies.txt`).")
        
        # Wait for the next message containing a document (file) from the user
        new_message = await bot1.listen(message.chat.id, timeout=30)
        if new_message and new_message.document:  # Check if a document was sent
            # Download the document to a temporary file
            file_path = await new_message.download()
            
            # Read the file content and overwrite cookies_file_path
            with open(file_path, "r") as temp_file:
                cookies_content = temp_file.read()
            with open(cookies_file_path, "w") as cookies_file:
                cookies_file.write(cookies_content)
            
            await message.reply("Cookies have been updated successfully.")
        else:
            await message.reply("No valid file provided. Operation canceled.")
    else:
        await message.reply("You are not authorized to use this command.")


# Function to check authorization
async def is_authorized(user_id):
    return user_id in authorized_users or user_id == owner_id

                                                                                       
# Extras 
failed_links = []  # List to store failed links
fail_cap =f"**➜ This file Contain Failed Downloads while Downloding \n You Can Retry them one more time **"

# counter 
global videocount, pdfcount  # Declare videocount and pdfcount as global variables

#url var 
pwdl = os.environ.get("api")

processing_request = False  # Variable to track if a request is being processed


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/sumtwo",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/sumtwo",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/anonyupdates",
            ),
            
        ],
    ]
)



Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/sumtwo",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://t.me/sumtwo",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Join to Check My Status ",
                url="https://t.me/anonyupdates",
            ),
            
        ],
    ]
)


@bot1.on_message(filters.command(["logs"]) )
async def send_logs(bot: Client, m: Message):
    try:
        
        # Assuming `assist.txt` is located in the current directory
         with open("Assist.txt", "rb") as file:
            sent= await m.reply_text("**📤 Sending you ....**")
            await m.reply_document(document=file)
            await sent.delete(True)
    except Exception as e:
        await m.reply_text(f"Error sending logs: {e}")


# List of image URLs
image_urls = [
    "http://graph.org/file/1952368384059649513e1.jpg",
    "http://graph.org/file/8678c337223acb5b4dffb.jpg",
    "http://graph.org/file/f00ef9f87f094bbddf0df.jpg",
    "http://graph.org/file/1952368384059649513e1.jpg",
    "http://graph.org/file/8678c337223acb5b4dffb.jpg",
    "http://graph.org/file/f00ef9f87f094bbddf0df.jpg",
    # Add more image URLs as needed
]

@bot1.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Send a loading message with emoji
    loading_message = await bot.send_message(
        chat_id=message.chat.id,
        text="Loading... ⏳🔄"
    )
  
    # Choose a random image URL from the list
    random_image_url = random.choice(image_urls)
    
    # Caption for the image
    caption = (
        "**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫  👋!\n\n"
        "➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n"
        "➠ Can Extract Videos & Pdf From Your Text File and Upload to Telegram\n\n"
        "➠ 𝐔𝐬𝐞 /ghost 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞\n\n"
        "➠𝐌𝐚𝐝𝐞 𝐁𝐲: @sumtwo **"
    )

    # Send the image with the caption
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )

@bot1.on_message(filters.command('h2t'))
async def run_bot(bot: Client, m: Message):
    user_id = m.from_user.id
    if user_id not in auth_users:
        await m.reply_text("**HEY BUDDY THIS IS ONLY FOR MY ADMINS TO USE THIS CONATCH MY DEV : @sumtwo  **")
    else:
        editable = await m.reply_text(" Send Your HTML file\n")
        input: Message = await bot.listen(editable.chat.id)
        html_file = await input.download()
        await input.delete(True)
        await editable.delete()
        with open(html_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            tables = soup.find_all('table')
            videos = []
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()
                    link = cols[1].find('a')['href']
                    videos.append(f'{name}:{link}')
        txt_file = os.path.splitext(html_file)[0] + '.txt'
        with open(txt_file, 'w') as f:
            f.write('\n'.join(videos))
        await m.reply_document(document=txt_file,caption="Here is your txt file.")
        os.remove(txt_file)



def is_subscription_expired(user_id):
    with open("Subscription_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if int(data[0]) == user_id:
                end_date = datetime.datetime.strptime(data[2], "%d-%m-%Y") #%Y-%m-%d
                today = datetime.datetime.today()
                return end_date < today
    return True  # User not found in Subscription_data.txt or no subscription data found



# Define the myplan command handler
@bot1.on_message(filters.command("myplan"))
async def myplan_command_handler(bot, message):
    user_id = message.from_user.id
    with open("Subscription_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if int(data[0]) == user_id:
                subscription_start = data[1]
                expiration_date = data[2]
                today = datetime.datetime.today()
                if today > datetime.datetime.strptime(expiration_date, "%d-%m-%Y"):
                    plan = "EXPIRED "
                    response_text = f"**✨ User ID: {user_id}\n📊 PLAN STAT : {plan}\n\n🔰 Activated on : {subscription_start}\n🧨 Expiration Date: {expiration_date} \n\n 🫰🏼 ACTIVATE YOUR PLAN NOW ! \n⚡️ TO ACTIVATE MESSAGE : @sumtwo :D **"
                else:
                    plan = "ALIVE!"  
                    response_text = f"**✨ User ID: {user_id}\n📊 PLAN STAT : {plan}\n🔰 Activated on : {subscription_start}\n🧨 Expiration Date: {expiration_date}**"
                await message.reply(response_text)
                return
    if user_id in auth_users:
        await message.reply("YOU HAVE LIFE TIME ACCESS :) ")
    else:
        await message.reply("No subscription data found for you.")


@bot1.on_message(filters.command("stop"))
async def restart_handler(_, m):
    
        if failed_links:
         error_file_send = await m.reply_text("**📤 Sending you Failed Downloads List Before Stoping   **")
         with open("failed_downloads.txt", "w") as f:
          for link in failed_links:
            f.write(link + "\n")
    # After writing to the file, send it
         await m.reply_document(document="failed_downloads.txt", caption=fail_cap)
         await error_file_send.delete()
         os.remove(f'failed_downloads.txt')
         failed_links.clear()
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("🚦**STOPPED**🚦", True)
         os.execl(sys.executable, sys.executable, *sys.argv)
        else:
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("🚦**STOPPED**🚦", True)
         os.execl(sys.executable, sys.executable, *sys.argv)
   

@bot1.on_message(filters.command("restart"))
async def restart_handler(_, m):
   
     processing_request = False  # Reset the processing flag
     await m.reply_text("🤖**Restarting Bot **🤖", True)
     os.execl(sys.executable, sys.executable, *sys.argv)
    

@bot1.on_message(filters.command(["drm"]))
async def account_login(bot: Client, m: Message):
    global processing_request
    if m.from_user.id not in authorized_users:
            await m.reply_text("** YOU ARE NOT IN ADMIN LIST **",reply_markup=keyboard)
            return
    else: 
        editable = await m.reply_text(f"**➠ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐀 𝐏𝐫𝐨𝐩𝐞𝐫 𝐖𝐚𝐲 \n\n➠ TXT FORMAT : LINK : URL \n➠ 𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲:  @sumtwo**")
        input: Message = await bot.listen(editable.chat.id)
        editable = await editable.edit(f"**⚙️PROCESSING INPUT.......**")

        if input.document:
            processing_request = True
            x = await input.download()        
            await input.delete(True)
            file_name, ext = os.path.splitext(os.path.basename(x))
            credit = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            path = f"./downloads/{m.chat.id}"

            try:
                links = []
                videocount = 0
                pdfcount = 0
                with open(x, "r", encoding="utf-8") as f:
                    for line in f:
                        link = line.strip().split("://", 1)
                        links.append(link)
                        if ".pdf" in link[1]:
                            pdfcount += 1 
                        else:
                            videocount += 1
            except Exception as e:
                await m.reply_text("Error occurred while processing the file.🥲")
                print("Error:", e)
                os.remove(x)
                processing_request = False  # Reset the processing flag
                return

        else:
            content = input.text
            content = content.split("\n")
            links = []
            videocount = 0
            pdfcount = 0

            for i in content:
                link = i.split("://", 1)
                links.append(link)
                if ".pdf" in link[1]:
                    pdfcount += 1 
                else:
                    videocount += 1
    await editable.edit(f"**Total links found are : {len(links)}\n┃\n┠ Total Video Count : {videocount}\n┠ Total Pdf Count: {pdfcount}  \n┠ Send From where you want to download initial is  : `1` \n┃\n┠ Send `stop` If don't want to Contine \n┖ Bot By : @SUMTWO*" )
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    if raw_text.lower() == "stop":
        await editable.edit(f"**Task Stoped ! **")
        await input0.delete(True)
        processing_request = False  # Reset the processing flag
        os.remove(x)
        return
    

    await editable.edit(f"**ENTER TILL WHERE YOU WANT TO DOWNLOAD \n┃\n┠ Starting Dowload Form : `{raw_text}`\n┖ Last Index Of Links is : `{len(links)}` **")
    input9: Message = await bot.listen(editable.chat.id)
    raw_text9 = input9.text
    
    if int(input9.text) > len(links) :
        await editable.edit(f"**PLZ ENTER NUMBER IN RANGE OF INDEX COUNT    **")
        processing_request = False  # Reset the processing flag
        await m.reply_text("**Exiting Task......  **")
        return
    else: await input9.delete(True)
    
    await editable.edit("𝗜𝗻 𝗖𝗮𝘀𝗲 𝗬𝗼𝘂𝗿 𝗧𝗫𝗧 , 𝗖𝗮𝗿𝗲𝗲𝗿𝘄𝗶𝗹𝗹 𝗮𝗽𝗽, 𝗦𝗲𝗻𝗱 𝗕𝗮𝘁𝗰𝗵 𝗧𝗼𝗸𝗲𝗻 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg' \n\n𝐎𝐑\n\n`KUSH`")
    input7: Message = await bot.listen(editable.chat.id)
    authkey = input7.text
    await input7.delete(True)
    

    await editable.edit("**Enter Batch Name or send d for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0


    # await editable.edit("**Enter resolution \n SEND 1 for 720p \n 2 for 480 \n 3 for 360 \n 4 for 240**")
    await editable.edit("**Enter resolution \n SEND 1 for 720p \n 2 for 480 \n 3 for 360 \n 4 for 240**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    quality = input2.text
    await input2.delete(True)
    
    
    await editable.edit("**Enter Your Name or send `de` for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = "ghost"
    else:
        CR = raw_text3


    await editable.edit("**🖼 Thumbnail \n\n• Custom Thumbnail : Use @vtelegraphbot and send me link \n• If you don't want Send :  `no` **")  
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    #await editable.delete()
    thumb = input6.text
    thumb2 = input6.text

    await editable.edit("**⚡️ Thumnail in PDF too ? \n\n• If need Same thumb on pdf as video send : `yes` \nNOTE : if you have given stumb for Video then only use this   \n• SEND `no` If you dont want to add \n\n• Want other thumbnail ? \n\n• Send `custom`  IF need Different thubnail for pdf **")  
    input7 = message = await bot.listen(editable.chat.id)
    raw_text7 = input7.text.lower()  # Convert to lowercase
    await input7.delete(True)
    

    if raw_text7 == "custom":
     await editable.edit("**Send URl of Pdf Thumbanil **")  
     input8 = message = await bot.listen(editable.chat.id)
     raw_text8 = input8.text.lower()  # Convert to lowercase
     await input8.delete(True)
     await editable.delete()
     thumb3 = input8.text 

    else: await editable.delete() 
      
    
    if thumb.startswith("http://") or thumb.startswith("https://"):
        # getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        getstatusoutput(f"wget {thumb} -O thumb1.jpg")
        thumb = "thumb1.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)
  
    try:
        for i in range(count - 1, int(input9.text)):
        #for i in range(count - 1, len(links)):    

            V = links[i][1].replace("file/d/","uc?export=download&id=")\
               .replace("www.youtube-nocookie.com/embed", "youtu.be")\
               .replace("?modestbranding=1", "")\
               .replace("/view?usp=sharing","")\
               .replace("youtube.com/embed/", "youtube.com/watch?v=")

            url = "https://" + V

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            if "edge.api.brightcove.com" in url:
                url=url.split("bcov_auth=")[0]+"bcov_auth="+authkey

            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            #elif 'videos.classplusapp' in url:
             #url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']
            
            elif "tencdn.classplusapp" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip() 
            name = f'{name1[:60]}'
              
            if "/master.mpd" in url :
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/","https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                else: 
                    url = url    

                print("mpd check")
                key = await helper.get_drm_keys(url)
                print(key)
                await m.reply_text(f"got keys form api : \n`{key}`")
          
            if "/master.mpd" in url:
                cmd= f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"bestvideo.{quality}"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            if "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "romeo.mp4"'
                #cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.%(ext)s"'
          
            else: 
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "romeo.mp4"'
                print("counted 2 ")
            
            # else
            #     cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:   
                cc = f' **➭ Index » {str(count).zfill(3)} **\n**➭ Title »  {name1}.mkv**\n**➭ 𝐁𝐚𝐭𝐜𝐡 » {b_name} **\n**➭ Quality » {raw_text2}**\n\n✨ **𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 : @shivanshu1bot\n**━━━━━━━✦✗✦━━━━━━━**'
                cc1 = f'**➭ Index » {str(count).zfill(3)} **\n**➭ Title » {name1}.pdf** \n**➭ 𝐁𝐚𝐭𝐜𝐡 »  {b_name}**\n\n✨ **𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 : @shivanshu1bot\n**━━━━━━━✦✗✦━━━━━━━**'                            
    
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        await copy.copy(chat_id = -1002097681261)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e: 
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        time.sleep(1)
                        #prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Index » {str(count).zfill(3)} **\n**➭ File » ** `{name}`\n**➭ Link »** `{url}`\n\n✨ **Bot Made by GHOST**\n**━━━━━━━✦✗✦━━━━━━━**")
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        time.sleep(1)
                        #await prog.delete (True)
                        start_time = time.time()
                        reply = await m.reply_text(f"**⚡️ Starting Uploding ...** - `{name}`")
                        time.sleep(1)
                        if raw_text7 == "custom" :
                           subprocess.run(['wget', thumb3, '-O', 'pdfthumb.jpg'], check=True)  
                           thumbnail = "pdfthumb.jpg"
                           copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                           os.remove(thumbnail)
                        elif thumb == "no" and raw_text7 == "no":
                        
                             copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, progress=progress_bar, progress_args=(reply, start_time))
                        elif raw_text7 == "yes" and thumb != "no":
                              subprocess.run(['wget', thumb2, '-O', 'thumb1.jpg'], check=True)  # Fixing this line
                              thumbnail = "thumb1.jpg"
                              copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1,thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                        else:
                            subprocess.run(['wget', thumb2, '-O', 'thumb1.jpg'], check=True)  
                            thumbnail = "thumb1.jpg"
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                        await reply.delete (True)
                        os.remove(f'{name}.pdf')
                        count += 1
                        time.sleep(2)
                    except FloodWait as e:
                        #await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                else:
                    prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Count » {str(count).zfill(3)} **\n**➭ Video Name » ** `{name}`\n**➭ Quality** » `{raw_text2}`\n**➭ Video Url »** `{url}`\n**➭ Thumbnail »** `{input6.text}` \n\n✨ **Bot Made by @sumtwo**\n**━━━━━━━✦✗✦━━━━━━━**")
                    time.sleep(2)
                    res_file = await helper.drm_download_video(url,quality, name, authkey)
                    filename = res_file
                    await prog.delete(True)
                    time.sleep(1)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, thumb2)
                    count += 1
                    

            except Exception as e:
                await m.reply_text(f"**This #Failed File is not Counted**\n**Name** =>> `{name1}`\n**Link** =>> `{url}`\n\n ** Fail reason »** {e}")
                failed_links.append(f"{name1} : {url}")
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    time.sleep(2)


    if failed_links:
     error_file_send = await m.reply_text("**📤 Sending you Failed Downloads List **")
     with open("failed_downloads.txt", "w") as f:
        for link in failed_links:
            f.write(link + "\n")
    # After writing to the file, send it
     await m.reply_document(document="failed_downloads.txt", caption=fail_cap)
     await error_file_send.delete()
     failed_links.clear()
     os.remove(f'failed_downloads.txt')
    await m.reply_text("🔰Done🔰")
    await m.reply_text("**✨Thanks for Choosing**")
    processing_request = False  # Reset the processing flag  


#-------------:::-----------------:::::--------------------::::::------------------------------------------------:::::-------------------------------
OWNER2 = int(os.environ.get("OWNER2", 6977768796))

try: 
    ADMINS = [] 
    for x in (os.environ.get("ADMINS", "6977768796, 6977768796").split()):  
        ADMINS.append(int(x)) 
except ValueError: 
    raise Exception("Your Admins list does not contain valid integers.") 

ADMINS.append(OWNER)

# Allowed users and channels
allowed_users = set(ADMINS)  # Initialize with ADMINS
authorized_channels = set()  # Keep track of authorized channels
codes = {}  # Store generated codes and their corresponding chat IDs


@bot1.on_message(filters.command(["code"]))
async def generate_code(bot: Client, m: Message):
    user_id = m.from_user.id
    if user_id != OWNER2:
        await m.reply_text("You do not have permission to use this command to get access contact @sumtwo.")
        return

    code = str(random.randint(100000, 999999))  # Generate a 6-digit code
    codes[code] = m.chat.id  # Store the code with the chat ID
    await m.reply_text(f"Your code is: {code}. Use this code to redeem.")


@bot1.on_message(filters.command(["redeem"]))
async def redeem_code(bot: Client, m: Message):
    if len(m.command) < 2:
        await m.reply_text("Please provide a code to redeem.")
        return
    
    code = m.command[1]
    if code in codes:
        chat_id = m.chat.id  # Get the chat ID where the code is redeemed
        authorized_channels.add(chat_id)  # Add the chat ID to authorized channels
        await m.reply_text(f"Chat {chat_id} has been authorized!")
        del codes[code]  # Remove the code after redemption
    else:
        await m.reply_text("Invalid code or code has already been used.")


@bot1.on_message(filters.command(["GHOST"]))
async def account_login(bot: Client, m: Message):
    user_id = m.from_user.id if m.from_user else None
    chat_id = m.chat.id

    # Check if the user or chat is authorized
    if user_id not in allowed_users and chat_id not in authorized_channels:
        await m.reply_text("**You are not authorized to use this command.**")
        return

    editable = await m.reply_text('𝗦𝗘𝗡𝗗 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗙𝗢𝗥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗖𝗢𝗨𝗥𝗦𝗘 𝗔𝗡𝗗 𝗨𝗣𝗟𝗢𝗔𝗗 𝗧𝗢 [...]')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await bot.send_document(961916589, x)
    await input.delete(True)


    path = f"./downloads/bot1/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
    #    os.remove(x)
       await m.reply(links[0])
    #    print(links)
    except Exception as e:
           await m.reply_text("Invalid file input.")
           os.remove(x)
           print(e)
           return
       
    await editable.edit(f"**𝐓𝐨𝐭𝐚𝐥 𝐥𝐢𝐧𝐤𝐬 𝐟𝐨𝐮𝐧𝐝 𝐚𝐫𝐞**{len(links)}**\n\n𝗦𝗲𝗻𝗱 𝗙𝗿𝗼𝗺 𝘄𝗵𝗲𝗿𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝗻𝗶𝘁𝗶𝗮𝗹 𝗶𝘀 **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝐄𝐧𝐭𝐞𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝐄𝐧𝐭𝐞𝐫 𝐫𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("**𝐄𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐧𝐚𝐦𝐞 𝐦𝐮𝐬𝐭**\n\n**𝐎𝐑**\n\n`[—(••÷[ Ghost ]÷••)— ]`")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Co':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/0633f8b6a6f110d34f044.jpg```\n\nor Send `no`")
    
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()
    thumb = input6.text
    x=await m.reply("If classpluss send token or\nSEND\n\n`Jai Shree Ram`")
    input7: Message = await bot.listen(editable.chat.id)
    classplus_token = input7.text
    await input7.delete(True)
    await x.delete()

    
    
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            if "visionias" in url:    
                async with ClientSession() as session:    
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                         'Accept-Language': 'en-US,en;q=0.9', 
                                                         'Cache-Control': 'no-cache', 
                                                         'Connection': 'keep-alive', 
                                                         'Pragma': 'no-cache', 
                                                         'Referer': 'http://www.visionias.in/', 
                                                         'Sec-Fetch-Dest': 'iframe', 
                                                         'Sec-Fetch-Mode': 'navigate', 
                                                         'Sec-Fetch-Site': 'cross-site', 
                                                         'Upgrade-Insecure-Requests': '1', 
                                                         'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                                                         'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 
                                                         'sec-ch-ua-mobile': '?1', 
                                                         'sec-ch-ua-platform': '"Android"',}) as resp:    
                        text = await resp.text()    
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            
            # print(urls)
            elif "tencdn.classplusapp" in url or "cpvod.testbook" in url or "webvideos.classplusapp.com" in url or "cpvod.testbook" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'Host': 'api.classplusapp.com', 'x-access-token': classplus_token, 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}).json()['url']

            #elif 'cpvod.testbook' in url:
             #url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'
            if links[i][0].startswith("("):
                name5_match = re.search(r'\((.*?)\)', links[i][0])
                name5 = name5_match.group(1) if name5_match else "Unknown Subject"
            else:
                name5_match = re.match(r'^(.*?)(?=\s*[^a-zA-Z0-9\s])', links[i][0])
                if name5_match:
                    name5 = name5_match.group(1).strip()  # Get the first word
                else:
                    name5 = "Unknown Subject"
            if "/master.mpd" in url :
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/","https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                else: 
                    url = url    

                print("mpd check")
                key = await helper.get_drm_keys(url)
                print(key)
                await m.reply_text(f"got keys form api : \n`{key}`")
          
            if "/master.mpd" in url:
                cmd= f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")

            

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "@sumtwo_{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "@sumtwo_{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "@sumtwo_{name}.mp4"'

            try:
                cc = (
                      f"{str(count).zfill(3)}\n"
                      f"**Title** : **{name1}.mkv**\n\n"
                      f"**Batch Name** : **{raw_text0}**\n\n"  # Fixed  brac
                      f"**Downloaded By** : **{raw_text3}**"
                       )

                ccyt = (
                        f"——— ✦ {str(count).zfill(3)} ✦ ———\n"
                        f"🎞️ **Subject** : {name5}\n\n"
                        f"🎞️ **Title** : {name1}\n\n"
                        f"📚 **Batch Name** : {raw_text0}\n\n"
                        f"📽️ **Video Link** : {url}\n"
                      )

                      # Formatting for PDF
                cc1 = (
                       f"{str(count).zfill(3)}\n"
                      f"**Title** : **{name1}.pdf**\n\n"
                      f"**Batch Name** : **{raw_text0}**\n\n"  # Fixed  brac
                      f"**Downloaded By** : **{raw_text3}**"
                     )

                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id= -1002427525007)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'@sumtwo_{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=chat_id, document=f'@sumtwo_{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'@sumtwo_{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        await asyncio.sleep(2)  # Use asyncio.sleep for non-blocking sleep
                        return  # Exit the function to avoid continuation

                    except Exception as e:
                        await m.reply_text(f"An error occurred: {str(e)}")
                        await asyncio.sleep(4)  # You can replace this with more specific
                        continue
                       
                else:
                    Show = f"**🌩𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐕𝐈𝐃𝐄𝐎🌩**\n\n𝗟𝗢𝗖𝗔𝗧𝗜𝗢𝗡 :- ❤️𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗙𝗢𝗟𝗗𝗘𝗥❤️"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**Link** - {url}"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**🤡DONE🤡**")



    
  
processing_request = False
bot1.run()
