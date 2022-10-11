import fileinput

from flask import flash
import easyocr
import cv2

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads/'
IMAGE_PATH = UPLOAD_FOLDER + 'file'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#

"""def read(filename):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    if len(result) == 0:
        flash('Given file is not invoice')
    else:
        return result"""
"""#def remove_clutter(result):
    a1 = []
    for i in range(len(result)):
        x = result[i][1]
        a1.append(x)
        return a1"""
"""def check(a1):
    for i, word in zip(range(len(a1)), a1):
       if word in ["GSTIN", "GST/UIN", "GSTIN No"]:
        temp = a1[i + 1]
        return temp
"""

"""for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] in ['GSTIN']:
                if len(result[i + 1][j]) == 15:
                    if type(result[i + 1][j] == 'str'):
                        return result[i + 1][j]"""

"""## 2. Draw Results"""
"""def show(filename):
  img = cv2.imread(filename)
  plt.imshow()
  plt.show()"""


def show_result():
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH)
    a1 = []
    if len(result) == 0:
        flash('Given file is not invoice')
    else:
        for i in range(len(result)):
            x = result[i][1]
            a1.append(x)
        return a1


def check(a1):
    for i, word in zip(range(len(a1)), a1):
        if word in ["GSTIN", "GST/UIN", "GSTIN No"]:
            temp = a1[i + 1]
            return str(temp)


"""def check(a1):
    for i, word in zip(range(len(a1)), a1):
        if word in ["GSTIN", "GST/UIN", "GSTIN No"]:
            temp = a1[i + 1]
            return str(temp)"""
