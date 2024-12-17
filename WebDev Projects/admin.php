<?php 
	session_start();
	if(!isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 1)){
		header('Location: login.php');
		exit();
	}
?>

<!doctype html>
<html lang= "en">

<head>
	<title> Website ni Artuz </title>
	<meta charset = "utf-8">
	<link rel="stylesheet" type= "text/css" href = "stylesartuz.css">
</head>

<body>
	
	<div id= "topbar"> 
		<?php include('header.php'); ?>
		<?php include('nav_admin.php'); ?>
		</div>
	<div id= "container">
		<?php include('info-col-admin.php'); ?>

		<div id= "content">
			<h2 id = "adminheader">Welcome to the Admin's Page!</h2>
			<img id = "dashboard" src= "admindash.png">
		</div>
	</div>
	<?php include('footer.php'); ?>
</body>
</html>