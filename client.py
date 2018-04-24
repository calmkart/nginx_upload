#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-11 11:41:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import requests
import hashlib
import sys, getopt

class mupload_client():
    # 待上传文件路径
    FILE_UPLOAD = ""
    # 上传接口地址
    UPLOAD_URL = "http://10.41.12.246/api/upload"
    # 单个片段上传的字节数
    SEGMENT_SIZE = 1048576
    
    
    def upload(self, fp, file_pos, size, file_size):
        session_id = self.get_session_id()
        fp.seek(file_pos)
        payload = fp.read(size)
        file_name = os.path.basename(self.FILE_UPLOAD)
        content_range = "bytes {file_pos}-{pos_end}/{file_size}".format(file_pos=file_pos,
                                                                        pos_end=file_pos+size-1, file_size=file_size)
        headers = {'Content-Disposition': 'attachment; filename="'+file_name+'"', 'Content-Type': 'application/octet-stream',
                   'X-Content-Range': content_range, 'Session-ID': session_id, 'Content-Length': size}
        res = requests.post(self.UPLOAD_URL, data=payload, headers=headers)
        if res.status_code == 200:
            print("#####################################################")
            print(res.text)
            print("#####################################################")
    
    
    # 根据文件名hash获得session id
    def get_session_id(self):
        m = hashlib.md5()
        file_name = os.path.basename(self.FILE_UPLOAD)
        m.update(file_name)
        return m.hexdigest()
    
    def progress(self, file_pos, file_size):
        percent = float(file_pos)*100/float(file_size)
        sys.stdout.write("%.2f"%percent)
        sys.stdout.write("%\r")  
        sys.stdout.flush() 


    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv, "hf:")
        except getopt.GetoptError:
            print 'Usage: mupload: invalid option'
            print '        -h    show help info'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print "Usage: mupload [option] [param]"
                print "                  -f     local file path"
                sys.exit()
            elif opt == "-f":
                self.FILE_UPLOAD = arg
                file_pos = 0
                file_size = os.path.getsize(self.FILE_UPLOAD)
                fp = open(self.FILE_UPLOAD, "r")
                while True:
                    self.progress(file_pos, file_size)
                    if file_pos + self.SEGMENT_SIZE >= file_size:
                        self.upload(fp, file_pos, file_size - file_pos, file_size)
                        fp.close()
                        break
                    else:
                        self.upload(fp, file_pos, self.SEGMENT_SIZE, file_size)
                        file_pos = file_pos + self.SEGMENT_SIZE



if __name__ == "__main__":
    mupload_client = mupload_client()
    mupload_client.main(sys.argv[1:])

