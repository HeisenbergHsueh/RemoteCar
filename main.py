#導入RPi.GPIO的模組，此模組的用途是讓我們可以使用python的script來操作raspberry pi上的GPIO
import RPi.GPIO as GPIO
from time import sleep

#導入flask，flask為一個lightweight的web server
#使用flask製作操作車子的web UI，因而需要導入
#render_template會自動結合template資料夾底下的html檔，這樣在python的程式碼中
#可以用相當簡單的方式設定web的頁面
from flask import Flask, render_template

#Flask進行初始化，在此階段會建立起一個實例(instance)
#此實例會負責處理所有傳送給flask的請求
#在此實例中，只有一個必須指定的參數，這裡使用__name__系統變數
#此參數是為了清楚區分出flask是作為獨立web server運作、還是作為一個module運作
app = Flask(__name__)

#忽略GPIO所跳出的警告
GPIO.setwarnings(False)
#指定使用BCM編碼的模式
GPIO.setmode(GPIO.BCM)

#設定raspberry pi用來對LN298(馬達驅動模組)下達指定的GPIO接腳
#in1、in2為控制左邊輪子TT馬達的GPIO接腳
in1 = 18
in2 = 23
#in3、in4為控制右邊輪子TT馬達的GPIO接腳
in3 = 24
in4 = 25

#設定GPIO接腳為輸出的狀態，這樣子接下來才可以透過raspberry pi的GPIO接腳去控制LN298
#然後透過改變LN298的in1~in4的電壓高低狀態，進一步控制TT馬達的轉動
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
  
@app.route("/")
#定義route的參數傳遞，參數名為remote_param，設定傳遞參數後
#就可以從html傳遞參數python的腳本，如此一來，就可以透過web UI傳遞操作車子的指令
@app.route("/<remote_param>")

def main(remote_param=None):
    #設定一個變數status，之後會依據傳進來的參數，給予status不同的狀態
    #最後，status會一起return到前端web UI
    status = ""

    #LN298馬達運作說明
    #GPIO.output中，True為高電壓(HIGH)、False為低電壓(LOW)

    #以下分別為左馬達、右馬達的in1~in4接收到不同電壓時，馬達的狀態
    #左馬達(in1、in2)
    #順時針 : in1(HIGH)、in2(LOW)
    #逆時針 : in1(LOW)、in2(HIGH)
    #停止 : in1(LOW)、in2(LOW)
    #右馬達(in3、in4)
    #順時針 : in3(HIGH)、in4(LOW)
    #逆時針 : in3(LOW)、in4(HIGH)
    #停止 : in3(LOW)、in4(LOW)
    


    #前進 : 要讓兩個輪子都是"順時針"轉動
    #因此訊號的狀態為 : in1(HIGH)、in2(LOW)、in3(HIGH)、in4(LOW) 
    if remote_param == 'f':
        status = "前進"
        GPIO.output(in1, True)
        GPIO.output(in2, False)
        GPIO.output(in3, True)
        GPIO.output(in4, False)
    #後退 : 要讓兩個輪子都是"逆時針"轉動
    #因此訊號的狀態為 : in1(LOW)、in2(HIGH)、in3(LOW)、in4(HIGH)  
    if remote_param == 'b':
        status = "後退"
        GPIO.output(in1, False)
        GPIO.output(in2, True)
        GPIO.output(in3, False)
        GPIO.output(in4, True)
    #往右轉 : 僅讓左輪"順時針"轉動
    #因此訊號的狀態為 : in1(HIGH)、in2(LOW)、in3(LOW)、in4(LOW)
    if remote_param == 'r':
        status = "往右轉"
        GPIO.output(in1, True)
        GPIO.output(in2, False)
        GPIO.output(in3, False)
        GPIO.output(in4, False)
    #往左轉  : 僅讓右輪"順時針"轉動
    #因此訊號的狀態為 : in1(LOW)、in2(LOW)、in3(HIGH)、in4(LOW) 
    if remote_param == 'l':
        status = "往左轉"
        GPIO.output(in1, False)
        GPIO.output(in2, False)
        GPIO.output(in3, True)
        GPIO.output(in4, False)
    #停止 : 讓所有輪子的訊號都呈現低電壓
    #因此訊號的狀態為 : in1(LOW)、in2(LOW)、in3(LOW)、in4(LOW) 
    if remote_param == 's':
        status = "停止"
        GPIO.output(in1, False)
        GPIO.output(in2, False)
        GPIO.output(in3, False)
        GPIO.output(in4, False)	
    templateData = {
        'status' : status
    }
    #這邊預設會開啟template資料夾底下的mobile.html作為首頁
    return render_template('remote.html', **templateData)

#if __name__ == "__main__"指的是 : 
#這一個main.py的script是主要執行的程式，而非作為module時，才會執行
#執行之後，web server就建立起來，這邊使用的port是8080，也可以隨意修改成自己想要用的port
#之後只要打開瀏覽器輸入http://localhost:8080便會出現web頁面
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
