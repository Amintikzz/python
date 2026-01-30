from openai import OpenAI
import base64
import cv2
from gtts import gTTS
import pyglet
import time
import os

# 🔑 Твой OpenAI ключ
client = OpenAI(api_key="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")# вставь свой ключ сюда

# Включаем камеру
cap = cv2.VideoCapture(0)
print("Нажми 's' чтобы сделать фото и отправить в ChatGPT, 'q' чтобы выйти.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка камеры.")
        break

    cv2.imshow("Камера (S - распознать, Q - выйти)", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        image_path = "capture.jpg"
        cv2.imwrite(image_path, frame)
        print("📸 Фото сохранено, отправляю в ChatGPT...")

        # Кодируем изображение в base64
        with open(image_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")

        # Отправляем изображение в модель gpt-4o
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # или gpt-4o, если у тебя есть доступ
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Ты умные очки для незрячих людей ты должен распозновать текст и отправлять мне его без изменений а если нету текста или того что можно прочитать ты должен описать то что видишь"},
                        {"type": "image_url", "image_url": {"url":f"data:image/jpeg;base64,{img_base64}"},}
                    ]
                }
            ]
        )

        recognized_text = response.choices[0].message.content.strip()
        print("\n📜 Распознанный текст ChatGPT:")
        print(recognized_text)

        if recognized_text:
            print("\n🔊 Озвучиваю текст...")
            tts = gTTS(text=recognized_text, lang="ru")
            tts.save("voice.mp3")
            music = pyglet.media.load("voice.mp3", streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove("voice.mp3")
        else:
            print("⚠️ Текст не найден.")

    elif key == ord('q'):
        print("🚪 Выход из программы.")
        break

cap.release()
cv2.destroyAllWindows()
