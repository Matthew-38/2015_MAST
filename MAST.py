ERRORCODES=["ERROR: The page range should be a comma and/or dashed sequence only. No spaces. E.g. (1,3-6)",
			"ERROR: Names should have no spaces. Use hyphens for double names; underscores for many names",
			"ERROR: One or more required fields are blank",
			]
GENRES=["student card","halfway review"]
ANNEES=["2012","2013"]
TRIMESTERS=["",'(1)','(2)','(3)','(4)','(Jan)','(Feb)','(Mar)','(Apr)','(May)','(Jun)','(Jul)','(Aug)','(Sept)',
			'(Oct)','(Nov)','(Dec)']
SOCIETES=["C1","C2","C3"]
Names=[""]
alwaysOnTop=True #move to file settings
fin=open("settings.ini")
def getSettings():
	outL=[]
	temp=fin.readline().split("\t")[1].split(',')
	for item in temp:
		outL.append(item.strip())
	outL.sort()
	return outL
GENRES=getSettings()
ANNEES=getSettings()
SOCIETES=getSettings()
alwaysOnTop=fin.readline().split("\t")[1]

import os
from Tkinter import *
datalines=[["-"," -"," -"," -"," -"]] #example: ["1,2,3","otoole","student card","2015","je"],
# ["5,6,7","EVANS","student card","2014-2015","je"]

#Get File List
pdflist=[]
def getFileList():
	Filelist=list(os.walk("."))[0][2]
	del pdflist[:]
	for item in Filelist:
		if ".pdf" in item.lower():
			pdflist.append(item)
	if len(pdflist) == 0: 
		pdflist.append["Error - no pdf files in current directory"]
		#Block program here
getFileList()
def show(txt):
	stringVars[8].set(txt)
def testData(inL):
	if ' ' in inL[0]: 
		show(ERRORCODES[0])
		return False
	if len(inL[0])==0 or len(inL[1])==0:
		show(ERRORCODES[2])
		return False
	if ' ' in inL[1]:
		show(ERRORCODES[1])
		return False
	return True
def form(inL):
	bourne=inL[0]
	nom=inL[1].upper()
	genre=inL[2].lower()
	annee=inL[3]
	societe=inL[4].upper()
	outStr=' {} -o "{} {} {} {}.pdf"'.format(bourne,nom,genre,annee,societe)
	return outStr
def updateUpperAnnee(event=0):
	i=ANNEES.index(stringVars[5].get())
	upperAnnee=["same"]
	print(i)
	if i<len(ANNEES)-1:
		upperAnnee.extend(ANNEES[i+1:])
	menuAnnee2["menu"].delete(0, "end")
	def callback(item):
		menuAnnee2.configure(text=item)
	for x in upperAnnee:
		menuAnnee2["menu"].add_command(label=x, command=lambda item=x: menuAnnee2.setvar(menuAnnee2.cget("textvariable"),value=item))
	#stringVars[6].set("same") #I know this is a bug, but I think it might help to leave it out.This would allow backwards years, but it may be useful
def editDataline(event=0):
	selected=list(event)
	i=datalines.index(selected)
	if selected[0] !="-": #make sure it is not dummy
		del datalines[i]
		menuOutputs["menu"].delete(i)
		anneeGrp=event[3]
		stringVars[9].set("")
		if "(" in anneeGrp:
			anneeGrp,trimester= anneeGrp[0:-1].split("(")
			stringVars[9].set("("+trimester+")")
		event[3]=anneeGrp.split("-")[0]
		event.insert(4, "same")
		if "-" in anneeGrp:
			event[4]=anneeGrp.split("-")[1]
		for j in range(len(event)):
			stringVars[j+2].set(event[j])
	stringVars[1].set("View or Edit existing entries here")
def takeDataline(event=0):
	if stringVars[3].get() not in Names: Names.append(stringVars[3].get()) #if clause eliminates repetition
	Names.sort()
	historyMenuUpdate()
	annee=stringVars[5].get()
	if stringVars[6].get() != "same":
		annee=stringVars[5].get()+"-"+stringVars[6].get()
	if stringVars[9]!="":
		annee+=stringVars[9].get()
	inL=[stringVars[2].get(),stringVars[3].get(),stringVars[4].get(), annee, stringVars[7].get()]
	if testData(inL):
		datalines.append(inL)
		global menuOutputs
		menuOutputs = OptionMenu(root,stringVars[1],*datalines, command=editDataline)
		menuOutputs.grid(row=1, column=1, columnspan=6, sticky="we")
		#menuOutputs["menu"].add_command(label=inL, command=lambda item=inL: menuOutputs.setvar(menuOutputs.cget("textvariable"),value=item))
		show("SUCCESS: Command added to list :-)")
		endLimit=inL[0].split(",")[-1].split("-")[-1]
		endLimit=int(endLimit)+1
		if "-" in inL[0]:
			if (int(inL[0].split("-")[1])-int(inL[0].split("-")[0])==1):
				endLimit=str(endLimit)+"-"+str(endLimit+1)
		stringVars[2].set(endLimit)
def convert(event=0):
	for item in datalines:
		os.system("cpdf.exe "+stringVars[0].get()+form(item))
	show("Success. Please exit, sort files and start again")
def makeCS(*args):
	curNom=stringVars[3].get()
	stringVars[3].set("CANSPEAK("+curNom+")")
def historyMenuUpdate():
	menu=globals()["menuNom"].children["menu"]
	menu.delete(0, "end")
	for value in Names:
		menu.add_command(label=value, command=lambda v=value: stringVars[3].set(v))
#GUI
root = Tk()
root.title("MAST 2.1")
if alwaysOnTop: root.wm_attributes("-topmost", 1)
stringVars=[StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root),StringVar(root)]
Label(root, text="Input:").grid(row=0)
stringVars[0].set(pdflist[0])
menuInput = OptionMenu(root,stringVars[0],*pdflist)
menuInput.grid(row=0, column=1, columnspan=2, sticky="we")
Label(root,text="Machine Assisted Scanning Toolkit II",fg="blue", bg="#99ffff").grid(row=0, column=3, columnspan=4)

labelOutputs = Label(root, text="Outputs:").grid(row=1)
menuOutputs = OptionMenu(root,stringVars[1],*datalines, command=editDataline)
menuOutputs.grid(row=1, column=1, columnspan=6, sticky="we")
stringVars[1].set("View or Edit existing entries here")
buttonConvert=Button(root, text="Convert!", command=convert)
buttonConvert.grid(row=1, column=7)

entryBourne=Entry(root,textvariable=stringVars[2], width=6)
entryBourne.grid(row=2)
stringVars[2].set(1)
entryNom=Entry(root,textvariable=stringVars[3])
entryNom.grid(row=2, column=1)
menuGenre=OptionMenu(root,stringVars[4],*GENRES)
menuGenre.grid(row=2,column=2)
stringVars[4].set("student card")
menuAnnee1=OptionMenu(root,stringVars[5],*ANNEES, command=updateUpperAnnee)
menuAnnee1.grid(row=2,column=3)
stringVars[5].set("2015")
menuAnnee2=OptionMenu(root,stringVars[6],"same")
menuAnnee2.grid(row=2,column=4)
updateUpperAnnee()
stringVars[6].set("same")
menuTrimester=OptionMenu(root, stringVars[9], *TRIMESTERS)
menuTrimester.grid(row=2,column=5)
entrySociete=Entry(root,textvariable=stringVars[7], width=10)
entrySociete.grid(row=2,column=6)
stringVars[7].set(SOCIETES[0])
buttonAdd=Button(root, text="Add",command=takeDataline)
buttonAdd.grid(row=2, column=7, sticky="we")
Label(root, text="History:").grid(row=3, column=0, sticky='e')
menuNom=OptionMenu(root,stringVars[3],*Names)
menuNom.grid(row=3,column=1,sticky="we")
buttonCanspeak=Button(root,text="<=Canspeak", command=makeCS)
buttonCanspeak.grid(row=3,column=2, sticky="w")
menuSociete=OptionMenu(root,stringVars[7],*SOCIETES)
menuSociete.grid(row=3,column=6, sticky="we")
Label(root, textvariable=stringVars[8]).grid(row=4, columnspan=7, sticky="we") #no need to ref afterwards, since it has a strvar
#Startup Seq
show("Tip: don't worry about capitalisation - MAST will take care of it :-)")
root.mainloop()

