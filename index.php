<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <?php
        setcookie("afiliado","5323", (time() + (3 * 24 * 3600)));

        $afiliado = $_COOKIE["afiliado"];

        echo "adff: $afiliado";
    ?> 
</body>
</html>