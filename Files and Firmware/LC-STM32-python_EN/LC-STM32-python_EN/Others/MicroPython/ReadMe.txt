pyboard是一个可以运行MicroPython的小巧而强大的开发板。它通过USB数据线连接到电脑，并模拟出一个“U盘”来保存Python代码，还有一个用于编程的Python提示符（REPL）。你需要一个USB数据线，Windows，Mac和Linux都可以开发。
MicroPython完全兼容Python（3.4）语言，并针对嵌入式重写了解释器，因此可以在微控制器上运行。它做了许多优化，使其高效运行，并使用非常少的RAM。
MicroPython跑在pyboard裸板上，本质上为您提供了一个Python操作系统。内置的pyb模块包含控制板上可用外设（如UART，I2C，SPI，ADC和DAC）的函数和类。
观看此视频以了解pyboard的概述。
控制pyboard有三种主要方式：
REPL：通过USB连接到PC，电脑显示出USB虚拟串口（CDC VCP），您可以使用任何串口软件连接，并获得Python REPL提示。这样就可以立即输入和执行Python命令，就像在PC上运行Python一样。您还可以将REPL重定向到板上的任何UART。
远程脚本：您可以通过发送ctrl-A将其从REPL更改为原始REPL模式，然后以原始REPL模式，您可以向板子发送任意Python脚本，以便立即执行。可以使用Python脚本，这使得使用此模式非常简单：您只需运行python pyboard.py script_to_run.py，这将在pyboard上执行script_to_run.py，返回任何输出。
从文件：pyboard有一个小的，内置的文件系统，它是微控制器闪存的一部分。如果要扩展可用的存储空间，它也有一个SD卡插槽。当您将电脑板连接到电脑时，它显示为USB闪存存储设备，您可以通过这种方式访问（安装）内部文件系统和SD卡。如果将Python脚本复制到文件系统并将其称为main.py，那么当启动时，该脚本将执行此脚本。通过这种方式，您可以在不连接到PC的情况下运行脚本。
硬件的主要特点：
STM32F405RG微控制器
168 MHz Cortex M4 CPU，具有硬件浮点运算
1024K Flask 和192K RAM
Micro USB连接器，用于供电和REPL
Micro SD卡插槽，支持最高32G SD卡
3轴加速度计（MMA7660）
具有可选电池备份的实时时钟
左右有24个GPIO，底部有5个GPIO和LED以及button的引脚
3个12位ADC，可用在16个引脚
2个DAC，（X5和X6引脚）
4个LED（红，绿，黄，蓝）
1个复位按键和1个用户按键
3.3V LDO稳压器，能够提供高达300mA的电流
输入电压范围为3.6V至10V的
DFU引导加载器在ROM中，便于升级固件