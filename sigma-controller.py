#!/usr/bin/env python
#coding: utf-8

# 
#	Controller for Sigma using magic to create illusions of reality.
#

from subprocess import call
import time
import webbrowser

def search():
	path = "searching.svg"
	call('firefox -P "Sigma" -url %s' % path, shell=True)


def normal():
	path = "http://technocake.xyz/sigma/test/prototype/search.html"
	call('firefox -P "default" -url %s' % path)

def hide_browser():
	call("killall firefox", shell=True)


def show_map():
	# switch focus or jump to new file...
	path = "JavaScript.mm"
	call("xdg-open %s" % path, shell=True)	


if __name__ == '__main__':
	#show_map()
	search()
	#normal()
	time.sleep(2)
	#hide_browser()

	webbrowser.close()
	
