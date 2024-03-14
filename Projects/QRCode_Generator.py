import qrcode
from PIL import Image

# img=qrcode.make("https://skill-lync.com/")
# img.save("skill_lync.png")

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=30,border=10,)
qr.add_data("https://vaibhavgopnar.github.io/My-Portfolio/")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("gitlink.png")