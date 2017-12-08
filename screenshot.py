from selenium import webdriver
from PIL import Image
import threading
import time
import os
import configparser

import redis


class ScreenShot(threading.Thread):

    def __init__(self, task_id, room_url, dur, pit_path, interval_time, fn_list, rt_list):
        threading.Thread.__init__(self)
        self.task_id = str(task_id)
        self.room_url = room_url
        self.dur = dur
        cp = configparser.ConfigParser()
        cp.read(r'G:/MyPython/screenshot/config.ini', encoding='utf-8')
        self.cp = cp
        self.pit_path = pit_path
        self.interval_time = interval_time
        self.fn_list = fn_list
        redis_host = self.cp.get('base', 'redis_host')
        redis_post = self.cp.get('base', 'redis_post')
        redis_db = self.cp.get('base', 'redis_db')
        self.r = redis.StrictRedis(redis_host,redis_post ,redis_db)
        self.rt_list = rt_list

    def create_icon(self, file_temp, file):
        im = Image.open(file_temp)
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, im)
        bg.save(file)

    def run(self):
        global browser
        try:
            browser = webdriver.Chrome(self.cp.get('base', 'chromeDriver'))
            browser.set_window_size(int(self.cp.get('base', 'img_width')), int(self.cp.get('base', 'ima_heigh')))
            browser.get(self.room_url)
            # browser.refresh();
            js = """
                (function () {
                    document.title += "xiaohulu-scroll-done";
                })();
            """

            js = """
                (function () {
                    var quanmin = document.getElementsByClassName("room_w-blessing-iconguide")[0];
                    if(quanmin != undefined){
                        quanmin.style.display="none";
                    }
                    var bilibili = document.getElementsByClassName("upgrade-intro-component")[0];
                    if(bilibili != undefined){
                        bilibili.style.display="none";
                    }
                    bilibili = document.getElementById("g_btnp");
                    if(bilibili != null){
                        bilibili.style.display="none";
                    }
                })();
            """

            # document.getElementsByClassName("room_w-blessing-iconguide")[0].style.display="none";
            # for i in xrange(30):
            #     if "xiaohulu-scroll-done" in browser.title:
            #         break
            #     time.sleep(5)

            dit_path = self.pit_path
            # self.cp.get('base', 'base_img_path')+"pit/"+time.strftime("%Y%m/%d", time.localtime(
            # ))+"/"+self.taskid+"/"+time.strftime("%H%M%S", time.localtime())+"/"
            is_exists = os.path.exists(dit_path)
            if not is_exists:
                os.makedirs(dit_path)

            time.sleep(self.interval_time)

            browser.execute_script(js)
            list_shot = []
            l = len(self.fn_list)
            for i in range(l):
                temp = self.fn_list.pop(0)
                path = self.rt_list.pop(0)
                ss_temp_path = dit_path + temp + "_temp.png"
                ss_path = dit_path + temp + ".jpg"
                browser.get_screenshot_as_file(ss_temp_path)
                self.create_icon(ss_temp_path, ss_path)

                list_shot.append(path)

                if os.path.exists(ss_temp_path):
                    os.remove(ss_temp_path)
                time.sleep(self.interval_time)
            else:
                redis_key = "screenshot_" + self.task_id
                if len(list_shot) > 0:
                    self.r.lpush(redis_key, *list_shot)
                # browser.close()
        except:
            browser.close()
        else:
            browser.close()
