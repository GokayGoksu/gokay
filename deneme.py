import numpy as np
import cv2
import math

res_x, res_y = 1920, 1080
h = 50
fov_x = 60
fov_y = 36
en, boy = 0.5, 1.7

Length_x = 2 * math.tan(math.radians(fov_x / 2)) * h
Length_y = 2 * math.tan(math.radians(fov_y / 2)) * h

GSD_x = Length_x / res_x
GSD_y = Length_y / res_y

pixel_x = int(en / GSD_x)   
pixel_y = int(boy / GSD_y)  

print(pixel_x)
print(pixel_y)

img = np.zeros((res_y, res_x, 3), dtype=np.uint8)

center_x = res_x // 2
center_y = res_y // 2

top_left = (center_x - pixel_x // 2, center_y - pixel_y // 2)
bottom_right = (center_x + pixel_x // 2, center_y + pixel_y // 2)

cv2.rectangle(img, top_left, bottom_right, (255, 255, 255), -1)

cv2.imwrite("output2.png", img)
cv2.imshow("Insan", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
