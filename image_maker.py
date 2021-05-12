import string
import PIL.ImageDraw
import PIL.Image
import PIL.ImageFont


# colored background
class Image:
    most_imp = ["icu", "bed", "beds", "ambulance", "home-icu"]
    imp = ["blood", "plasma", "donor", "donate"]
    less_imp = ["cylinder", "cylinders", "can", "cans", "concentrator"]

    def image_creator(self, text):
        """This function takes text as data and creates an image out of it"""

        table = str.maketrans("", "", string.punctuation)
        color = (255, 255, 255)
        word_list = text.split()
        for x, y in enumerate(word_list):
            word_list[x] = y.lower().translate(table)

        if any(x in self.most_imp for x in word_list):
            color = (255, 69, 67)
        elif any(x in self.imp for x in word_list):
            color = (109, 189, 0)
        elif any(x in self.less_imp for x in word_list):
            color = (73, 146, 211)
        else:
            color = (215, 164, 0)

        # create the image
        img = PIL.Image.new('RGB', (1080, 1350), color)
        d = PIL.ImageDraw.Draw(img)
        myfont = PIL.ImageFont.truetype("Lato-Bold.ttf", 50)
        d.text((30, 30), text, fill=(0, 0, 0), font=myfont)
        text_size = myfont.getsize(text)
        print(text_size)
        d.text((30, (text_size[1]*len(text.splitlines()))+40), "hashtag", fill=(0, 0, 0), font=myfont)

        img_name = "myImage_RnD"

        # save the image
        img.save("./{}".format(img_name) + '.jpeg')

img = Image()
img.image_creator("This text is \n\n broken into two lines")


