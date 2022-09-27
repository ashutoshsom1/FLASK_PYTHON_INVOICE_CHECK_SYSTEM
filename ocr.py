import easyocr
import cv2

"""## 1. Read in images or video"""
def pathconfig():
    IMAGE_PATH = 'static/uploads', file

def read():
        reader = easyocr.Reader(['en'])
        result = reader.readtext(IMAGE_PATH)
        type(result)

def check():
     for i in range(len(result)):
        for j in range(len(result[i])):
          if result[i][j] == 'GSTIN':
            print('GST : ', result[i + 1][j])

"""## 2. Draw Results """
def show():
  img = cv2.imread(IMAGE_PATH)
  plt.imshow(img)
  plt.show()


pathconfig()

