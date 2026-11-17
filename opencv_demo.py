import cv2

# 读取图片，把这里换成你的图片路径
img = cv2.imread("test.jpg")
if img is None:
    print("图片读取失败，请检查图片文件名！")
else:
    # 1.高斯模糊
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    # 2.翻转（水平翻转）
    flip_h = cv2.flip(img, 1)
    # 3.旋转
    h, w = img.shape[:2]
    rotate_mat = cv2.getRotationMatrix2D((w//2, h//2), 45, 1)
    rotate_img = cv2.warpAffine(img, rotate_mat, (w, h))
    # 4.缩放
    resize_img = cv2.resize(img, (w//2, h//2))

    # 展示
    cv2.imshow("original", img)
    cv2.imshow("gaussian blur", blur)
    cv2.imshow("flip horizontal", flip_h)
    cv2.imshow("rotate 45", rotate_img)
    cv2.imshow("resize", resize_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
