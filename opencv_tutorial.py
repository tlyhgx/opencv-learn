#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenCV 交互式学习教程
从基础开始了解OpenCV的使用及原理
"""

import sys
import time

class OpenCVTutorial:
    def __init__(self):
        self.progress = 0
        self.sections = [
            self.intro_section,
            self.installation_section,
            self.basic_operations_section,
            self.image_processing_section,
            self.advanced_topics_section,
            self.practice_section
        ]
    
    def clear_screen(self):
        """清屏函数"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_title(self):
        """打印标题"""
        title = """
        ==================================================
            📚 OpenCV 交互式学习教程 - 从基础开始
        ==================================================
        """
        print(title)
    
    def pause(self):
        """暂停函数，等待用户输入"""
        input("\n按回车键继续...")
        self.clear_screen()
    
    def intro_section(self):
        """介绍部分"""
        self.print_title()
        print("📌 第 1 节：OpenCV 简介\n")
        print("OpenCV (Open Source Computer Vision Library) 是一个开源的计算机视觉和机器学习软件库。\n")
        print("📋 主要特点：")
        print("  ✅ 开源免费")
        print("  ✅ 跨平台（支持Windows、Linux、MacOS等）")
        print("  ✅ 包含2500多个优化算法")
        print("  ✅ 支持图像处理、视频分析、物体识别、机器学习等\n")
        print("🔍 OpenCV的应用领域：")
        print("  🔬 计算机视觉研究")
        print("  📱 移动应用开发")
        print("  🚗 自动驾驶")
        print("  🔒 人脸识别和安全系统")
        print("  🩺 医学图像处理")
        print("  🎮 增强现实\n")
        print("OpenCV由Intel于1999年开发，现在由Willow Garage和Itseez继续维护。")
        self.progress = 1
    
    def installation_section(self):
        """安装部分"""
        self.print_title()
        print(f"📌 第 {self.progress+1} 节：安装 OpenCV\n")
        print("💻 使用pip安装OpenCV（推荐）：")
        print("  在命令行中输入以下命令：")
        print("  pip install opencv-python")
        print("  或者安装完整版（包含额外功能）：")
        print("  pip install opencv-contrib-python\n")
        
        print("🔧 验证安装是否成功：")
        print("  在Python中运行以下代码：")
        print("  >>> import cv2")
        print("  >>> print(cv2.__version__)\n")
        
        print("⚠️ 常见安装问题及解决方案：")
        print("  1. 权限问题：使用管理员权限或添加 --user 参数")
        print("  2. 版本兼容性：指定版本安装，如 pip install opencv-python==4.5.5.64")
        print("  3. 依赖冲突：考虑创建虚拟环境\n")
        
        print("💡 提示：本教程假设您已经安装了Python和pip。")
        self.progress = 2
    
    def basic_operations_section(self):
        """基础操作部分"""
        self.print_title()
        print(f"📌 第 {self.progress+1} 节：OpenCV 基础操作\n")
        
        print("📷 图像的读取、显示和保存\n")
        
        print("1. 读取图像：")
        print("  import cv2")
        print("  img = cv2.imread('image.jpg')  # 读取图像")
        print("  # 参数说明：")
        print("  # - cv2.IMREAD_COLOR：读取彩色图像（默认）")
        print("  # - cv2.IMREAD_GRAYSCALE：读取灰度图像")
        print("  # - cv2.IMREAD_UNCHANGED：读取包含alpha通道的图像\n")
        
        print("2. 显示图像：")
        print("  cv2.imshow('Image Window', img)  # 显示图像")
        print("  cv2.waitKey(0)  # 等待按键")
        print("  cv2.destroyAllWindows()  # 关闭所有窗口\n")
        
        print("3. 保存图像：")
        print("  cv2.imwrite('output.jpg', img)  # 保存图像\n")
        
        print("📏 图像的基本属性：")
        print("  print(img.shape)  # 图像的形状（高度, 宽度, 通道数）")
        print("  print(img.size)   # 图像的像素总数")
        print("  print(img.dtype)  # 图像的数据类型\n")
        
        print("💡 注意：OpenCV读取的图像默认是BGR格式，而不是常见的RGB格式。")
        self.progress = 3
    
    def image_processing_section(self):
        """图像处理部分"""
        self.print_title()
        print(f"📌 第 {self.progress+1} 节：基本图像处理\n")
        
        print("🎨 颜色空间转换：")
        print("  # BGR 转 RGB")
        print("  rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)")
        print("  ")
        print("  # BGR 转 灰度图")
        print("  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n")
        
        print("✂️ 图像裁剪：")
        print("  # 裁剪图像 [y:y+h, x:x+w]")
        print("  cropped_img = img[100:300, 200:400]\n")
        
        print("📐 图像缩放：")
        print("  # 方法1：指定宽度和高度")
        print("  resized_img = cv2.resize(img, (width, height))")
        print("  ")
        print("  # 方法2：按比例缩放")
        print("  resized_img = cv2.resize(img, None, fx=0.5, fy=0.5)\n")
        
        print("🔄 图像旋转：")
        print("  # 获取图像尺寸")
        print("  h, w = img.shape[:2]")
        print("  # 计算旋转矩阵")
        print("  M = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)  # 中心点，角度，缩放因子")
        print("  # 执行旋转")
        print("  rotated_img = cv2.warpAffine(img, M, (w, h))\n")
        
        print("🔳 图像阈值处理：")
        print("  # 全局阈值")
        print("  ret, thresh1 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)")
        print("  # 自适应阈值")
        print("  thresh2 = cv2.adaptiveThreshold(gray_img, 255, ")
        print("                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, ")
        print("                                 cv2.THRESH_BINARY, 11, 2)")
        self.progress = 4
    
    def advanced_topics_section(self):
        """高级主题部分"""
        self.print_title()
        print(f"📌 第 {self.progress+1} 节：OpenCV 高级主题\n")
        
        print("🔍 边缘检测：")
        print("  # Canny边缘检测")
        print("  edges = cv2.Canny(gray_img, 100, 200)\n")
        
        print("🔤 轮廓检测：")
        print("  # 寻找轮廓")
        print("  contours, hierarchy = cv2.findContours(thresh1, ")
        print("                                        cv2.RETR_EXTERNAL, ")
        print("                                        cv2.CHAIN_APPROX_SIMPLE)")
        print("  # 绘制轮廓")
        print("  cv2.drawContours(img, contours, -1, (0, 255, 0), 3)\n")
        
        print("🔢 直方图计算：")
        print("  # 计算灰度图直方图")
        print("  hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])")
        print("  # 计算彩色图直方图")
        print("  color = ('b', 'g', 'r')")
        print("  for i, col in enumerate(color):")
        print("      hist = cv2.calcHist([img], [i], None, [256], [0, 256])\n")
        
        print("🎥 视频处理：")
        print("  # 打开摄像头")
        print("  cap = cv2.VideoCapture(0)")
        print("  while True:")
        print("      ret, frame = cap.read()  # 读取一帧")
        print("      cv2.imshow('Video', frame)  # 显示帧")
        print("      if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出")
        print("          break")
        print("  cap.release()  # 释放摄像头")
        print("  cv2.destroyAllWindows()  # 关闭所有窗口")
        self.progress = 5
    
    def practice_section(self):
        """练习部分"""
        self.print_title()
        print(f"📌 第 {self.progress+1} 节：实践练习\n")
        
        print("🎯 练习 1：图像读取与显示")
        print("  任务：编写代码读取一张图像，显示它，并在窗口标题中显示图像的尺寸。")
        print("  提示：使用cv2.imread(), cv2.imshow(), cv2.waitKey()和cv2.destroyAllWindows()")
        print()
        
        print("🎯 练习 2：图像转换")
        print("  任务：读取一张彩色图像，将其转换为灰度图，然后显示两种版本。")
        print("  提示：使用cv2.cvtColor()和cv2.COLOR_BGR2GRAY")
        print()
        
        print("🎯 练习 3：简单图像处理")
        print("  任务：读取一张图像，将其缩放到原尺寸的一半，然后旋转45度，最后保存结果。")
        print("  提示：使用cv2.resize(), cv2.getRotationMatrix2D(), cv2.warpAffine()和cv2.imwrite()")
        print()
        
        print("🎯 练习 4：边缘检测")
        print("  任务：读取一张图像，转换为灰度图，然后应用Canny边缘检测算法。")
        print("  提示：使用cv2.Canny()")
        
        print("\n🎉 恭喜！您已经完成了OpenCV基础学习教程的所有章节！")
        print("🚀 接下来，您可以尝试解决上面的练习，或者继续学习更高级的OpenCV功能。")
        self.progress = 6
    
    def start(self):
        """开始教程"""
        self.clear_screen()
        print("欢迎使用 OpenCV 交互式学习教程！\n")
        print("这个教程将帮助您从基础开始学习OpenCV的使用及原理。\n")
        print("教程包含以下章节：")
        for i, section in enumerate(self.sections, 1):
            print(f"  {i}. {section.__name__.replace('_', ' ').title()}")
        print()
        print("让我们开始吧！\n")
        self.pause()
        
        for section in self.sections:
            section()
            if section != self.sections[-1]:  # 如果不是最后一节
                self.pause()
        
        print("\n📚 教程结束。希望您对OpenCV有了初步的了解！")
        print("💡 提示：您可以随时再次运行本教程来复习这些内容。")
        print("🔍 想要深入学习？尝试完成最后的练习题或查阅OpenCV官方文档。")

if __name__ == "__main__":
    tutorial = OpenCVTutorial()
    tutorial.start()