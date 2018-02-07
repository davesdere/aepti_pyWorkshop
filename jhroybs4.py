# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

###########################################################
#####               EXEMPLE AVEC KIJIJI               #####
###########################################################

# data = "donneesKijiji.csv"

# for x in range(1,101):
# 	url = "https://www.kijiji.ca/b-maison-a-vendre/grand-montreal/page-{}/c35l80002".format(x)
# 	# print(url)
# 	contenu = requests.get(url)
# 	page = BeautifulSoup(contenu.text,"html.parser")
# 	# print(page)

# 	urlsDesMaisons = page.find_all("div", class_="info-container")
# 	for urlMaison in urlsDesMaisons:
# 		infos = []
# 		# print(urlMaison)
# 		# print(urlMaison.a["href"])
# 		urlMaison = "https://www.kijiji.ca{}".format(urlMaison.a["href"])
# # 		# print(urlMaison)
# 		infos.append(urlMaison)

# 		contenu2 = requests.get(urlMaison)
# 		page2 = BeautifulSoup(contenu2.text,"html.parser")

# 		# titre = page2.title
# 		# # print(titre)
# 		# titre = page2.title.text
# 		# # print(titre)
# 		# titre = page2.title.text.split("|")
# 		# # print(titre)
# 		# titre = page2.title.text.split("|")[0]
# 		# print(titre)
# 		titre = page2.title.text.split("|")[0].strip()
# 		# print(titre)
# 		infos.append(titre)

# 		prix = page2.find("span",class_="currentPrice-2872355490").text.strip()
# 		# print(prix)
# 		if prix[-1] == "$":
# 			prixNb = float(prix[:-1].replace("\xa0","").replace(",","."))
# 		else:
# 			prixNb = "Non indiqué"
# 		infos.append(prix)
# 		infos.append(prixNb)

# 		latitude = page2.find("meta",attrs={"property":"og:latitude"})["content"]
# 		longitude = page2.find("meta",attrs={"property":"og:longitude"})["content"]
# # 		# print(latitude,longitude)
# 		infos.append(latitude)
# 		infos.append(longitude)

# 		print(infos)

# 		dead = open(data,"a")
# 		obies = csv.writer(dead)
# 		obies.writerow(infos)

###########################################################
#####               EXEMPLE AVEC LA SAQ               #####
###########################################################

n = 0
donneesSAQ = "donneesSAQ.csv"

for x in range(1,6):
	fichier = "saq{}.html".format(x)
	print(fichier)

	# Pas besoin de requests
	page3 = BeautifulSoup(open(fichier),"html.parser")
	# print(page3)
	liens = page3.find_all("div",class_="wapProduit")

	for lien in liens:
		produit = []
		n += 1
		url = lien.a["href"]
		# print(n,url)
		produit.append(n)
		produit.append(url)

		entetes = {
			"User-Agent":"Jean-Hugues Roy - cours de BI à l'UQAM",
			"From":"skywalker.luke@uqam.ca",
			"Cookie":"pageViewPreference=grid; WC_SESSION_ESTABLISHED=true; WC_ACTIVEPOINTER=%2d2%2c20002; WC_PERSISTENT=eoScfaN7BwFxnjYxz0ikkxCs6LI%3d%0a%3b2018%2d02%2d05+14%3a03%3a20%2e742%5f1517857337031%2d17353%5f20002%5f226117632%2c%2d2%2cCAD%5f20002; WC_AUTHENTICATION_226117632=226117632%2cPO6xVo%2fmfxJ4RBiaIG9gUKsgm08%3d; WC_USERACTIVITY_226117632=226117632%2c20002%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cqPTj6hLO%2b9ZCXQjKOohYt7rJBy6N1JfYKmlfiZax1UHUeFQZYa2iUiEO%2f9yyh1MhjUgiThcjs09a%0aHOMunfWRHcfDKgtaXAHI2IpqHRcSMpxoRE%2fML%2bGliOSza4R2ICVvNH8HuqBdbpuCIhQJP1Rx%2bA%3d%3d; searchTermHistory=%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; JSESSIONID=00007bf2BzqDKdVYS35lkIlhtBg:16pap1lqp; __utma=246523739.157086077.1517857339.1517857339.1517865280.2; __utmb=246523739.20.9.1517869124352; __utmc=246523739; __utmz=246523739.1517857339.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); browserWarning=true"
		}

		contenido = requests.get(url,headers=entetes)
		# contenido = requests.get(url)
		p = BeautifulSoup(contenido.text,"html.parser")

		nom = p.title.text
		nom = nom.split("|")[0].strip()
		print(n,nom)
		produit.append(nom)

		prix = p.find("p",class_="price").text
		prix = prix.split(":")[1].strip()
		prixNb = float(prix[:-1].replace(",",".").strip())
		# print(prix,prixNb)
		produit.append(prix)
		produit.append(prixNb)

		codes = p.find("div",class_="product-description-row2").text
		# print(codes)
		codes = codes.split(":")
		# print(codes)
		codeSAQ = codes[1].split("\r\n")
# 		# print(codeSAQ)
		codeSAQ = codeSAQ[1].strip()
# 		# print(codeSAQ)
		codeCUP = codes[2].split("\r\n")
# 		# print(codeCUP)
		codeCUP = codeCUP[1].strip()
# 		# print(codeCUP)
		produit.append(codeSAQ)
		produit.append(codeCUP)

		details = p.find("div",id="details")
# 		# print(details)
		# pays = details.find("div",class_="right").text.strip()
# 		# print(pays)
# 		region = details.find("div",class_="right").find_next("div",class_="right").text.strip()
# 		# print(region)

		for items in details.find_all("div"):
			if items.text.strip() == "Pays":
				pays = items.find_next("div",class_="right").text.strip()
			if items.text.strip() == "Format":
				format = items.find_next("div",class_="right").text.strip()
# 		# print(pays)
# 		# print(format)

		produit.append(pays)
		produit.append(format)

		print(produit)

		loud = open(donneesSAQ,"a")
		lary = csv.writer(loud)
		lary.writerow(produit)