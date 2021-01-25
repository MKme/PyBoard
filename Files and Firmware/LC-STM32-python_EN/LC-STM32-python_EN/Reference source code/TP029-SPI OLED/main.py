import pyb
from ssd1306 import SSD1306


display = SSD1306(pinout={'dc': 'Y9',
                          'res': 'Y10'},
                  height=64,
                  external_vcc=False)

led_red = pyb.LED(1)
led_red.off()
display.poweron()
display.init_display()
display.draw_text(1,1,'Hello World!',size=1,space=1)
display.draw_text(1,10,'this is TPYBoard V102！',size=1,space=1)
# 显示出你想要显示的内容
display.display()
 