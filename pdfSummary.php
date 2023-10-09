<?php
    ini_set('max_execution_time',0);

    $uniqPdfName = uniqid();
    $answer = "";
    $command = "";

    $fileDir = '/var/www/unj-labo/pdfs/';
    if(!move_uploaded_file($_FILES['pdfFile']['tmp_name'], $fileDir . $uniqPdfName.'.pdf')) {
        $answer = "failed";
        exit;
    }

    $filePath = "/var/www/unj-labo/";
    $pyPath = "myPdfSummary.py";
    $command = "python3 " . $filePath . $pyPath . " 2 " . $uniqPdfName;
    exec($command,$output,$retval);

    foreach ($output as $o) {
        $answer .= mb_convert_encoding($o, "UTF-8", "auto");
        $answer .= '<br>';
    }

    $pyPath = "MySQLHandler.py";
    $command = "python3 " . $filePath . $pyPath . " 1 " . $uniqPdfName;
    exec($command,$output);

    echo $answer;