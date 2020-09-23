sudo modprobe -r v4l2loopback
sudo modprobe videodev
sudo modprobe v4l2loopback devices=1 video_nr=20 exclusive_caps=1
