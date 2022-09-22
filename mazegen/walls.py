from PIL import Image, ImageDraw
import random


black = 0
white = 255
gridWidth = 20
gridHeight = 20
cellSize = 10

# Lag nytt bilde i gråtonemodus, hent "draw"-objekt for å kunne tegne på det
image = Image.new("L", ((2 * gridWidth + 1) * cellSize, (2 * gridHeight + 1) * cellSize), black)
draw = ImageDraw.Draw(image)

def getAdjacentCells(cell: tuple[int, int]) -> list[tuple[int,int]]:
    """
    Gir en liste av alle cellene som rører inputcellen
    """
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    return [(cell[0]+direction[0], cell[1]+direction[1]) for direction in directions if cell[0] + direction[0] in range(gridWidth) and cell[1] + direction[1] in range(gridHeight)]

def removeWall(firstCell: tuple[int,int],secondCell: tuple[int,int]) -> None:
    """
    Fjerner en vegg mellom to celler (firstCell og secondCell).
    Gir en ValueError hvis cellene ikke er ved siden av hverandre.
    """
    # Sjekker om avstanden mellom cellene er 1
    if((firstCell[0]-secondCell[0])**2+(firstCell[1]-secondCell[1])**2 != 1):
        raise ValueError("firstCell and secondCell must be adjacent")

    #Tegner en hvis boks mellom cellene
    x = (firstCell[0] + secondCell[0])/2
    y = (firstCell[1] + secondCell[1])/2
    draw.rectangle(((1+2*x)*cellSize, (1+2*y)*cellSize, (2+2*x)*cellSize, (2+2*y)*cellSize),fill=white, outline=None)

# Tegn alle cellene
for x in range(gridWidth):
    for y in range(gridHeight):
        draw.rectangle(((1+2*x)*cellSize, (1+2*y)*cellSize, (2+2*x)*cellSize, (2+2*y)*cellSize),fill=white, outline=None)

# Sånn kan du lage en vei mellom cellene
removeWall((0,0),(0,1))
removeWall((0,1),(1,1))
removeWall((1,1),(2,1))


# Sånn kan du hente ut nabocellene til en celle
print(getAdjacentCells((1,1)))

# Vis bilde
image.show()