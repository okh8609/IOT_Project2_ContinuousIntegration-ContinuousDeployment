# IOT_Project2
## Continuous Integration & Continuous Deployment

本專案使用 Jenkins 他配 ansible 來佈署程式到 Raspberry Pi  
系統架構圖如下圖所示：  
![](https://i.imgur.com/J1PDc0H.png)
![](https://i.imgur.com/et74sK5.png)  



Jenkins會接收到Github的webhook的呼叫  
並透過 ansible 來進行一連串的佈署  
webhook的設定方式可參考我的[部落格文章](https://blog.khaos.tw/2021/04/jenkins-github.html)  
https://blog.khaos.tw/2021/04/jenkins-github.html  

主機名單的註冊與維護 [可以參考另外一個repository](https://github.com/okh8609/IOT_Project2_DeviceDeploymentAndConfigurationManagement)  
https://github.com/okh8609/IOT_Project2_DeviceDeploymentAndConfigurationManagement

執行畫面如下圖所示：  
![](https://i.imgur.com/agL66rV.png)  
