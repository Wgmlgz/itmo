# WSL setup

```bash
pip install networkx
pip install pytesseract
pip install opencv-python
pip install numpy

sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata
sudo mv -v eng.traineddata  /usr/share/tesseract-ocr/4.00/tessdata/
```
