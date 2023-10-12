# ChatGPTのAPIを使用してPDFの要約をするWebアプリ  
SiteURL:https://unj-labo.com  

## 各ファイル説明  
MySQLHandler.py:SQL操作　一時ファイルの日付管理など  
README.md:this file  
README.pdf:利用法、実行環境などを記載  
index.php:ホームページ  
myPdfSummary.py:PDF要約処理  
notSync.js:jQueryを用いた非同期処理  
notSyncphp.php:ChatGPT-APIの呼び出し  
pdfSummary.php:アップされたファイルを移動、myPdfSummary.pyの呼び出し  
settings.py:環境変数取得  
