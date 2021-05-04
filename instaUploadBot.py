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

# get credentials
with open("./token.txt") as f:
    TOKEN = f.readlines()

# uploading on insta
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
    garb = ["ss", "Ss", "sS", "SS"]
    garb2 = ["verified", "Verified"]
    if str(message.channel) == "test" and len(message.content.split()) > 0:
        msgs = message.content.splitlines()
        for i, j in enumerate(msgs):
            if any(x in garb for x in j.split()):
                del msgs[i]

        finalMsg = []
        for msg in msgs:
            words = msg.split()
            if any(x in garb2 for x in words):

                z = [a for a in words if not "@" in a]
                finalMsg.append(" ".join(z))
            else:
                y = [a for a in words if not "<" in a]
                finalMsg.append(" ".join(y))

        text = "\n".join(finalMsg)

        # get the attachment image
        url = message.attachments[0].url
        r = requests.get(url, stream=True)
        screenshot_name = "ss.jpeg"
        with open(screenshot_name, "wb") as out_file:
            shutil.copyfileobj(r.raw, out_file)

        # save the attachment image with bg
        bg = PIL.Image.open("./background.jpeg")
        ss = PIL.Image.open("./ss.jpeg")
        dim = ss.height * ss.width
        ss_resize = ss.resize((int(ss.width / 2), int(ss.height / 2)))
        if dim < 1000000:
            PIL.Image.Image.paste(bg, ss, (250, 0))
        else:
            PIL.Image.Image.paste(bg, ss_resize, (250, 0))
        bg.save("pasted.jpeg")

        # colored background
        color = (255, 255, 255)
        word_list = message.content.split()
        for x, y in enumerate(word_list):
            word_list[x] = y.lower()

        if any(x in ["cylinder", "cylinders", "can", "cans"] for x in word_list):
            color = (73, 146, 211)
        elif "concentrator" in word_list:
            color = (73, 146, 211)
        elif any(x in ["icu", "bed", "beds", "ambulance", "home-icu", "home"] for x in word_list):
            color = (255, 69, 67)
        else:
            color = (215, 164, 0)

        # create the image
        img = PIL.Image.new('RGB', (1000, 667), color)
        d = PIL.ImageDraw.Draw(img)
        myfont = PIL.ImageFont.truetype("Lato-Bold.ttf", 28)
        d.text((30, 30), text, fill=(0, 0, 0), font=myfont)

        img_name = "myImage"

        # save the image
        img.save("./{}".format(img_name) + '.jpeg')

        # upload the image on instagram
        place_list = []
        for channel in message.channel_mentions:
            hash = "#"+str(channel)
            place_list.append(hash)

        caption = "Resource availability and contact point verified only. Please do you due diligence before making any"\
                "purchase. DO NOT MAKE ANY ADVANCE PAYMENT - IN CASE SOMEONE ASKS, REPORT THEM AND WRITE IN THE COMMENT"\
                "SECTION #covid19India #covidhelp #covidresources #oxygencylinder"\
                "#beds #icu #amiplify #covid #{}".format(" ".join(place_list))

        photo_list = [Path("./myImage.jpeg"), Path("./pasted.jpeg")]
        bot.album_upload(photo_list, caption)

        print("Instagram upload complete")


client.run(TOKEN[0])
