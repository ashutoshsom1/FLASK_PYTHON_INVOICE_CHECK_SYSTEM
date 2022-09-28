from flask import flash
import easyocr





"""## 1. Read in images or video"""


def pathconfig(file):
    image = 'static/uploads', file
    return image


def read(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    if len(result) == 0:
        flash('Given file is not invoice')
    else:
        return result


def check(result):
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == ('GSTIN', 'GST', 'GST/UIN'):
                if len(result[i+1][j]) == 15:
                    if type(result[i+1][j] == 'str'):
                      print('GST : ', result[i + 1][j])
                    else:
                      print("GST present is not feasible")
                else:
                  print("INVOICE does not have clear GST no.")
            else:
              print("INVOICE does not have GST")


"""## 2. Draw Results """
"""def show(IMAGE_PATH):
  img = cv2.imread(IMAGE_PATH)
  plt.imshow(img)
  plt.show()"""
