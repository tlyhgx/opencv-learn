#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenCV 特征检测和匹配演示
展示关键点检测、特征描述和特征匹配
"""

import cv2
import numpy as np

def main():
    print("🔍 OpenCV 特征检测和匹配演示")
    print("=" * 35)
    
    # 读取图像
    img = cv2.imread('sample_image.jpg')
    if img is None:
        print("❌ 无法读取图像，请确保 sample_image.jpg 存在")
        return
    
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Harris角点检测
    print("1. Harris角点检测...")
    
    # 创建Harris角点检测所需的图像副本
    harris_img = img.copy()
    gray_float = np.float32(gray)
    
    # 应用Harris角点检测
    dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    
    # 标记角点
    harris_img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv2.imshow('Harris角点检测', harris_img)
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 2. SIFT特征检测 (如果可用)
    print("2. SIFT特征检测...")
    
    try:
        # 创建SIFT检测器
        sift = cv2.SIFT_create()
        
        # 检测关键点和计算描述符
        keypoints, descriptors = sift.detectAndCompute(gray, None)
        
        # 绘制关键点
        sift_img = cv2.drawKeypoints(img, keypoints, None, 
                                    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('SIFT特征检测', sift_img)
        print(f"   检测到 {len(keypoints)} 个关键点")
        print("   按任意键继续...")
        cv2.waitKey(0)
        
    except AttributeError:
        print("   SIFT不可用（可能是由于专利限制）")
        # 使用ORB作为替代
        print("   使用ORB特征检测作为替代...")
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        orb_img = cv2.drawKeypoints(img, keypoints, None, 
                                   flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('ORB特征检测', orb_img)
        print(f"   检测到 {len(keypoints)} 个关键点")
        print("   按任意键继续...")
        cv2.waitKey(0)
    
    # 3. 图像匹配示例
    print("3. 图像特征匹配...")
    
    # 创建一个变换后的图像作为"模板"
    rows, cols = gray.shape
    M = np.float32([[1, 0, 50], [0, 1, 30]])  # 平移变换
    template = cv2.warpAffine(gray, M, (cols, rows))
    
    try:
        # 使用ORB进行特征匹配
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(gray, None)
        kp2, des2 = orb.detectAndCompute(template, None)
        
        if des1 is not None and des2 is not None:
            # 创建BFMatcher对象
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            
            # 匹配描述符
            matches = bf.match(des1, des2)
            
            # 按距离排序
            matches = sorted(matches, key=lambda x: x.distance)
            
            # 绘制前10个匹配
            match_img = cv2.drawMatches(img, kp1, 
                                       cv2.cvtColor(template, cv2.COLOR_GRAY2BGR), kp2, 
                                       matches[:10], None, 
                                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            
            cv2.imshow('特征匹配', match_img)
            print(f"   找到 {len(matches)} 个匹配点，显示前10个")
            print("   按任意键继续...")
            cv2.waitKey(0)
        else:
            print("   未检测到足够的特征点进行匹配")
            
    except Exception as e:
        print(f"   特征匹配出现错误: {e}")
    
    # 4. 模板匹配
    print("4. 模板匹配...")
    
    # 截取图像的一部分作为模板
    template_roi = gray[100:200, 150:250]  # 从原图中截取一个区域作为模板
    
    # 应用模板匹配
    res = cv2.matchTemplate(gray, template_roi, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 绘制匹配结果
    template_match_img = img.copy()
    top_left = max_loc
    h, w = template_roi.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(template_match_img, top_left, bottom_right, (0, 255, 0), 2)
    
    # 显示模板和匹配结果
    cv2.imshow('模板', template_roi)
    cv2.imshow('模板匹配结果', template_match_img)
    print(f"   最佳匹配相关性: {max_val:.2f}")
    print("   按任意键继续...")
    cv2.waitKey(0)
    
    # 清理资源
    cv2.destroyAllWindows()
    print("✅ 特征检测和匹配演示完成!")

if __name__ == "__main__":
    main()