# PyQt6 GUI 开发示例

## 1. 项目概述

本项目是一个使用PyQt6库开发的GUI应用程序示例，包含多个窗口和界面。每个示例文件展示了如何使用PyQt6创建不同类型的窗口和界面组件。

## 2. 文件结构

项目的文件结构如下：

```text
PyQtTutorial/
├── README.md
├── requirements.txt
└── Part01/
    ├── WindowUI.py
    ├── LoadUI.py
    ├── mywindow.py
    ├── window_2.py
    ├── window_3.py
    └── window_4.py
```

### 2.1 文件说明

- WindowUI.py: 通过Qt Designer生成的UI文件的Python实现，定义了窗体的基本结构和布局。
- LoadUI.py: 加载通过Qt Designer生成的UI文件，并将其应用到自定义的QWidget子类中。
- mywindow.py: 创建一个简单的QWidget窗口，并显示出来。
- window_2.py: 创建一个QMainWindow窗口，添加状态栏和菜单栏，并显示出来。
- window_3.py: 创建一个QDialog窗口，并显示出来。
- window_4.py: 创建一个自定义的QWidget子类，设置窗口的各种属性（如标题、图标、背景颜色、透明度等），并显示出来。

## 3. 代码说明

- WindowUI.py: 包含Ui_Form类，定义了窗体的UI结构。setupUi方法用于设置窗体的基本属性，retranslateUi方法用于翻译窗体中的文本。
- LoadUI.py: 包含UI类，继承自QWidget，并在构造函数中加载通过Qt Designer生成的UI文件。
- mywindow.py: 创建一个简单的QWidget窗口，并调用show方法显示出来。
- window_2.py: 创建一个QMainWindow窗口，设置状态栏和菜单栏，并调用show方法显示出来。
- window_3.py: 创建一个QDialog窗口，并调用show方法显示出来。
- window_4.py: 创建一个自定义的QWidget子类Window，设置窗口的各种属性（如标题、图标、背景颜色、透明度等），并调用show方法显示出来。

## 4. 依赖库

- PyQt6: 用于创建GUI应用程序的Python库。
- PyQt6-Qt6: PyQt6的Qt库。
- PyQt6_sip: PyQt6的SIP绑定库。

## 5. 运行环境

- Python 3.x
- PyQt6 6.8.0
- PyQt6-Qt6 6.8.1
- PyQt6_sip 13.9.1

## 6. 使用方法

### 6.1. 安装依赖库：

```bash
   pip install -r requirements.txt
```
