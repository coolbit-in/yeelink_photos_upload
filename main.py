#/bin/env python
# -*-coding:utf=8 -*-
import os,time,subprocess,shlex
import urllib2
def upload_yeelink(image_name, log_file):
    url = 'http://api.yeelink.net/v1.0/device/719/sensor/8613/photos'
    length = os.path.getsize(image_name)
    image_data = open(image_name, 'rb')
    request = urllib2.Request(url, data=image_data)
    request.add_header('U-ApiKey', '14765d9cc6aec5057880398486d08f9c')
    request.add_header('Content-Length', '%d' % length)
    res = urllib2.urlopen(request).read().strip()
    log_file.write(res + '\n')

if __name__ == '__main__':
    images_path = os.path.join(os.getcwd(), 'image')
    log = open(os.path.join(os.getcwd(), 'output.log'),'w+')
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    com_line = 'fswebcam -d /dev/video0 -r 320x240 --bottom-banner --title "%s" --no-timestamp %s/%s.jpg'
    while True:
        time_now = time.strftime('%Y-%m-%d-%H-%M-%S')
        com_line_now = com_line % (time_now, images_path, time_now)
        subprocess.call(shlex.split(com_line_now), stdout=log, stderr=log)
        upload_yeelink('%s/%s.jpg' % (images_path, time_now), log)
        print com_line_now
        time.sleep(11)
