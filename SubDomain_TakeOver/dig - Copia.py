import socket
import dns.resolver
import requests
import csv
import concurrent.futures
import time



#===========PARTE 2: VERIFICA E SALVA OS CNAME=============
TimeOut = []

#Lê o TimeOut.csv
with open('Salvos/Status_Code/TimeOut.csv', 'r', encoding='utf-8') as f:
    reader2 = csv.reader(f)
    for row in reader2:
        TimeOut.append(row[0])

#Descobre e salva o CNAME
def extract(site2):
    try:

        #Descobre o CNAME
        for rdata in dns.resolver.resolve(site2, 'CNAME') :
            cnamee = (rdata.target)

            #Salva o CNAME
            with open('Salvos/CNAMES/Com CNAME.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(str(cnamee)+'      -    Origem =   '+site2+'\n')


    except:
        #Salva o CNAME
        with open('Salvos/CNAMES/Sem CNAME.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(str(site2)+'\n')

#Realiza o loop
with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, TimeOut) 


