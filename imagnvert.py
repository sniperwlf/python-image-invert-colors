

from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def openGraphicsWindow(title, width, height, image):
    # open grapics window
    win = GraphWin(title, width, height)
    win.setBackground(color_rgb(56, 54, 53))
    # center image in window
    image.move(width / 2, height / 2)
    image.draw(win)
    return win


def openFile():
    # open file
    infileName = askopenfilename()
    infile = open(infileName, "r")
    return infile


def openImage():
    # habrir PPM o archivo GIF
    infileName = askopenfilename()
    # centrar el origen basado en el tamaño de la imagen a usar
    image = Image(Point(0, 0), infileName)
    return image


def createButton(win):
    button = Rectangle(Point(1, 1), Point(250, 40))
    button.setOutline(color_rgb(244, 188, 15))
    button.setFill(color_rgb(119, 94, 57))
    button.draw(win)
    buttonText = Text(button.getCenter(), "Invertir Colores")
    buttonText.setTextColor(color_rgb(244, 188, 15))
    buttonText.draw(win)
    return button, buttonText


def invertColor(win, image, width, height):
    # cambia los pixeles a escala gris y muestra proceso
    for y in range(height):
        for x in range(width):
            r, g, b = image.getPixel(x, y)
            image.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))
        image.undraw()
        image.draw(win)


def saveFile(image):
    saveFileName = asksaveasfilename()
    if saveFileName != "":
        image.save(saveFileName)


def main():
    # habre y muestra la imagen
    image = openImage()
    # creacion de ventana
    width = image.getWidth()
    height = image.getHeight()
    win = openGraphicsWindow("Color Inversion", width, height, image)

    # boton para invertir
    button, buttonText = createButton(win)
    win.getMouse()
    invertColor(win, image, width, height)

    # instruccion para guardar nueva imagen
    saveFile(image)

    # boton para salir
    button.undraw()
    buttonText.undraw()
    buttonText.setText("Click para salir")
    button.draw(win)
    buttonText.draw(win)
    win.getMouse()


main()