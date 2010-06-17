#!/usr/bin/python
# -*- coding: utf-8 -*-
# twitter/tmtの監視とメールを送る処理を行う
import os 

homePath = os.path.abspath(os.path.dirname(__file__))

import picklefile,tmt,datetime,tmtBot
try:
	userData = picklefile.read(homePath+"/user/twdata_tmtMail")
except:
	userData = []
	

# userData は、({"user":user,"mail":mail,
# "time":nexttime(次の定期更新時刻),"now":flag(直ぐに送信するか)},...)
tmtBot.tmtBot(userData)
picklefile.write(homePath+"/user/twdata_tmtMail",userData)

for u in userData:
	
	if u["now"]:
		u["now"] = False
		tmt.tmt(u["user"],u["mail"])
		
	#もし最終更新時刻～現在時刻の間にtimeがあったら、メールを送る
	#elif datetime.today() > u["time"] and \
	#	u["time"] > latestTime :
	tmt.sendTmt(u["user"],u["mail"])
	u["time"] += datetime.timedelta(days=1)

picklefile.write(homePath+"/user/twdata_tmtMail",userData)
