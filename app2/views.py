from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
import wave
from datetime import datetime
from app2 import stri
import re
import os
# Create your views here.

def hi(request):
    # return HttpResponse('<h1>THIS IS MY WEBPAGE</h1>')
    return render(request,'voice_4.html')
def output(request):
    r = sr.Recognizer()
    s=""
    global drago
    drago=[]
    d={}
    index1=[]
    #s2=""
    s3=""
    k1=[]
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Please say something")
        # recognize speech using google
        while(True):
            try:
                audio = r.listen(source,timeout=10)
                s=s+' '+r.recognize_google(audio)
                
                if 'stop' in s:
                    s=s.replace("stop","")
                    break
            except:
                break
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

    print(s.lower())
    s=s.lower()
    s=s.replace("coma",",")
    s=s.replace("kama",",")
    
    
    for i in stri.l:
        k=s.find(i)
       # indices.append(k)
        index1.append(k)
    index1.append(len(s))
    index1.sort()
    if s.find("medical history")==-1:
        d["medicalhistory"]=''
    else:
        d["medicalhistory"]=s[s.find("medical history")+len("medical history"):index1[index1.index(s.find("medical history"))+1]]
    if s.find("current medical condition")==-1:
        d["current medical condition"]=''
    else:
        d["currentmedicalcondition"]=s[s.find("current medical condition")+len("current medical condition"):index1[index1.index(s.find("current medical condition"))+1]]
    if s.find("suggestions")==-1:
        d["suggestions"]=''
    else:
        d["suggestions"]=s[s.find("suggestions")+len("suggestions"):index1[index1.index(s.find("suggestions"))+1]]
    if s.find("drugs")==-1:
        d["drugs"]=''
    else:
        m=(s[s.find("drugs")+len("drugs"):index1[index1.index(s.find("drugs"))+1]].lower())
        print(m)
        m=m.replace("coma",",")
        m=m.replace("kama",",")
        k1=m.split(",")
        print(m)
        g=0
        for i in k1:
            drago1=[]
            m1=re.findall(r"\d+",i.strip())
            res=list(map(int,m1))
            print(res)
            m2=re.search(r"\d",i.strip())
            if len(m1)!=0:
                g=m2.start()
                if i[0:g].strip() in stri.l1:
                    drago1.append(i[0:g].strip())
                    for j in res:
                        print(j)
                        drago1.append(j)
                    print(drago1)
                    drago.append(drago1)
                else:
                    s3=s3+i.strip()+","
            else:
                if i.strip() in stri.l1:
                    #s2=s2+i.strip()+","
                    drago1.append(i.strip())
                    #drago.append(s2[:len(s2)-1])
                    drago.append(drago1)
                    #s2=" "
                    
                else:
                    s3=s3+i.strip()+","
                
        d["drugs"]=drago
        d["otherdrugs"]=s3[:len(s3)-1]
    if s.find("other complaints")==-1:
        d["othercomplaints"]=''
    else:
        d["othercomplaints"]=s[s.find("other complaints")+len("other complaints"):index1[index1.index(s.find("other complaints"))+1]]
    if s.find("family history")==-1:
        d["familyhistory"]=''
    else:
        d["familyhistory"]=s[s.find("family history")+len("family history"):index1[index1.index(s.find("family history"))+1]]
    if s.find("temperature")==-1:
        d["temperature"]=''
    else:
        d["temperature"]=s[s.find("temperature")+len("temperature"):index1[index1.index(s.find("temperature"))+1]]+"??C"
    if s.find("pulse")==-1:
        d["pulse"]=''
    else:
        d["pulse"]=s[s.find("pulse")+len("pulse"):index1[index1.index(s.find("pulse"))+1]]
    if s.find("hemoglobin")==-1:
        d["hemoglobin"]=''
    else:
        d["hemoglobin"]=s[s.find("hemoglobin")+len("hemoglobin"):index1[index1.index(s.find("hemoglobin"))+1]]
    if s.find("RBS")==-1:
        d["rbs"]=''
    else:
        d["rbs"]=s[s.find("RBS")+len("RBS"):index1[index1.index(s.find("RBS"))+1]]
    if s.find("allergies")==-1:
        d["allergies"]=''
    else:
        d["allergies"]=s[s.find("allergies")+len("allergies"):index1[index1.index(s.find("allergies"))+1]]
    if s.find("exercise")==-1:
        d["exercise"]=''
    else:
        d["exercise"]=s[s.find("exercise")+len("exercise"):index1[index1.index(s.find("exercise"))+1]]
    if s.find("lab findings")==-1:
        d["labfindings"]=''
    else:
        d["labfindings"]=s[s.find("lab findings")+len("lab findings"):index1[index1.index(s.find("lab findings"))+1]]
    if s.find("next meeting")==-1:
        d["nextmeeting"]=''
    else:
        d["nextmeeting"]=s[s.find("next meeting")+len("next meeting"):index1[index1.index(s.find("next meeting"))+1]]
    if s.find("diet plan")==-1:
        d["dietplan"]=''
    else:
        d["dietplan"]=s[s.find("diet plan")+len("diet plan"):index1[index1.index(s.find("diet plan"))+1]]
    if s.find("comments")==-1:
        d["comments"]=''
    else:
        d["comments"]=s[s.find("comments")+len("comments"):index1[index1.index(s.find("comments"))+1]]
    if s.find("chief complaints")==-1:
        d["chiefcomplaints"]=''
    else:
        d["chiefcomplaints"]=s[s.find("chief complaints")+len("chief complaints"):index1[index1.index(s.find("chief complaints"))+1]]
    if s.find("past history")==-1:
        d["pasthistory"]=''
    else:
        d["pasthistory"]=s[s.find("past history")+len("past history"):index1[index1.index(s.find("past history"))+1]]
    if s.find("patient name")==-1:
        d["patientname"]='NoName'
    else:
        d["patientname"]=s[s.find("patient name")+len("patient name"):index1[index1.index(s.find("patient name"))+1]]
    #d["patientname"]='Krishna'
    print(d)
    global u
    u=d["patientname"]
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%y,%H hrs %M min %S sec")
    d["pn"]=str(d["patientname"])+str(timestampStr)
    f=d["pn"]+".txt"
    r=d["pn"]+".wav"
    global path
    path="D:/audio/"+f
    path1="D:/audio/"+r
    f1=open(path,mode="w")

    f1.write(s)
    f1.close()

    with wave.open("recorded.wav", "rb") as wav_file:    
    
        n_channels = wav_file.getnchannels()      
        sample_width = wav_file.getsampwidth()    
        framerate = wav_file.getframerate()       
        n_frames = wav_file.getnframes()          
        comp_type = wav_file.getcomptype()        
        comp_name = wav_file.getcompname()        

    # Read audio data.
        frames = wav_file.readframes(n_frames)   
        assert len(frames) == sample_width * n_frames

    # Duplicate to a new WAV file.
    with wave.open(path1, "wb") as wav_file:    
    
        params = (n_channels, sample_width, framerate, n_frames, comp_type, comp_name)
        wav_file.setparams(params)
        wav_file.writeframes(frames) 
    return render(request,'voice_5.html',{'data':d})
def conti(request):
    d={}
    d["patientname"]=request.POST["patientname"]
    d["medicalhistory"]=request.POST["historyP"]
    #d["currentmedicalcondition"]=request.GET["currentmedicalcondition"]
    d["suggestions"]=request.POST["followadvice"]
    d["drugs"]=drago
    d["otherdrugs"]=request.POST["otherdrug"]
    d["othercomplaints"]=request.POST["othercomplaints"]
    d["familyhistory"]=request.POST["historyf"]
    d["temperature"]=request.POST["temperature"]
    d["pulse"]=request.POST["pulse"]
    d["hemoglobin"]=request.POST["hemoglobin"]
    #d["rbs"]=request.GET["rbs"]
    d["allergies"]=request.POST["present"]
    d["exercise"]=request.POST["rest"]
    d["labfindings"]=request.POST["investigation"]
    d["nextmeeting"]=request.POST["followupdate"]
    d["dietplan"]=request.POST["deit"]
    d["comments"]=request.POST["comments"]
    d["chiefcomplaints"]=request.POST["chiefcomplaints"]
    d["pasthistory"]=request.POST["history"]      
    return render(request,'voice_5.html',{'data':d})

def output1(request):
    d={}
    r = sr.Recognizer()
    s=" "
    #output(request)
   #d=dict()
    
    index1=[]
    index2=[]
    #s2=""
    s3=""
    s4=""
    k1=[]
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Please say something")
        # recognize speech using google
        while(True):
            try:
                audio = r.listen(source,timeout=5)
                s=s+' '+r.recognize_google(audio)
                with open("recorded.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                if 'stop' in s:
                    s=s.replace("stop","")
                    break
            except:
                break
    s=s.lower()
    print(s.lower())
    s4=s4+s
    print(s4.lower())
    
    s=s.replace("coma",",")
    s=s.replace("kama",",")
       
    
    for i in stri.l:
        k=s.find(i)
       # indices.append(k)
        index1.append(k)
    index1.append(len(s))
    index1.sort()
    f2=open(path,"a")
    f2.write(s)
    f2.close()
    f1=open(path,"r")
    s=" "
    for i in f1:
        s=s+i
    f1.close()
    d["patientname"]=u

    index1=[]


    for i in stri.l:
        k=s.find(i)
       # indices.append(k)
        index1.append(k)
    index1.append(len(s))
    index1.sort()
    for i in stri.l:
        k=s4.find(i)
        index2.append(k)
    index2.append(len(s4))
    index2.sort()
    if s.find("medical history")==-1:
        d["medicalhistory"]=''
    else:
        d["medicalhistory"]=s[s.find("medical history")+len("medical history"):index1[index1.index(s.find("medical history"))+1]]
    if s.find("current medical condition")==-1:
        d["current medical condition"]=''
    else:
        d["currentmedicalcondition"]=s[s.find("current medical condition")+len("current medical condition"):index1[index1.index(s.find("current medical condition"))+1]]
    if s.find("suggestions")==-1:
        d["suggestions"]=''
    else:
        d["suggestions"]=s[s.find("suggestions")+len("suggestions"):index1[index1.index(s.find("suggestions"))+1]]
    if s.find("drugs")==-1:
        d["drugs"]=''
    else:
        m=(s4[s4.find("drugs")+len("drugs"):index2[index2.index(s4.find("drugs"))+1]].lower())
        print(m)
        m=m.replace("coma",",")
        m=m.replace("kama",",")
        k1=m.split(",")
        print(m)
        g=0
        for i in k1:
            drago1=[]
            m1=re.findall(r"\d+",i.strip())
            res=list(map(int,m1))
            m2=re.search(r"\d",i.strip())
            if len(res)!=0:
                g=m2.start()
                if i[0:g].strip() in stri.l1:
                    drago1.append(i[0:g].strip())
                    for j in res:
                        print(j)
                        drago1.append(j)
                    print(drago1)
                    drago.append(drago1)
                else:
                    s3=s3+i.strip()+","
            else:
                if i.strip() in stri.l1:
                    #s2=s2+i.strip()+","
                    drago1.append(i.strip())
                    #drago.append(s2[:len(s2)-1])
                    drago.append(drago1)
                    #s2=" "
                else:
                    s3=s3+i.strip()+","
            
        d["drugs"]=drago
        d["otherdrugs"]=s3[:len(s3)-1]
    if s.find("other complaints")==-1:
        d["othercomplaints"]=''
    else:
        d["othercomplaints"]=s[s.find("other complaints")+len("other complaints"):index1[index1.index(s.find("other complaints"))+1]]
    if s.find("family history")==-1:
        d["familyhistory"]=''
    else:
        d["familyhistory"]=s[s.find("family history")+len("family history"):index1[index1.index(s.find("family history"))+1]]
    if s.find("temperature")==-1:
        d["temperature"]=''
    else:
        d["temperature"]=s[s.find("temperature")+len("temperature"):index1[index1.index(s.find("temperature"))+1]]+"??C"
    if s.find("pulse")==-1:
        d["pulse"]=''
    else:
        d["pulse"]=s[s.find("pulse")+len("pulse"):index1[index1.index(s.find("pulse"))+1]]
    if s.find("hemoglobin")==-1:
        d["hemoglobin"]=''
    else:
        d["hemoglobin"]=s[s.find("hemoglobin")+len("hemoglobin"):index1[index1.index(s.find("hemoglobin"))+1]]
    if s.find("RBS")==-1:
        d["rbs"]=''
    else:
        d["rbs"]=s[s.find("RBS")+len("RBS"):index1[index1.index(s.find("RBS"))+1]]
    if s.find("allergies")==-1:
        d["allergies"]=''
    else:
        d["allergies"]=s[s.find("allergies")+len("allergies"):index1[index1.index(s.find("allergies"))+1]]
    if s.find("exercise")==-1:
        d["exercise"]=''
    else:
        d["exercise"]=s[s.find("exercise")+len("exercise"):index1[index1.index(s.find("exercise"))+1]]
    if s.find("lab findings")==-1:
        d["labfindings"]=''
    else:
        d["labfindings"]=s[s.find("lab findings")+len("lab findings"):index1[index1.index(s.find("lab findings"))+1]]
    if s.find("next meeting")==-1:
        d["nextmeeting"]=''
    else:
        d["nextmeeting"]=s[s.find("next meeting")+len("next meeting"):index1[index1.index(s.find("next meeting"))+1]]
    if s.find("diet plan")==-1:
        d["dietplan"]=''
    else:
        d["dietplan"]=s[s.find("diet plan")+len("diet plan"):index1[index1.index(s.find("diet plan"))+1]]
    if s.find("comments")==-1:
        d["comments"]=''
    else:
        d["comments"]=s[s.find("comments")+len("comments"):index1[index1.index(s.find("comments"))+1]]
    if s.find("chief complaints")==-1:
        d["chiefcomplaints"]=''
    else:
        d["chiefcomplaints"]=s[s.find("chief complaints")+len("chief complaints"):index1[index1.index(s.find("chief complaints"))+1]]
    if s.find("past history")==-1:
        d["pasthistory"]=''
    else:
        d["pasthistory"]=s[s.find("past history")+len("past history"):index1[index1.index(s.find("past history"))+1]]
        
    print(d)
    return render(request,'voice_5.html',{'data':d})





