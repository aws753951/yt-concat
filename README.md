Youtube影片專案 
=====
### 專案目標:下載某一youtube頻道，並針對其影片有談到的關鍵字進行片段搜尋與整合單一影片<br>
流程如下<br> 
   ![image](https://user-images.githubusercontent.com/101057598/168748125-c9d9a191-f63b-4dfd-8d96-5ba733a345ce.png) <br> 
Step 1. 建立影片、字幕、最後產出等相關資料夾<br> 
Step 2. 取得該youtube頻道所有影片網址<br> 
Step 3. 建立YT物件，協助後續流程能夠拿取該物件的屬性使用<br> 
Step 4. 下載所有影片的字幕 <br>
Step 5. 讀取剛剛下載的字幕 → 避免重複使用YT-api，有quota限制<br> 
Step 6. 搜尋特殊關鍵字，此專案是以"comparison"為例，並把該'關鍵字的字幕'與對應的'時間'紀載於Found物件<br> 
Step 7. 下載所有影片<br> 
Step 8. 編輯影片(pip install moviepy)，針對剛剛紀載於Found物件的時間片段進行剪輯與產出<br> 
Step 9. 是否把素材(字幕/影片)刪掉<br> 
### 主要應用內容
運用 pipline，使每一個流程就像管線一樣接力，從頭一步一步到產出<br> 
繼承 Step，確保每個流程的架構統一<br> 
另設物件 YT(yt.py) 與 Found(found.py)，針對特定抓取的屬性附加在這些物件上，後續提取使用<br> 
使用 Utils物件，主要處理路徑以及確認檔案是否存在使用<br> 
### 附加應用內容
運用虛擬環境系統 venv ，確保該環境所需安專套件，可依requirements.txt達成<br> 
使用dotenv取得環境變數，並使用.gitignore避免敏感性文件上傳(api)<br> 
使用logging，可於檔案運行時Debug並存成紀錄<br> 
於main.py內建立投遞引數(python line arguments)，使使用者可於命令提示字元(cmd)運行主程式時可修改運行內容<br> 
https://www.tutorialspoint.com/python/python_command_line_arguments.htm <br> 
### 錯誤應用集
![image](https://user-images.githubusercontent.com/101057598/168755992-90979b3e-27db-4302-8c46-e447d8060730.png)<br> 
於step4 下載字幕時，由於youtube影片字幕已經改成自動產出，須於en改成a.en <br> 
![image](https://user-images.githubusercontent.com/101057598/168756336-5e2dd0a0-0e7b-4135-9762-89effc6e6014.png) <br> 
同樣於step4 下載字幕時，pytube相關原始碼尚未更新至最新youtube的字幕型態，需於原始碼內更改相關內容才能正常運行<br> 
https://github.com/pytube/pytube/issues/1085 <br> 
![image](https://user-images.githubusercontent.com/101057598/168757127-0e0ff642-2a47-48a4-9291-bcbac2a5f31a.png)<br> 
於step7 下載影片時，javascript更改其格式，須於pytube程式碼內更改<br>
https://github.com/pytube/pytube/issues/1281<br>
## 打包至pip install成為資源給他人使用，請參考packyt專案(由於當時我從python 3.8 至 python3.10，相關程式無法正常打包)
