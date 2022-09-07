import cv2

# Question 5
image =  cv2.imread("C:\\Users\\nazee\\Desktop\\templateNew2.PNG")
template = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
w, h = template.shape[::-1]

cap = cv2.VideoCapture("C:\\Users\\nazee\\Desktop\\Vid.mp4")

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)

    cv2.rectangle(frame, min_loc, bottom_right, 255, 2)
    cv2.imshow('gray', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows