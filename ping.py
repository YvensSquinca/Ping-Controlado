import subprocess
import time
import pymysql

while (True):
    conexao = pymysql.connect(host='seu host aqui', db='Nome do DB', user='Usuario', passwd='Senha', port=3306) #Porta 3306 é padrão, caso a sua seja especifica, Altere
    i = 0
    count = 0
    for i in range(0, 10):
        cursor = conexao.cursor()
        print (count)
        maquina = 'Hostname ou IP'
        print (maquina)
        def ping(host):

            import subprocess, platform

            ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
            args = "ping " + " " + ping_str + " " + host
            need_sh = False if  platform.system().lower()=="windows" else True

            return subprocess.call(args, shell=need_sh) == 0

        if ping(maquina) == True:
            print ('Ok')
            cursor.execute("Comando em SQL")
            conexao.commit()
        else:
            print ('falhou')
            cursor.execute("Comando em SQL")
            conexao.commit()
        count += 1
        time.sleep(1.0) #Tempo de pausa entre os Loops do FOR
        
    conexao.close()
    time.sleep(10.0) #Tempo de pausa entre os Loops do WHILE
