# This is an example of how to use this package.
# You can edit this file or touch an other file in this directory.

from lib import get_epicflow

task_list = [['../1.png', '../2.png', '../av.png'], ['../1.png', '../2.png', '../ava.png'], 
    ['../1.png', '../2.png', '../avav.png'], ['../1.png', '../2.png', '../avava.png']]

get_epicflow(task_list=task_list, thread_num=3, lib_path='./lib')