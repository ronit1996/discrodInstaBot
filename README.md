# discrodInstaBot
Hi, if you are running to code or if you are intending to run the code the first thing I should tell you is that instagram doesn't like bots, so do it at your own risk.
However, this bot doesn't do much, it just posts the resources on instagram and doesn't interact with any user, also it doesn't log in or log out every time it posts
which according to me is a big advantage.

Now, about the code. The code uses 3 main libraries. The first one is discord library of course that runs the bot and grabs the messages, the second one is instagrapi
(the library is not continued anymore) which uploads the images on instagram after logging in and the third one is Pillow. It's an image processing library for
python, with Pillow I am making the images, so make sure you install these three libraries.

The code has a few stages, it all starts with the bot going online first, it's done using the discord library once that is done it will print bot is ready,
then it logs into instagram using instagrapi library and once that is done the bot stays online and waits for messages, you need to mention the channel name in the first if
statement so that the bot takes messages from that channel only and not from every channel.
Also for logging in the bot uses a file called Token.txt, this file is saved in my main drive and isn't uploaded as it contains the instagram id
the instagram passowrd and also the bot token with which it will log into discord. Once the logging in part is done the bot starts working.

Once a user messages in the specified channel, the bot checks if the message has text or only images, the message must have both else the bot won't upload it. if the message
has texts and images the bot first takes the text using the message.content() method and then checks for the tagged user or the channel mentioned in the message. If
there is a tagged user or a channel mentioned the bot removes them in the following if statements and also uses textwrap to make the text stay between a certain bound
else the lines of the message might be cropped.

Once the message part is done the bot now checks for attachments, we first take the link of the attachments by using the attachments.url method, then with the
requests library we take whatever attachment there is in that link and download it and save it in our harddrive, once that part is done we have got our attachment(in
this specific case, screenshot).

But we need to upload the screnshot too, for that I have create a simple white background alrady, what I do is if the screenshot is full HD i make it half hd
so that it fits insta's resolution and paste on top of the background, all this is done using the Pillow library in python, but if the screenshot is not full HD(lots
of users are just copy pasting screenshots or cropping them) I post it without scaling then save the image.

Next part is the text based image, for that I first create a colored backkground, we follow a certain color code and based on some keywords the background color is
creaed then I just write the text on top of that and again all of this is done using Pillow library.

Finally I use the instagrapi library again to make an album of images and upload it on instagram.
