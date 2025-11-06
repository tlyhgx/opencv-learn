#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenCV 高级操作演示
展示滤波器、形态学操作、轮廓检测等功能
"""

import cv2
import numpy as np

def main():
    print("🔍 OpenCV 高级操作演示")
    print("=" * 30)
    
    # 读取图像
    img = cv2.imread('sample_image.jpg')
    if img is None:
        print("❌ 无法读取图像，请确保 sample_image.jpg 存在")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. 应用不同的滤波器
    print("1. 应用滤波器...")
    
    # 均值滤波
    blur = cv2.blur(img, (5, 5))
    cv2.imshow('均值滤波', blur)
    cv2.waitKey(0)
    
    # 高斯滤波
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow('高斯滤波', gaussian)
    cv2.waitKey(0)
    
    # 中值滤波
    median = cv2.medianBlur(img, 5)
    cv2.imshow('中值滤波', median)
    cv2.waitKey(0)
    
    # 2. 形态学操作
    print("2. 形态学操作...")
    
    # 创建核
    kernel = np.ones((5, 5), np.uint8)
    
    # 腐蚀
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('腐蚀', erosion)
    cv2.waitKey(0)
    
    # 膨胀
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('膨胀', dilation)
    cv2.waitKey(0)
    
    # 开运算
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('开运算', opening)
    cv2.waitKey(0)
    
    # 闭运算
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('闭运算', closing)
    cv2.waitKey(0)
    
    # 3. 轮廓检测
    print("3. 轮廓检测...")
    
    # 应用阈值处理
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # 绘制轮廓
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)
    cv2.imshow('轮廓检测', contour_img)
    cv2.waitKey(0)
    
    # 4. 直方图计算和显示
    print("4. 直方图计算...")
    
    # 计算并显示灰度图直方图
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    print(f"   直方图大小: {hist.shape}")
    
    # 创建直方图可视化
    hist_img = np.zeros((300, 256, 3), dtype=np.uint8)
    for i in range(1, 256):
        # 修复NumPy警告：提取标量值
        prev_val = int(hist[i-1][0] / hist.max() * 300)
        curr_val = int(hist[i][0] / hist.max() * 300)
        cv2.line(hist_img, (i-1, 300-prev_val), 
                 (i, 300-curr_val), (255, 255, 255), 2)
    
    cv2.imshow('灰度直方图', hist_img)
    cv2.waitKey(0)
    
    # 清理资源
    cv2.destroyAllWindows()
    print("✅ 高级操作演示完成!")

if __name__ == "__main__":
    main()