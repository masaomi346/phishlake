<?php
function listFolderFiles($dir){
  $ffs = scandir($dir);

  unset($ffs[array_search('.', $ffs, true)]);
  unset($ffs[array_search('..', $ffs, true)]);

  if (count($ffs) < 1)
      return;

  echo '<ol>';
  foreach($ffs as $ff){
      echo '<li>';
      if (is_dir($dir.'/'.$ff)) {
        $path = $dir.'/'.$ff;
        echo '<a href="'.$path.'">'.$ff.'</li>';
        listFolderFiles($path);
      } else{
        $path = $dir;
        echo '<a href="'.$path.'/'.$ff.'">'.$ff.'</li>';
      } 
  }
  echo '</ol>';
}
?>

<!DOCTYPE html>
<html lang="en">

<style>
p {
  font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif;
}
title {
  font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif;
}
h1 {
  font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif;
}
li {
  font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif;
}
</style>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome!</title>
</head>

<body>
  <p align="center">
    <img align="center" src="./logo.png" />
  </p>

  <h1 align="center">Howdy! 🤠</h1>
  <p align="center">
    Welcome to PhishPond.
    <br>
    If you can see this message, it means you're up and running! Yeehaw!
    <br>
  </p>

  <p>
  <?php
  listFolderFiles('.')
  ?>
  </p>
</body>

</html>