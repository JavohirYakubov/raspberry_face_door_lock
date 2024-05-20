# raspberry_face_id
# Eshikni Yuzni Tanib Olish Orqali Ochish Qurilmasi

Bu loyiha Raspberry PI 4 va web kamera yordamida yuzni tanib olish orqali elektr eshik qulfini avtomatik ochish uchun ishlab chiqilgan. Ushbu loyiha Javohir Yakubov tomonidan Magisterlik dissertatsiyasi uchun ishlab chiqilgan.

## Loyihaning Maqsadi
Binolarda kirish-chiqish nazorati uchun shaxsni tanib olish dasturiy vositasini yaratish. Ushbu tizim yuzni aniqlash va tanib olish algoritmlaridan foydalanib, eshikni ochadi.

## Texnologiyalar va Kutubxonalar
- Raspberry Pi 4
- Python
- OpenCV (Haar Cascade Classifier va LBPH Face Recognizer algoritmlari)
- RPi.GPIO
- Web kamera

## Loyihaning Ishlash Tizimi
1. **Yuzni ro'yxatga olish:** Yuz tasvirlari to'plamini yaratish.
2. **Modelni o'qitish:** Yuzni tanib olish modeli yaratish uchun LBPH algoritmini ishlatish.
3. **Yuzni tanib olish:** Web kamera orqali tasvirlarni olish va yuzni aniqlash.
4. **Eshikni ochish:** Tanib olingan yuzni tekshirib, eshik qulfini ochish.

## O'rnatish va Ishga Tushirish
1. Raspberry Pi 4 ni sozlash.
2. Python kutubxonalarini o'rnatish:
    ```bash
    pip install opencv-python
    pip install RPi.GPIO
    ```
3. Skriptlarni yuklash va ishga tushirish:
    ```bash
    python enroll.py
    python train.py
    python recognize_pi.py
    ```

## Loyihaning Tuzilishi
- `enroll.py`: Yuzni ro'yxatga olish skripti.
- `train.py`: Yuzni tanib olish modelini o'qitish skripti.
- `recognize_pi.py`: Yuzni tanib olish va eshikni ochish skripti.
- `test_accuracy.py`: Modelning aniqligini tekshirish skripti.

## Muallif
Javohir Yakubov
javohir.fergana@gmail.com
