import string
import PIL.ImageDraw
import PIL.Image
import PIL.ImageFont
import address

with open("./message.txt") as f:
    text = f.read() 

class Tag:
    def __init__(self, input_text):
        """This funtion returns the tags needed for colored background and tags"""
        hosp = ["bed", "beds","home-icu", "icu", "ventilator", "home"]
        blood = ["blood", "plasma", "donor", "donate"]
        o2 = ["cylinder", "cylinders", "can", "cans", "concentrator", "oxygencylinder"]
        misc = ["food", "delivery", "meal", "meals", "refill", "refilling"]
        meds = ["tocilizumab", "remdesivir", "liposomal", "bevacizumab", "medicine", "medicines", "injection", "fabiflu"]

        # remove the punctuation
        replace_table = str.maketrans("", "", string.punctuation)
        self.tag = []
        self.color = (255, 255, 255)
        self.icon = ""
        word_list = input_text.split()
        for count, word in enumerate(word_list):
            word_list[count] = word.lower().translate(replace_table)

        # get tags
        for word in word_list:
            if word in hosp:
                self.tag.append(word)
                self.color = (233,141,142)
                self.icon = "./icons/hospital.png"
            elif word in blood:
                self.tag.append(word)
                self.color = (140,199,169)
                self.icon = "./icons/plasma.png"
            elif word == "ambulance":
                self.tag.append(word)
                self.color = (240,173,182)
                self.icon = "./icons/ambulance.png"
            elif word in meds:
                self.tag.append(word)
                self.color = (199,173,200)
                self.icon = "./icons/medicine.png"
            elif word in o2:
                self.tag.append(word)
                self.color = (135,181,207)
                self.icon = "./icons/oxygen.png"
            elif word in misc:
                self.tag.append(word)
                self.color = (250,241,140)
                self.icon = "./icons/others.png"



# create the tag creator class
class TagCreate:
    def __init__(self, image, text, text_elements, font, extra=0):
        text_size = font.getsize(text)
        elem_x_pos = 60
        elem_y_pos = (text_size[1]*len(text.splitlines()))+extra+40 # 40 is a padding amount

        # create the rounded rectangle
        my_tag_font = PIL.ImageFont.truetype("Lato-Bold.ttf", 60)
        x0 = elem_x_pos-30
        y0 = elem_y_pos
        x1 = my_tag_font.getsize(text_elements)[0] + elem_x_pos + 30 # 30 is padding amount
        y1 = my_tag_font.getsize(text_elements)[1] + elem_y_pos + 20 # 20 is padding amuont
        image.rounded_rectangle([(x0, y0), (x1, y1)], fill="white", radius=30)

        self.thickness = y1 - elem_y_pos

        # write the tags
        image.text((elem_x_pos, elem_y_pos), text_elements, fill=(42, 43, 48), font=my_tag_font)


# create final image
def image_maker(text):
    myfont = PIL.ImageFont.truetype("Lato-Bold.ttf", 50)
    tag = Tag(text)

    # create the image
    img = PIL.Image.new('RGB', (1080, 1350), tag.color)
    d = PIL.ImageDraw.Draw(img)
    d.text((30, 30), text, fill=(42, 43, 48), font=myfont)

    # remove duplicate elements from list
    clean = [elem for num, elem in enumerate(tag.tag) if elem not in tag.tag[:num]]
    text_elements = " ".join(clean)

    # create the tags
    add = address.Address()
    place = add.find_place(text)
    #fix punctuations
    fixed_place = ""
    if place == "new delhi ncr":
        fixed_place = "Delhi"
    else:
        fixed_place = place

    key_word_tag = TagCreate(d, text, text_elements, myfont)
    location_tag = TagCreate(d, text, fixed_place, myfont, key_word_tag.thickness+30)

    # add the icons
    path = tag.icon
    icon = PIL.Image.open(path)
    resized_icon = icon.resize((int(icon.width/7), int(icon.height/7)))
    resized_icon.convert("RGBA")
    text_size = myfont.getsize(text)
    x_pos = 30
    y_pos = (text_size[1]*len(text.splitlines()))+40 + key_word_tag.thickness+30 + location_tag.thickness+30

    # create rounded rectangle for icon
    x0 = x_pos
    y0 = y_pos
    x1 = resized_icon.width + x0
    y1 = resized_icon.height + y0
    d.rounded_rectangle([(x0, y0), (x1, y1)], fill="white", radius=30)
    img.paste(resized_icon, (x_pos, y_pos), resized_icon)

    # save the image
    img_name = "myImage"
    img.save("./{}".format(img_name) + '.jpeg')


image_maker(text)