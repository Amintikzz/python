import pytesseract
from PIL import Image
from gtts import gTTS
import pyglet
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
cap = cv2.VideoCapture(0)

print("Нажмите 's' чтобы сделать снимок и распознать текст")
print("Нажмите 'q' чтобы выйти")

while True:
    ret, frame = cap.read()
    if not ret:
        break

   
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("s"):  
        cv2.imwrite("frame.jpg", frame)

        image = Image.open("frame.jpg")

        text = pytesseract.image_to_string(image, lang="kaz")

        print("\nРаспознанный текст:")
        print(text)
        tts = gTTS(text, lang ='ru')
        tts.save('Chtenye.mp3')
        music = pyglet.resource.media('Chtenye.mp3')
        music.play()

    elif key == ord("q"):  
        break

cap.release()
