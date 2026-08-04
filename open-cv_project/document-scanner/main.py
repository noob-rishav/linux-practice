"""
Project: Document Scanner using OpenCV

Features:
- Image preprocessing
- Edge detection
- Contour detection
- Largest quadrilateral detection
- Perspective transformation
- Document scanning

Author: Rishav Kumar Singh
"""



import cv2
import numpy as np
from pathlib import Path

# -------------------- Constants --------------------
WIDTH = 600
HEIGHT = 800

kernel = np.ones((5, 5), np.uint8)


# -------------------- Functions --------------------

def reorder(points):
    points = points.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), np.int32)

    add = points.sum(1)

    newPoints[0] = points[np.argmin(add)]      # Top Left
    newPoints[3] = points[np.argmax(add)]      # Bottom Right

    diff = np.diff(points, axis=1)

    newPoints[1] = points[np.argmin(diff)]     # Top Right
    newPoints[2] = points[np.argmax(diff)]     # Bottom Left

    return newPoints


def getContours(img):

    biggest = np.array([])
    maxArea = 0

    contours, hierarchy = cv2.findContours(
        img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 5000:

            peri = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(
                cnt,
                0.02 * peri,
                True
            )
            cv2.drawContours(imgContour, [approx], -1, (0, 255, 255), 3)

            print("Area :", area)
            print("Perimeter :", peri)
            print("Corners :", len(approx))
            print("--------------------------")

            if len(approx) == 4:

                if area > maxArea:

                    biggest = approx
                    maxArea = area

    if biggest.size != 0:

        biggest = reorder(biggest)

        cv2.drawContours(
            imgContour,
            [biggest],
            -1,
            (0, 255, 0),
            20
        )

    return biggest


# -------------------- Main --------------------

BASE_DIR = Path(__file__).parent
IMAGE_PATH = BASE_DIR / "images" / "input.jpeg"

img = cv2.imread(str(IMAGE_PATH))

resize_image = cv2.resize(img, (WIDTH, HEIGHT))
cv2.imwrite("results/test.png", resize_image)

imgContour = resize_image.copy()

# Preprocessing
imgGray = cv2.cvtColor(
    resize_image,
    cv2.COLOR_BGR2GRAY
)

imgBlur = cv2.GaussianBlur(
    imgGray,
    (7, 7),
    1
)

imgCanny = cv2.Canny(
    imgBlur,
    100,
    100
)

imgDil = cv2.dilate(
    imgCanny,
    kernel,
    iterations=2
)

imgErode = cv2.erode(
    imgDil,
    kernel,
    iterations=1
)

# Find biggest document
biggest = getContours(imgErode)

# Warp Perspective
if biggest.size != 0:

    pts1 = np.float32(biggest)

    pts2 = np.float32([
        [0, 0],
        [WIDTH, 0],
        [0, HEIGHT],
        [WIDTH, HEIGHT]
    ])

    matrix = cv2.getPerspectiveTransform(
        pts1,
        pts2
    )

    imgWarp = cv2.warpPerspective(
        resize_image,
        matrix,
        (WIDTH, HEIGHT)
    )

    # Crop little borders
    imgWarp = imgWarp[20:imgWarp.shape[0]-20,
                      20:imgWarp.shape[1]-20]

    imgWarp = cv2.resize(
        imgWarp,
        (WIDTH, HEIGHT)
    )
    cv2.imwrite("results/scanned_document.png", imgWarp)

    cv2.imshow("Warp", imgWarp)

# -------------------- Display --------------------

cv2.imshow("Original", img)
cv2.imshow("Resized", resize_image)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilated", imgDil)
cv2.imshow("Eroded", imgErode)
cv2.imshow("Contours", imgContour)

cv2.waitKey(0)
cv2.destroyAllWindows()