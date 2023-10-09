<!DOCTYPE html>
    <html lang="ja">
        <head>
            <meta charset="utf-8">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
            <title>owari</title>
    </head>
<body>
    <form>
        <input type="text" id="question" name="question">
        <input type="button" value="submit" id="keySend">
    </form>
    <div id="return"></div>
    <form>
        <input name="pdfFile" type="file" />
        <input type="button" value="submit" id="pdfSubmit"/>
    </form>
    <div id="pdfreturn"></div>

    <div id='pdfQuestion'>
        <form>
            <p>内容についての質問ができます</p>
            <input type="text" name="pdfQ">
            <input type="button" id="pdfQuestionSubmit" value="submit">
        </form>
    </div>
    <script>
        document.getElementById("pdfQuestion").style.display = "none";
    </script>

    <script src="./notSync.js"></script>
</body>
</html>