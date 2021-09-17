import src.path.pathCheck as pathCheck
import src.user.getUser as getUser
import src.course.foreWork as foreWork
import time, hashlib, requests, json
import requests.utils
from os import listdir

from rich.console import Console
from rich.table import Column, Table





if __name__ == '__main__':
    header = {'Accept-Encoding': 'gzip',
              'Accept-Language': 'zh_CN',
              'Host': 'i.chaoxing.com',
              'Connection': 'Keep-Alive',
              'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z) com.chaoxing.mobile/ChaoXingStudy_3_5.21_android_phone_206_1 (SM-G9350; Android 5.1.1; zh_CN)_1969814533'
              }
    usernm, session = getUser.get_session()
    chapterids, course = foreWork.find_courses(usernm,session)
    jobs = foreWork.find_objectives(usernm,chapterids,course['courseid'],session)

    # login('13554337909','20000204')
    # check_file('save/13554337909/courseid.json')
