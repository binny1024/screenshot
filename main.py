# -*- coding: utf-8 -*-
import configparser
import math
import time

from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

import screenshot

cp = configparser.ConfigParser()
cp.read(r'G:/MyPython/screenshot/config.ini', encoding='utf-8')


@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


def run_shell(task_id, room_url,scroll_top, dur, pit_path, interval_time, fn_list, rt_list):
    # screenshot.capture(url)
    ss = screenshot.ScreenShot(task_id, room_url, scroll_top,dur, pit_path, interval_time, fn_list, rt_list)
    ss.start()
    return


def gen_pits(base_path, task_id, total_dur, interval_time):
    st = int(time.time()) + interval_time
    total_count = int(math.ceil(total_dur / interval_time))
    now_count = 0
    rt_list = []
    at_list = []
    now = st
    while now_count < total_count:
        now_count += 1
        now += interval_time
        at_list.append(str(task_id) + "-" + str(now) + "-" + str(now_count))

        pit = str(task_id) + "-" + str(now) + "-" + str(now_count) + ".jpg"
        rt_list.append(cp.get('base', 'pit_host') + base_path + pit)
    return rt_list, at_list


@dispatcher.add_method
def screenshot_nb(**kwargs):
    print(kwargs)
    task_id = kwargs['id']
    interval_time = kwargs['interval_time']
    room_url = kwargs['room_url']
    scroll_top = kwargs['scroll_top']
    total_time = kwargs['total_time']
    base_img_path = cp.get('base', 'base_img_path')
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    current_time = time.strftime("%H-%M-%S", time.localtime())

    pit_path = '%spit/%s/%s/%s/' % (base_img_path, current_date, task_id, current_time)

    base_path_current_date = time.strftime("%Y-%m-%d", time.localtime())
    print(base_path_current_date)
    base_path_current_time = time.strftime("%H-%M-%S", time.localtime())
    base_path = '/%s/%s/%s/' % (base_path_current_date, task_id, base_path_current_time)

    rt_list, at_list = gen_pits(base_path, task_id, total_time, interval_time)

    run_shell(task_id, room_url, scroll_top, total_time, pit_path, interval_time, at_list, rt_list)
    print(rt_list)
    return rt_list


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}

    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == "__main__":
    hostname = cp.get('base', 'host')
    port = cp.get('base', 'port')
    print('hostname = ', hostname)
    print('port = ', port)
    run_simple(hostname, port, application)
