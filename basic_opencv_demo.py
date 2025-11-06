#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenCV 基础操作演示
展示图像读取、显示、基本处理等操作
"""

import cv2
import numpy as np

def main():
    print("🔍 OpenCV 基础操作演示")
    print("=" * 30)
    
    # 1. 读取图像
    print("1. 读取图像...")
    img = cv2.imread('sample_image.jpg')
    
    if img is None:
        print("❌ 无法读取图像，请确保 sample_image.jpg 存在")
        return
    
    print(f"   图像尺寸: {img.shape[1]}x{img.shape[0]} 像素")
    print(f"   通道数: {img.shape[2] if len(img.shape) > 2 else 1}")
    
    # 2. 显示原始图像
    print("2. 显示原始图像...")
    cv2.imshow('原始图像', img)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 3. 转换为灰度图
    print("3. 转换为灰度图...")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('灰度图', gray_img)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 4. 边缘检测
    print("4. 应用边缘检测...")
    edges = cv2.Canny(gray_img, 100, 200)
    cv2.imshow('边缘检测', edges)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 5. 图像缩放
    print("5. 图像缩放...")
    resized_img = cv2.resize(img, None, fx=0.5, fy=0.5)
    print(f"   缩放后尺寸: {resized_img.shape[1]}x{resized_img.shape[0]} 像素")
    cv2.imshow('缩放图像', resized_img)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 6. 绘制形状
    print("6. 在图像上绘制形状...")
    # 在图像上绘制一个矩形
    drawn_img = img.copy()
    cv2.rectangle(drawn_img, (50, 50), (200, 200), (0, 255, 255), 3)
    # 在图像上绘制一个圆
    cv2.circle(drawn_img, (300, 100), 50, (255, 0, 255), 3)
    # 在图像上添加文本
    cv2.putText(drawn_img, 'OpenCV Demo', (100, 400), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('绘制形状', drawn_img)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 7. 保存处理后的图像
    print("7. 保存处理后的图像...")
    cv2.imwrite('processed_image.jpg', drawn_img)
    print("   图像已保存为 processed_image.jpg")
    
    # 清理资源
    cv2.destroyAllWindows()
    print("✅ 演示完成!")

if __name__ == "__main__":
    main()