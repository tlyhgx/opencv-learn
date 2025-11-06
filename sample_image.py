#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建示例图像，用于OpenCV学习
"""

import numpy as np
import cv2

# 创建一个500x500的彩色图像（BGR格式）
img = np.ones((500, 500, 3), dtype=np.uint8) * 240  # 白色背景

# 绘制一些基本形状
# 绘制一个蓝色矩形
cv2.rectangle(img, (100, 100), (400, 300), (255, 0, 0), -1)

# 绘制一个红色圆形
cv2.circle(img, (250, 200), 50, (0, 0, 255), -1)

# 绘制一个绿色三角形
pts = np.array([[150, 350], [250, 250], [350, 350]], np.int32)
cv2.fillPoly(img, [pts], (0, 255, 0))

# 添加文本
cv2.putText(img, 'OpenCV Sample', (150, 450), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# 保存图像
cv2.imwrite('sample_image.jpg', img)

print("✅ 示例图像已创建：sample_image.jpg")
print("📏 图像尺寸：500x500 像素")
print("🎨 图像内容：包含蓝色矩形、红色圆形、绿色三角形和文本")
print("💡 您可以在OpenCV学习过程中使用此图像进行实践操作。")