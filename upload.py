#-*- coding=utf-8 -*-
from qcloud_cos import CosClient
from qcloud_cos import UploadFileRequest
from qcloud_cos import UploadSliceFileRequest
from qcloud_cos import UpdateFileRequest
from qcloud_cos import UpdateFolderRequest
from qcloud_cos import DelFileRequest
from qcloud_cos import DelFolderRequest
from qcloud_cos import CreateFolderRequest
from qcloud_cos import StatFileRequest
from qcloud_cos import StatFolderRequest
from qcloud_cos import ListFolderRequest

import logging
import sys
import os
import shutil
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)
def cos_demo(mkdir,file_path):
    appid = xxxxxx               # 替换为用户的appid
    secret_id = u'xxxxxxx'         # 替换为用户的secret_id
    secret_key = u'xxxxxxx'         # 替换为用户的secret_key
    region = "tj" #           # 替换为用户的region，目前可以为 shanghai/guangzhou
    cos_client = CosClient(appid, secret_id, secret_key, region)
    bucket = u'xxxx'
    request = UploadFileRequest(bucket, u'/'+mkdir+'/'+file_path+'', u''+file_path+'')
    upload_file_ret = cos_client.upload_file(request)
    print logger.info("upload file, return message: " + str(upload_file_ret))
if __name__ == '__main__':
    print "************welcome Rain file uploading RainCloud2.0************"
    mkdir = raw_input('This-------->>>mkdir:')
    while 1:
        file_path = raw_input('This------>>>File:')
        file_path = file_path.split('\\')
        path = ""
        for l in range(0, len(file_path)):
            path = path + str(file_path[l])
            if l < len(file_path) - 1:
                path = path + "/"
        print path
        shutil.copyfile(path, file_path[-1])
        cos_demo(mkdir, file_path[-1])
        # shutil.copyfile(path, '1.png')
        os.remove(file_path[-1])
        # result = raw_input('Continue------>>>y/n:')
        # if result!='y':
        #     break
