# RTSP Stream README

Ez a projekt egy RTSP streamet hoz létre egy webkamera segítségével, és továbbítja azt egy RTSP szerverre az FFmpeg használatával.

### Követelmények

- Python 3.x
- OpenCV (`cv2` modul)
- FFmpeg (telepítve és elérhető a PATH-ban)

### Telepítés

1. Telepítsd a szükséges Python csomagokat:
    ```sh
    pip install opencv-python
    ```

2. Telepítsd az FFmpeg-et és győződj meg róla, hogy elérhető a PATH-ban.

### Használat

1. Futtasd a [rtsp_stream.py](http://_vscodecontentref_/0) fájlt:
    ```sh
    python rtsp_stream.py
    ```

2. A script megnyitja a webkamerát, és elkezdi streamelni a videót az RTSP szerverre a megadott URL-en (`rtsp://127.0.0.1:8554/proba`).

### Konfiguráció

A következő konfigurációs változókat módosíthatod a [rtsp_stream.py](http://_vscodecontentref_/1) fájlban:

- [rtsp_server_url](http://_vscodecontentref_/2): Az RTSP szerver URL-je.
- [ffmpeg_path](http://_vscodecontentref_/3): Az FFmpeg futtatható fájl elérési útja.
- [frame_width](http://_vscodecontentref_/4): A videó szélessége.
- [frame_height](http://_vscodecontentref_/5): A videó magassága.
- [fps](http://_vscodecontentref_/6): A videó képkockasebessége.

### Hibakeresés

- Ha a webkamera nem nyílik meg, ellenőrizd, hogy megfelelően csatlakoztatva van-e, és hogy a megfelelő indexet használod-e ([cv2.VideoCapture(0)](http://_vscodecontentref_/7)).
- Ha az FFmpeg nem található, ellenőrizd, hogy telepítve van-e, és elérhető-e a PATH-ban.

### Leállítás

A streamelés leállításához nyomj meg egy `Ctrl+C` kombinációt a terminálban. A script automatikusan felszabadítja a webkamerát és leállítja az FFmpeg folyamatot.

### Licenc

Ez a projekt szabadon használható és módosítható.