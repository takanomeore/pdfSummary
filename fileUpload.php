<?php
    function uploadPDF() {
        $fileDir = './pdfs/';
        if(move_uploaded_file($_FILES['pdfFile']['tmp_name'], $fileDir . $_FILES['pdfFile']['name'])) {
            echo '<script>alert("upload succeed");</script>';
        } else {
            echo '<script>alert("upload failed");</script>';
        }
    }
?>