import pyautogui
import time
import os
#print('Press Ctrl-C to quit.')
#x, y = pyautogui.position()
#positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#print(positionStr, end='')

def FechaQV():
    time.sleep(10)
    os.system("taskkill /im Qv.exe")
    time.sleep(5)
    

def StartQV():
    os.system("start /MAX qv.exe")
    time.sleep(5)
    # Clique de abertura (tela verde) 
    pyautogui.click(637, 338, button='left')

def OpenFile(NomeArquivo):
    os.system(NomeArquivo)



################## FECHA QV ##########################
FechaQV()
######################################################

######################################################
######################################################

StartQV()
os.system("b:\extracao\extracao_dre.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(100)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################

StartQV()
os.system("b:\extracao\extracao_benner.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(600)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################



######################################################
######################################################
StartQV()
os.system("b:\lazer\Vendas.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(60)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\corporativo\Vendas_corporativo.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(60)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\conselho\Vendas.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\ComerciaL\Bi_reemissao.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(60)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Financeiro\Projetos.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(100)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################
StartQV()
os.system("b:\Eventos\Projetos_sao.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################
StartQV()
os.system("b:\Eventos\Projetos_for.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################
StartQV()
os.system("b:\Eventos\Projetos_rec.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Corporativo\Projetos_lazer.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(30)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################



######################################################
######################################################
StartQV()
os.system("b:\Financeiro\Orcamento_gerencial.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(100)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Financeiro\CRE\Clientes_em_aberto.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Financeiro\conferencia_terrestre.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################
StartQV()
os.system("b:\Financeiro\CRE\Clientes_bloqueados.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Financeiro\CRE\Clientes_baixados_em_Advogado.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################


######################################################
######################################################
StartQV()
os.system("b:\Conselho\clientes_bloqueados.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################

######################################################
######################################################
StartQV()
os.system("B:\Gestão Fornecedores\gestão_fornecedores.qvw")
time.sleep(20)
pyautogui.click(162, 59, button='left')
time.sleep(80)
pyautogui.click(86, 59, button='left')
FechaQV()
######################################################
######################################################