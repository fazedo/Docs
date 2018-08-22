#!/usr/bin/python3


import sys
import os
import string
import datetime

capitulo="cap_superficies"
nome_saida="saida.tex"



texto_inicial='\
\\documentclass{standalone}\
\\usepackage{pstricks-add}\
\\usepackage{pstricks,pst-plot}\
\\usepackage[dvips]{graphicx}\
\\usepackage{pst-math}\
\\usepackage{pst-plot}\
\\usepackage{pst-circ}\
\\usepackage[brazil]{babel}\
\\usepackage[utf8]{inputenc}\
\\usepackage[T1]{fontenc}\
\\usepackage{amsmath}\
\\usepackage{amssymb}\
\\usepackage{amsthm}\
\\usepackage{mathtools}\
\\usepackage{pst-3dplot}\
\\usepackage{pst-solides3d}\
\\newcommand{\sen}{\operatorname{sen}\,}\
\\newcommand{\senh}{\operatorname{senh}\,}\
\\renewcommand{\sin}{\operatorname{sen}\,}\
\\renewcommand{\sinh}{\operatorname{senh}\,}\
\\begin{document}'

texto_final='\\end{document}'


ifile = open(capitulo+".tex",'r')
linhas = ifile.readlines()
ifile.close()    

token=0
k=1
texto=""
novotexto=""

for line in linhas:
	sl=line.strip()
	if len(sl)>0:
		if sl[0] != "%":	
			if (line.find("\\begin{pspicture}") !=-1) or (line.find("\\psset") !=-1):
				token=1
			if token==1:
				texto=texto+line
			if token==0:
				novotexto=novotexto+line
			if line.find("\\end{pspicture}") !=-1:
				token=0
				nomearq="figura_"+str(k)
				print(nomearq)
				ofile = open("./figs/"+nomearq+".tex",'w')
				ofile.write(texto_inicial+texto+texto_final)
				ofile.close()
				#os.system("latex "+nomearq)
				k=k+1
				texto='' 
				novotexto=novotexto+"\n\\includegraphics{"+capitulo+"/figs/"+nomearq+"}"

os.system("cd ..")
ofile = open(nome_saida,'w')
ofile.write(novotexto)
ofile.close()


