# Wi-Fi Digital Microscope

We bought <a href="https://www.amazon.de/-/en/Digital-Microscope-Industrial-Portable-Support/dp/B07YZ8WL7Q">this microscope</a>, but we noticed that it does not connect to the computer with USB and only works with its application.

After a lot of searching, I found that this company has no official website and it did not have any source code.

![1000x W04 WiFi Digital Microscope USB Industrial Microscope Camera Portable Support IOS/Android System, Tablet](https://m.media-amazon.com/images/I/41XtqSZr1GL.jpg)

So I decided to write this script using reverse engineering and get the frames using udp protocol.

## Getting started
```
pip install opencv-python

python3 main.py
