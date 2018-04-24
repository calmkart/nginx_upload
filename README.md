# mupload后台以及客户端

------

## 部署指南

```shell
pip install -r requirements.txt
#文件夹下的nginx替换系统的nginx,用文件夹下的nginx.conf替换系统的nginx.conf
gunicorn -w4 -b 0:9528 server:app
python rm_timer.py

```
你也可以选择自己编译nginx,要用到nginx-fancyindex和nginx-upload-module:   

--add-module=../ngx-fancyindex --add-module=../nginx_upload_module    

注意，环境是python2   
server.py为mupload的处理后台     
client.py为mupload的客户端(推荐编译后使用)    
rm_timer.py会定时清理上传文件(默认保留7天)     
请配合nginx_upload_page使用   
