<?php
    //$question = json_decode($_POST['data']);
    ini_set('max_execution_time',0);
    $UserQ = $_POST['data'];
    $filePath = "./myPdfSummary.py";
    $command = "python3 ".$filePath ." 1 ".$UserQ;
    exec($command,$output,$retval);

    $answer = "";
    foreach ($output as $o) {
        $answer .= mb_convert_encoding($o, "UTF-8", "auto");
        $answer .= '<br>';
    }
    echo $answer;