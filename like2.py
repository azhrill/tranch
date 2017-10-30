# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess


cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()
cl 
print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
i = 0
c_text = """this is autolike """

def autolike(op):
    try:
		for posts in cl.activity(1)["result"]["posts"]:
			if wait["posts"] == True:
				if posts["postInfo"]["liked"] is False:
					cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					print u"liked" + str(i)
					i += 1
    except Exception as e:
            print e

   