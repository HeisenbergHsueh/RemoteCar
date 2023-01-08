## 111中央大學-大數據與物聯網-期末專題

***

<br>

### 專題緣由

***

本學期所上的大數據與物聯網的課程，是我人生中第一次接觸到與IoT有關的課程，因此想利用上課所學到的相關知識，實作一台遙控車，藉由實作一台遙控車來檢驗自己所學成果，謝謝。

<br>

### 專題材料

***

* Raspberry Pi 4 Model B * 1
* 電池盒3號6槽 * 1

<img src="https://i.imgur.com/Yb20w8s.png" width="200" height="150">

* 行動電源 * 1

<img src="https://i.imgur.com/xoxhy9T.png" width="200" height="150">

* 馬達驅動模組(L298N) * 1

<img src="https://i.imgur.com/K8qU8eZ.png" width="200" height="150">

* 3號1.5V電池 * 6
* 單芯線 * 4(連接TT馬達與L298N)

<img src="https://i.imgur.com/o8jvHdQ.png" width="200" height="150">

* 杜邦線母對母 * 4(連接L298N與樹莓派GPIO腳位)
* 杜邦線公對母 * 1(連接L298N與樹莓派GPIO腳位)
* Type C to USB 傳輸線 * 1
* 泡棉雙面膠

<img src="https://i.imgur.com/vUVuxx5.png" width="200" height="150">

* 車子材料(底盤 * 1、輪子 * 3)

<img src="https://i.imgur.com/9YUyAbU.png" width="200" height="150">

* TT馬達 * 2

<img src="https://i.imgur.com/1784ToM.png" width="200" height="150">

### 硬體架構說明

***

<img src="https://i.imgur.com/N54xY2X.jpg" width="450" height="300">

<img src="https://i.imgur.com/OdopWSy.jpg" width="450" height="150">

<img src="https://i.imgur.com/ovrTALq.jpg" width="450" height="300">

<img src="https://i.imgur.com/te56vBB.jpg" width="450" height="300">

<br>

### 軟體架構說明

***

#### 使用的語言&框架&模組

* python

* HTML

* jQuery mobile

* flask

#### 說明

* 使用python & flask 實作車子的remote control action & lightweight的web server，動作包含前進、後退、左轉、右轉、停止等5個action，程式碼請參閱github中main.py檔案

* 使用HTML & jQuery mobile 實作remote control的UI，如此一來便可以透過網頁上的UI來操作車子，程式碼請github中template資料夾底下的remote.html

#### 操作流程

1. 將main.py & template資料夾 & template資料夾內的remote.html放到樹梅派上，如下圖

<img src="https://i.imgur.com/B8Z7bu0.png" width="450" height="300">

2. 接著打開Thonny Python IDE，如下圖

<img src="https://i.imgur.com/5565AVB.png" width="300" height="300">

3. 打開main.py，並按下[Run]的按鈕，接著底下的訊息視窗會出現Serving flask app的字樣......結尾會是Debugger......，出現這一段訊息表示flask web server已經開始運行，如下圖

<img src="https://i.imgur.com/mao79UK.png" width="450" height="300">

4. 接著打開瀏覽器，輸入http://localhost:8080，就會看見remote UI，如下圖

<img src="https://i.imgur.com/GmsGbKU.png" width="450" height="200">

5. 接著確認硬體-L298N的驅動馬達模組是否有亮燈，有亮燈表示有過電，這樣子透過網頁下指令，車子才會動，如下圖

<img src="https://i.imgur.com/0Xhyhol.jpg" width="450" height="200">

6. 到此就完成了Remote Car的整體架設，謝謝

### 影片連結

***

[Remote Car範例展示](https://www.youtube.com/watch?v=xm3B2NemXxk)

<br>

### 可以改進的地方

***

* 可進一步結合超音波感測器做避障車

* 可進一步結合openCV做AI循線車

* 電池模組可以改用18650電池 * 2 + 18650電池盒，這樣可以節省更多空間

* 行動電源可改用raspberry pi專用的行動電源模組，這樣可以節省更多空間

<br>

### 參考資料

***

* [Physical Computing with Python - Using motors](https://projects.raspberrypi.org/en/projects/physical-computing/14)

* [Raspberry Pi How to Control a DC Motor With an L298N Driver](https://www.youtube.com/watch?v=2bganVdLg5Q)

* [Donkey car Assembly tutorial](https://www.youtube.com/watch?v=dcordkDSs80)

* [傑森創工智慧車底盤組裝教學](http://jmaker.banner.tw/doc/car_info.pdf)





