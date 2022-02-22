import pytesseract
#import cv2
from PIL import Image

# img = Image.open("nov2.jpeg")
# text = pytesseract.image_to_string(img, lang="ukr")

# with open("test.txt", "w", encoding='utf-8') as test_file:
#     test_file.write(text)

def dekanat_file(filename, img_list):
    text = ""
    for img in img_list:
        buff = Image.open(img)
        text += pytesseract.image_to_string(buff, lang="ukr")
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
    

if __name__=="__main__":
    nov = ["nov1.jpeg", "nov2.jpeg", "nov3.jpeg", "nov4.jpeg", "nov5.jpeg", "nov6.jpeg"]
    oz = ["oz1.jpeg", "oz2.jpeg", "oz3.jpeg", "oz4.jpeg", "oz5.jpeg", "oz6.jpeg"]
    roz = ["roz1.jpeg", "roz2.jpeg", "roz3.jpeg", "roz4.jpeg"]

    dekanat_file("Novosilsky.txt", nov)
    dekanat_file("Oziriansky.txt", oz)
    dekanat_file("Roznitivsky.txt", roz)
