### curl 命令
#### 不带滚动网页的请求(旧版)
    curl 127.0.0.1:4002 -d {"jsonrpc":"2.0","method":"screenshot_nb","params":{"id":321, "total_time":20, "interval_time":2, "room_url":"http://www.panda.tv/act/baozoumanhua20160824.html"},"id":200} -H "Content-Type:application/json"
#### 带滚动网页的请求（新版）
    curl  127.0.0.1:4002 -d '{"jsonrpc":"2.0","method":"screenshot_nb","params":{"id":321,"total_time":20,"interval_time":2,"scroll_top":"1000","room_url":"http://www.panda.tv/act/baozoumanhua20160824.html"},"id":200}' -H "Content-Type: application/json"
#### [安装Image库指令]
    http://www.cnblogs.com/Ray-liang/p/5415033.html
    http://blog.csdn.net/c_boy_lu/article/details/49816039
##### pip命令 进入到pip所在目录：我的是C:\Python\Scripts
    pip install -I --no-cache-dir -v Pillow
#### python 3
#### [安装Redis]
    python pip install redis
#### 下面是配置信息，供 configparser 读取
#### 新建 config.ini（文件名与扩展名不限）文件中

    [base]
    host = 127.0.0.1
    port = 4002
    chromeDriver = G://MyPython/screenshot/chromedriver
    #空默认项目地址,不为空最后要有'/'
    base_img_path = G://MyPython/screenshotimg/

    #截取的视频宽度
    img_width = 1900
    #截取的视频高度
    ima_heigh = 1600
    #视频加载时间
    video_load_time = 2
    #广告延时保护时间
    extend_time = 0
    #广告时间分水岭：广告时长<=10秒的，3秒截1次；广告时长>10秒的，按:广告时长X0.75（3/4间隔时间）
    ad_middle_time = 10
    #短广告截取图片间隔
    short_ad_space = 3
    #长广告截取图片系数
    long_ad_space = 0.75

    ad_server_tcp = http://
    ad_server_host = ad-xujianfeng.hub520.com

    redis_host = 127.0.0.1
    redis_post = 6379
    redis_db = 0
    pit_host = http://pic.xiaohulu.com

###  不同版本的chromeDriver对应不同版本的chrome浏览器
    http://blog.csdn.net/qijingpei/article/details/68925392

    chromedriver版本	支持的Chrome版本
    v2.25	|   v53-55
    v2.24	|   v52-54
    v2.23	|   v51-53
    v2.22	|   v49-52
    v2.21	|   v46-50
    v2.20	|   v43-48
    v2.19	|   v43-47
    v2.18	|   v43-46
    v2.17	|   v42-43
    v2.13	|  	v42-45
    v2.15	|  	v40-43
    v2.14	|  	v39-42
    v2.13	|  	v38-41
    v2.12	|  	v36-40
    v2.11	|  	v36-40
    v2.10	|  	v33-36
    v2.9	|  	v31-34
    v2.8	|  	v30-33
    v2.7	|  	v30-33
    v2.6	|  	v29-32
    v2.5	|  	v29-32