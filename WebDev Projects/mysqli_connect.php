<?php
$dbcon = @mysqli_connect('localhost', 'rodneyartuz', 'rodneyartuz', 'members_artuz')
OR die('Could not connect to mySQL, Error in '. mysqli_connect_error());
mysqli_set_charset ($dbcon, 'utf8');