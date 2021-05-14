import instagrapi
from instagrapi import Client
import discord
import PIL.ImageDraw
import PIL.Image
import PIL.ImageFont
from discord.ext import commands
import io
from pathlib import Path
import requests
import shutil
import textwrap
import datetime
from address import Address
import image_maker
from image_maker import image_maker

# get credentials
with open("./token_RnD.txt") as f:
    TOKEN = f.readlines()

instagram log in
bot = Client()
username = TOKEN[1]
password = TOKEN[2]
bot.login(username, password)
print("Logged in")

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    # check discord messages
    garb2 = ["verified", "Verified"]
    place = ""
    adrs = Address()
    if str(message.channel) == "confirmed-availibility" and len(message.content.split()) > 0:
        msgs = message.clean_content.splitlines()

        for num, msg in enumerate(msgs):
            words = msg.split()
            for count, word in enumerate(words):
                if "#" in word:
                    if adrs.hash_address(word) is True:
                        words[count] = word[1:]
                    msgs[num] = "\n".join(textwrap.wrap(" ".join(words), 35))
                else:
                    msgs[num] = "\n".join(textwrap.wrap(msg, 35))

        text = "\n".join(msgs)
        text = text + "\n\nVerification time - {}, {}".format(datetime.datetime.now().strftime("%H:%M"),
                                                                             datetime.date.today())

        # get the attachment image
        for num, attach in enumerate(message.attachments):
            url = attach.url
            r = requests.get(url, stream=True)
            screenshot_name = "ss{}.jpeg".format(num)
            with open(screenshot_name, "wb") as out_file:
                shutil.copyfileobj(r.raw, out_file)

            # save the attachment image with bg
            bg = PIL.Image.open("./background.jpeg")
            ss = PIL.Image.open("./ss{}.jpeg".format(num))
            dim = ss.height * ss.width
            ss_resize = ss.resize((int(ss.width / 2), int(ss.height / 2)))
            if dim < 1000000:
                PIL.Image.Image.paste(bg, ss, (250, 0))
            else:
                PIL.Image.Image.paste(bg, ss_resize, (250, 0))
            bg.save("pasted{}.jpeg".format(num))

        # make and save the image
        image_maker(text)

        # upload the image on instagram
        place_list = []
        for channel in message.channel_mentions:
            if str(channel) == "new-delhi-ncr":
                hash = "#Delhi"
                place_list.append(hash)
            else:
                hash = "#"+str(channel)
                place_list.append(hash)

        caption = "Resource availability and contact point verified only. Please do your due diligence before making any"\
                "purchase. DO NOT MAKE ANY ADVANCE PAYMENT - IN CASE SOMEONE ASKS, REPORT THEM AND WRITE IN THE COMMENT"\
                " SECTION #covid19India #covidhelp #covidresources #oxygencylinder"\
                "#beds #icu #amplify #covid {}".format(" ".join(place_list))

        photo_list = [Path("./myImage.jpeg")]
        for num, attach in enumerate(message.attachments):
            photo_list.append(Path("./pasted{}.jpeg".format(num)))
        bot.album_upload(photo_list, caption)

        print("Instagram upload complete at {}".format(datetime.datetime.now().strftime("%H:%M")))


client.run(TOKEN[0])
