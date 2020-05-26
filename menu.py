#!/usr/bin/python3.8
#coding:u8


from random import randrange

def hasard(liste) :
	number = 0
	for element in liste :
		number +=1
	word = liste[randrange(number)]
	return word
