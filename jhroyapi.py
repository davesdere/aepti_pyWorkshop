# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv
import requests

###################################################################
#####               EXEMPLE #1 AVEC GOOGLE MAPS               #####
###################################################################

# url1 = "https://maps.googleapis.com/maps/api/geocode/json?address=5201,Radisson,Montr%C3%A9al,QC"
# geo = requests.get(url1).json()

# latitude = geo["results"][0]["geometry"]["location"]["lat"]
# longitude = geo["results"][0]["geometry"]["location"]["lng"]

# print(latitude,longitude)

###################################################################
#####               EXEMPLE #2 AVEC GOOGLE MAPS               #####
###################################################################

# fichier1 = "adressesmedias.csv"

# f1 = open(fichier1)
# medias = csv.reader(f1)
# next(medias)

# for media in medias:
# 	print(media)
# 	url1 = "http://maps.googleapis.com/maps/api/geocode/json?address={}".format(media[2])
# 	geo = requests.get(url1).json()

# 	try:
# 		latitude = geo["results"][0]["geometry"]["location"]["lat"]
# 		longitude = geo["results"][0]["geometry"]["location"]["lng"]

# 		print("Le média {} est situé à la latitude {} et à la longitude {}".format(media[0],latitude,longitude))

# 	except:
# 		print("Impossible pour le média {}".format(media[0]))

######################################################################
#####               EXEMPLE #1 AVEC FACEBOOK PAGES               #####
######################################################################

# jeton = "EAACEdEose0cBACo5wcFV4MKXtYqTP49n9Bv5MyRzrjFPQHI4wilBymqZBOFEtfGkw82fYyrGsdJtUYHjOkqZBZAdDdpin0783HGECDZBqCoGTZA6ZCgVz37FZCiZAJUXfZAHfIhXHTZBProBtQYbKx1ZAeIQ2nYMwYPCGZApgnEphiEdjuiy2HwS0cW8rMYH8OxvZCwMZD"

# url2 = "https://graph.facebook.com/v2.12/122369341291136?fields=posts.limit(100)&access_token={}".format(jeton)

# pkp = requests.get(url2).json()

# n = 0

# fichier2 = "pkpSurFacebook.csv"

# for post in pkp["posts"]["data"]:
# 	n += 1
# 	print("~"*80)
# 	date = post["created_time"]
# 	try:
# 		message = post["message"]
# 		print(n,date,message)
# 	except:
# 		message = "Rien ici"
# 		print(n,date,message)
# 	# date = post["created_time"]
# 	ligne = [n,date,message]
# 	dead = open(fichier2,"a")
# 	obies = csv.writer(dead)
# 	obies.writerow(ligne)

# if len(pkp["posts"]["data"]) > 99:
# 	next = pkp["posts"]["paging"]["next"]
# 	posts = requests.get(next).json()
# 	while(True):
# 		try:
# 			for post in posts["data"]:
# 				n += 1
# 				print("~"*80)
# 				date = post["created_time"]
# 				try:
# 					message = post["message"]
# 					print(n,date,message)
# 				except:
# 					message = "Rien ici"
# 					print(n,date,message)
# 				ligne = [n,date,message]
# 				zeds = open(fichier2,"a")
# 				dead = csv.writer(zeds)
# 				dead.writerow(ligne)

# 			posts = requests.get(posts["paging"]["next"]).json()

# 		except KeyError:
# 			print("yo")