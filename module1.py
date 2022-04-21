from bottle import post, request
from bottle import post, request
import re #импорт модуля, который обеспечивает поддержку регулярные выражения
import pdb
import json
sample = r'[A-Za-z0-9]+[A-Za-z0-9._%-]+[A-Za-z0-9]+@[A-Za-z0-9.-]+[A-Za-z0-9]+\.[a-z]{2,3}' #регулярное выражение
#функция для проверки соответсвия строки регулярному выражению

#dictionary[mail]=[]
f=0  
def check(mail):
   if (re.fullmatch(sample, mail)): #fullmatch  - полностью вся входящая строка (findall, sub, finditer, etc.)
       return True
   else:
       return False
@post('/ind', method='post')#обработка POST-запроса
#функция обработки строк
def module1():
    #получение введенных строк
    mail = request.forms.get('ADRESS')
    question=request.forms.get('QUEST')
    dictionary={} #словарь
    #если оба пустые
    if question=="" and  mail =="":
        return "Please enter the question and your mail!" 
    elif question=="" and mail!="":
        return "Please enter the question!" 
    elif mail =="" and   question!="":
        return "Please enter the e-mail !"
    else:
        if check(mail):
            try:
                with open('QUE.txt') as json_file:
                    dictionary = json.load(json_file) #считываю словарь  
            except:
                #обработка ошибки если файл json пуст
                pass    

            if len(dictionary)==0: # в словаре ничего нет записываем ключ-значение
                dictionary[mail]=[]
                dictionary[mail].append(question)
            else:
                for key in  dictionary.keys():
                    #print(key)
                    if mail==key:#если найден ключ добавляется значение в массив
                        f=0
                        dictionary[mail].append(question)
                        #print("tcnm")
                        break
                    else:
                        f=1
                if f: #если ключа не было в файле
                    dictionary[mail]=[]
                    dictionary[mail].append(question) 
            with open('QUE.txt', 'w') as outfile:#открытие файла
                json.dump(dictionary, outfile)#запись в файл indent для более удобеого чтения записей
            return "Thank you! The answer will be sent to the mail %s" % mail
        else:
            return "Your mail is invalid! Try it again"



