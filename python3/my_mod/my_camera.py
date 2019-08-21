#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import time

def capture_camera():
        with cv2.VideoCapture(0) as cap:
            cv2.imshow('camera capture', frame)

def main():
    capture_camera()

if __name__ == "__main__":
    main()
