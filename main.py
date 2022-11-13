import cv2
import numpy as np

def hollow(imgFileName):
    img = cv2.imread(imgFileName)
    rgbaImg = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    rgbaImg[..., 3] = np.where(np.all(img == 255, axis=-1), 0, 255)
    
    imgName = imgFileName.split(".")[0]
    cv2.imwrite("result/result_" + imgName + ".png", rgbaImg)
    print("hollowed: " + imgFileName)
    
def __main__():
    imgFileName = input("ファイル名を入力してください（拡張子を含めること）")
    hollow(imgFileName)
    
__main__()