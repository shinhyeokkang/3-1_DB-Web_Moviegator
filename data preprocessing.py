# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:50:39 2019

@author: User
"""
import pandas as pd
import numpy as np

action=pd.read_csv("action_new.csv",encoding='utf-8')
adventure=pd.read_csv("adventure_new.csv",encoding='utf-8')
animation=pd.read_csv("animation_new.csv", encoding='utf-8')
Comedy=pd.read_csv("Comedy_new.csv", encoding='utf-8')
Crime=pd.read_csv("Crime_new.csv", encoding='utf-8')
#--------------------------------------------------------------------
#1차

Documentary=pd.read_csv("Documentary_new.csv",encoding='utf-8')
Drama=pd.read_csv("Drama_new.csv",encoding='utf-8')
Fantasy=pd.read_csv("Fantasy_new.csv",encoding='utf-8')
Horror=pd.read_csv("Horror_new.csv",encoding='utf-8')
Music=pd.read_csv("Music_new.csv",encoding='utf-8')
History=pd.read_csv("History_new.csv",encoding='utf-8')

#----------------------------------------------------------------------
#2차

Mystery=pd.read_csv("Mystery_new.csv",encoding='utf-8')
Romance=pd.read_csv("Romance_new.csv",encoding='utf-8')
Sci_Fi=pd.read_csv("Sci_Fi_new.csv",encoding='utf-8')
War=pd.read_csv("War_new.csv",encoding='utf-8')
Family=pd.read_csv("Family_new.csv",encoding='utf-8')


#--------------------------------------------------------------------
#3차
#합치기 모든 영화 테이블(이름 중복 영화 제거)

movie=pd.concat([action, adventure,animation, Comedy, Crime, Documentary, Drama, Fantasy, Horror, Music, History, Mystery, Romance, Sci_Fi, War, Family])
movie1= movie.drop_duplicates(['title'])
movie1.to_csv('movie_new.csv')




#배우--------------------------------------------------------------
celeb=pd.read_csv("celeb_after.csv",encoding='utf-8')

celeb
celeb_array[:,1]#배우이름
celeb_array[:,5]#배우에 따른 영화



act=[]
for i in range (len(celeb)):
    actor=celeb_array[i,1]
    movie=celeb_array[i,5]
    actor_movie=(actor,movie)
    act.append(actor_movie)
actor_movie1=pd.DataFrame(act)
b=a.tolist()
b.(\n,',')


import string
import math

#--------------------------------------------------------------------------
#sample 연습

action_nan=action.dropna(how="any") #nan없애기
list_l=[]
action_array=np.array(action_nan)#액션 배열화
for i in range(len(action_nan)):
    lis=[]
    movie_actor=[]
    movie_actor=action_array[i,2]
    
    if "|" in movie_actor :  #|를 가진 행만 추출해서 분
        mov=movie_actor.split("|")
        mov.pop(0) #director 없애기
        mov1=mov[0].replace('Stars:','')
        mov2=mov1.split(',')
        
        lis.append(action_array[i,1])
        for j in range(len(mov2)):
            lis.append(mov2[j])
        
        list_l.append(lis)
        
       
    else:
        mov=movie_actor
        mov1=mov.replace('Stars:','')
        mov2=mov1.split(',')
        lis.append(action_array[i,1])
        for j in range(len(mov2)):
            lis.append(mov2[j])
        
       
        list_l.append(lis)
    


list_l #영화+star
a=pd.DataFrame(list_l)
a.to_csv('seifjs.csv')

action_frame=pd.DataFrame(list_l)    
a=np.array(action_frame)
action_frame.to_excel('sample.xlsx')

import openpyxl as op
wb=op.worksheet

#----------------------------------------------------------------------
#영화 배우랑전처리
def cutchar(file):
    
    movie_nan=file.dropna(how="any") #nan없애기
    list_l=[]
    movie_array=np.array(movie_nan)#액션 배열화
    for i in range(len(movie_nan)):
        lis=[]
        movie_actor=[]
        movie_actor=movie_array[i,3]
        
        lis.append(movie_array[i,1])
        movie_year=[]
        movie_year=movie_array[i,2]
        
        if "–" in movie_year:
            mov=movie_year.split("–")
            
            mov1=mov[0].replace('(','')
            mov2=mov1.replace(')','')
            mov3=mov2.replace('I','')
            mov4=mov3.replace('Video','')
            mov5=mov4.replace('Game','')
            mov6=mov5.replace('TV','')
            mov7=mov6.replace('V','')
            mov8=mov7.replace('Short','')
            mov9=mov8.replace('Movie','')
            mov10=mov9.replace('Special','')
            mov11=mov10.replace('X','')
            if len(mov11)<3:
                lis.append(0)
            else:    
                lis.append(mov11)
        else:
            mov=movie_year
            mov1=mov.replace('(','')
            mov2=mov1.replace(')','')
            mov3=mov2.replace('I','')
            mov4=mov3.replace('Video','')
            mov5=mov4.replace('Game','')
            mov6=mov5.replace('TV','')
            mov7=mov6.replace('V','')
            mov8=mov7.replace('Short','')
            mov9=mov8.replace('Movie','')
            mov10=mov9.replace('Special','')
            mov11=mov10.replace('X','')
            if len(mov11)<3:
                lis.append(0)
            else:    
                lis.append(mov11)

        
        if "|" in movie_actor :  #|를 가진 행만 추출해서 분
            mov=movie_actor.split("|")
            mov.pop(0) #director 없애기
            mov1=mov[0].replace('Stars:','')
            mov2=mov1.replace('Star:','')
            mov3=mov2.split(',')
            
            for j in range(len(mov3)):
                lis.append(mov3[j])
            
        else:
            mov=movie_actor
            mov1=mov.replace('Directors:','')
            mov2=mov1.replace('Director:','')
            
                
            mov3=mov2.replace('Stars:','')
            mov4=mov3.replace('Star:','')
            mov5=mov4.split(',')
            
            for j in range(len(mov5)):
                lis.append(mov5[j])
            
        list_l.append(lis)
        
    return list_l


#-------------------------------------------------------------------------
#이름만 바꿔서 엑셀 파일 반환
file_after= cutchar(animation)
file_after= pd.DataFrame(file_after)
for i in range(6,8):
    file_after=file_after.drop(columns=[i], axis=1)
file_after.columns=['title','releasedate','actor1','actor2','actor3','actor4']
file_after.to_csv("animation_new.csv")

#-----------------------------------------------------------------------
#합치기
#배우
action_actor=pd.read_csv("action_actor.csv",encoding='utf-8')
adventure_actor=pd.read_csv("adventure_actor.csv",encoding='utf-8')
animation_actor=pd.read_csv("animation_actor.csv",encoding='utf-8')
Comedy_actor=pd.read_csv("Comedy_actor.csv",encoding='utf-8')
Crime_actor=pd.read_csv("Crime_actor.csv",encoding='utf-8')
Documentary_actor=pd.read_csv("Documentary_actor.csv",encoding='utf-8')
Drama_actor=pd.read_csv("Drama_actor.csv",encoding='utf-8')
Fantasy_actor=pd.read_csv("Fantasy_actor.csv",encoding='utf-8')
History_actor=pd.read_csv("History_actor.csv",encoding='utf-8')
Horror_actor=pd.read_csv("Horror_actor.csv",encoding='utf-8')
Music_actor=pd.read_csv("Music_actor.csv",encoding='utf-8')
Mystery_actor=pd.read_csv("Mystery_actor.csv",encoding='utf-8')
Romance_actor=pd.read_csv("Romance_actor.csv",encoding='utf-8')
Sci_Fi_actor=pd.read_csv("Sci_Fi_actor.csv",encoding='utf-8')
War_actor=pd.read_csv("War_actor.csv",encoding='utf-8')
Family_actor = pd.read_csv("Family_actor.csv",encoding='utf-8')
#연도
action_year=pd.read_csv("action_year.csv",encoding='utf-8')
adventure_year=pd.read_csv("adventure_year.csv",encoding='utf-8')
animation_year=pd.read_csv("animation_year.csv",encoding='utf-8')
Comedy_year=pd.read_csv("Comedy_year.csv",encoding='utf-8')
Crime_year=pd.read_csv("Crime_year.csv",encoding='utf-8')
Documentary_year=pd.read_csv("Documentary_year.csv",encoding='utf-8')
Drama_year=pd.read_csv("Drama_year.csv",encoding='utf-8')
Fantasy_year=pd.read_csv("Fantasy_year.csv",encoding='utf-8')
History_year=pd.read_csv("History_year.csv",encoding='utf-8')
Horror_year=pd.read_csv("Horror_year.csv",encoding='utf-8')
Music_year=pd.read_csv("Music_year.csv",encoding='utf-8')
Mystery_year=pd.read_csv("Mystery_year.csv",encoding='utf-8')
Romance_year=pd.read_csv("Romance_year.csv",encoding='utf-8')
Sci_Fi_year=pd.read_csv("Sci_Fi_year.csv",encoding='utf-8')
War_year=pd.read_csv("War_year.csv",encoding='utf-8')
Family_year = pd.read_csv("Family_year.csv",encoding='utf-8')
#합친것




def sumfile(file, file1):
    fil1=np.array(file)
    fil2=np.array(file1)
    list_l=[]
    for i in range(len(fil1)):
        lis=[]
        lis.append(fil1[i,1])
        lis.append(fil1[i,2])
        lis.append(fil2[i,2])
        lis.append(fil2[i,3])
        lis.append(fil2[i,4])
        lis.append(fil2[i,5])
        list_l.append(lis)
    
    after_file = pd.DataFrame(list_l)
    return after_file

file_after=sumfile(Family_year,Family_actor)
file_after.to_csv('Family.csv',encoding='utf-8')







#-------------------------------------------------------------------------
# 연도 전처리(널값인거 지우고, 숫자만 남게함)
list_l=[]
def transyear(file):
    movie_nan=file.dropna(how="any") #nan없애기
    list_l=[]
    movie_array=np.array(movie_nan)#액션 배열화
    for i in range(len(movie_array)):
        lis=[]
        movie_year=[]
        movie_year=movie_array[i,2]
        if "–" in movie_year:
            mov=movie_year.split("–")
            
            mov1=mov[0].replace('(','')
            mov2=mov1.replace(')','')
            mov3=mov2.replace('I','')
            mov4=mov3.replace('Video','')
            mov5=mov4.replace('Game','')
            mov6=mov5.replace('TV','')
            mov7=mov6.replace('V','')
            mov8=mov7.replace('Short','')
            mov9=mov8.replace('Movie','')
            mov10=mov9.replace('Special','')
            mov11=mov10.replace('X','')
            if len(mov11)<3:
                lis=[movie_array[i,1],None]
            else:    
                lis=[movie_array[i,1],mov11]
            
            list_l.append(lis)
        else:
            mov=movie_year
            mov1=mov.replace('(','')
            mov2=mov1.replace(')','')
            mov3=mov2.replace('I','')
            mov4=mov3.replace('Video','')
            mov5=mov4.replace('Game','')
            mov6=mov5.replace('TV','')
            mov7=mov6.replace('V','')
            mov8=mov7.replace('Short','')
            mov9=mov8.replace('Movie','')
            mov10=mov9.replace('Special','')
            mov11=mov10.replace('X','')
            if len(mov11)<3:
                lis=[movie_array[i,1],None]
            else:    
                lis=[movie_array[i,1],mov11]
            list_l.append(lis)
       
        
    return list_l
#--------------------------------------------------------------------
#연도 전처리 실행
file_year = transyear(Family)
file_year=pd.DataFrame(file_year)
file_year = file_year.dropna(how = "any")
file_year.columns=['title', 'release_date']
file_year.to_csv('Family_year.csv')

#----------------------------------------------------------------------

#셀럽 전처리 (null값 없음)
celeb=celeb.drop(columns=['movies'], axis=1)
celeb_array = np.array(celeb)
celeb_array[:,3]#생년월일
celeb_array[:,4] #키

#생년월일

list_l=[]
for i in range(len(celeb_array)):
    lis=[]
    name = celeb_array[i,1]
    role = celeb_array[i,2]
    birth=celeb_array[i,3]
    height = celeb_array[i,4]
    lis.append(name)
    lis.append(role)
    if "-" in birth:
        bir=birth.split("-")
        bir1=bir.pop(0)
        bir2=bir.pop(0)
        lis.append(bir1)
        lis.append(bir2)
    else:
        lis.append(None)
        lis.append(None)
    
    hei=height.split('(')
    hei.pop(0)
    hei1=hei[0].replace("'",'')
    hei2=hei1.replace(')','')    
    hei3=hei2.replace('m','')    
    hei4=float(hei3)*100
    hei5=int(hei4)
    lis.append(hei5)
    list_l.append(lis)

#------------------------------------------------------------------------
# 셀럽 남배우 여배우만 남기기
  
celeb_after=pd.DataFrame(list_l)
caa = np.array(celeb_after)
for i in range(len(caa)):
    rol=caa[i,1]
    if "Actor" in rol:
        caa1=caa[i,1].replace("Actor","male")
        caa[i,1]=caa1
    elif "Actress" in rol:
        caa1=caa[i,1].replace("Actress","female")
        caa[i,1]=caa1
    else:
        caa[i,1]=None
        
        
        
        
        
#------------------------------------------------------------------------
# 셀럽 이름 분할
ce_only=pd.DataFrame(caa)
ce_only=ce_only.dropna(how="any")
ce_only.columns=['actor_name','gender','birth_year','birth_month','height']
ce_only1=np.array(ce_only)
ce_only1[0,0]

list_l=[]
for i in range(len(ce_only1)):
    lis=[]
    name= ce_only1[i,0]
    name=name.split(" ")
   
    if len(name)==2:  
        name1=name[0]
        name2=name[1]
        lis.append(name1)
        lis.append(name2)
    else:
        name1=name[0]
        lis.append(name1)
        lis.append(name1)
    lis.append(ce_only1[i,1])
    lis.append(ce_only1[i,2])
    lis.append(ce_only1[i,3])
    lis.append(ce_only1[i,4])
    list_l.append(lis)
    
#------------------------------------------------------------------------
#셀럽 파일화

ce_only2=pd.DataFrame(list_l)
ce_only2.columns=['actor_lastname','actor_firstname','gender','birth_year','birth_month','height']
ce_only2.to_csv('celeb_after.csv')

#-------------------------------------------------------------------------    

a=[]
for i in range(1,500):
    
        
    b=[0]
    a.append(b)
c= np.array(a)
    

celeb=np.array(celeb)
celeb[:,1]    

cele1=[]
for i in range(len(celeb)):
    cele = celeb[i,1]
    cele.replace(" ",'')
    cele1.append(cele)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














