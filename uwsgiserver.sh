#! /bin/sh
#
# uwsgiserver.sh
# Copyright (C) 2015 mapleray <zhiwuliao#gmail.com>
#
# Distributed under terms of the MIT license.
#


if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "zh" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi --ini /root/workspace/appleQuote/website_uwsgi.ini
        uwsgi --ini /root/workspace/appleQuote/website_uwsgi2.ini
        uwsgi --ini /root/workspace/appleQuote/website_uwsgi3.ini
        echo "Start uwsgi service [OK]"
    fi

elif [ $1 = stop ];then
    killall -s INT uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -s INT uwsgi
    uwsgi --ini /root/workspace/appleQuote/website_uwsgi.ini
    uwsgi --ini /root/workspace/appleQuote/website_uwsgi2.ini
    uwsgi --ini /root/workspace/appleQuote/website_uwsgi3.ini
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi
