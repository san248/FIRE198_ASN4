import cv2

# Step 2

# Question 1

# reading in a template image
# then converting the template into grayscale
image =  cv2.imread("C:\\Users\\nazee\\Desktop\\templateNew2.PNG")
template = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Questions 2, 3, 4
 
w, h = template.shape[::-1]

cap = cv2.VideoCapture("C:\\Users\\nazee\\Desktop\\Vid.mp4")

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (max_loc[0] + w, max_loc[1] + h)

    cv2.rectangle(frame, max_loc, bottom_right, 255, 2)
    cv2.imshow('gray', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows


