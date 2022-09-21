from PIL import Image

black = 0
white = 255

#Grensen for hva vi setter til svart eller hvitt. Prøv å endre denne!
threshold = 255/2

with Image.open("goodDavid.png") as image:
    # Sett bilde til "L"ightness-mode, altså ignorer farger
    image = image.convert("L")

    # For hver piksel
    for x in range(image.width):
        for y in range(image.height):

            #Hvis lysverdien er under grensen og gjør den svart, ellers gjør den hvit
            if image.getpixel((x,y)) < threshold:
                image.putpixel((x,y), black)
            else:
                image.putpixel((x,y), white)
    #Vis bilde
    image.show()