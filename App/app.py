# TODO : Clean var ; rem cache
import sms_query as sms
import retreiveData as rd
import time,pickle
from flask import Flask, jsonify,redirect, url_for, request
import json,re
import urllib

app = Flask(__name__)

'''

ADD TEMPLATE : 

'''

@app.route('/',methods = ['POST', 'GET'])
def query():
    if request.method == 'POST':
        data = request.get_data()
        result = data.decode("utf-8")
        result = result[:result.index("inNumber")-1]
        sender,message = result[:result.index('&')],result[result.index('&')+1:]
        sender = sender.split("=")[1]
        message = message.split("=")[1]
        lines = message.split("%0A")
        sentence = []
        for i in lines:
            sentence += i.split("%20")
        print(sender)
        print(" ".join(sentence))

        return "HIPOST"
    else:
        data = request.data
        print(data)
        return "HIGET123"

    previous = ""
    file = open("./pinToLocMap.pickle","rb")
    placename = pickle.load(file)
    file.close()
    #print(response.json())
    #ans,number = sms.response()
    #ans = sms.response()
    # number = str(number)[2:]
    # temp = sms.get_context(ans)
    flag = -1 
    # if temp[-1]==0:
    #     #sms.sendSMS(number,temp[0])
    #     print("SENT :",temp[0])
    #     print("*"*80)
    #     response =  [number,temp[0]]
    #     flag = 0 
    # else:
    #     flag = temp[-1]
    #     response = temp[:-1] 
    # if flag == 2:
    #     data = rd.google_directions(response[0],response[1],response[2])
    #     # sms.sendSMS(number,data)
    #     print("SENT :",data)
    #     print("*"*80)
    # elif flag == 3:
    #     data = rd.process_detail(response[0])
    #     # sms.sendSMS(number,"ADDRESS: \n"+data)
    #     print("SENT :",data)
    #     print("*"*80)
    # elif flag:
    #     pincode = response[0]
    #     query = response[1]
    #     contact = number
    #     # pin code conv .
    #     data = rd.retreive_area(placename[str(pincode)],query)
    #     if len(data) == 1:
    #         # sms.sendSMS(number,data)
    #         print("SENT :",data)
    #         print("*"*80)
    #     elif data != None:
    #         if data[1]!=None:
    #             data = data[0]+"\n"+data[1]+"\n"+data[2]
    #         else:
    #             data = data[0]+"\n"+data[2]
    #         print("SENT :",data)
    #         print("*"*80)
    #         # sms.sendSMS(number,data)
    # print(data)
    print("Message Sent : app.py")
    #return "Hello world", 200


if __name__ == "__main__":
    app.run(debug=True,port=8080)
    #print(query())