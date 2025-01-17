import cv2
import turtle
import time


def draw_image_with_turtle(image_path):
    # Görseli yükle
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100))  # Görseli 100x100 piksele küçült

    # Turtle ekranını ayarla
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Atatürk Portresi")
    screen.tracer(0)  # Animasyon devre dışı 

    # Çizim işlemleri burada yapılır
    screen.update()  # Çizim tamamlandıktan sonra ekranı güncelle
    # Turtle ayarları
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()

    # Görseli çiz
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            color = img[y, x]
            pen.goto(x * 5 - 250, 250 - y * 5)  # Koordinatları ayarla
            pen.dot(5, (color / 255, color / 255, color / 255))  # Nokta çiz
            time.sleep(0.00001)  # Her adım arasında 0.001 saniye bekle

    pen.hideturtle()
    screen.mainloop()