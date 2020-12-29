import boto3
import numpy as np
import io 
import cv2
from libs.imageLib import Image 
from libs.handlerLib import handler

def main(event, context):
    def func(event, context):
        s3 = boto3.resource('s3', region_name='us-east-1')
        bucket = s3.Bucket('blueprint-mockupgen-logo-upload')
        key = 'Covid.PNG'

        img = bucket.Object(key).get().get('Body').read()

        s3img = cv2.imdecode(np.asarray(bytearray(img)), cv2.IMREAD_COLOR)

        img2 = Image(s3img, "s3Image")
        img2 = img2.cvt_color('RGBA')
        shape = img2.shape
        return shape
    return handler(func(event, context)) 









