<?php 
	session_start();
	if(!isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 0)){
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
		<?php include('nav_mem.php'); ?>
		</div>
	<div id= "container">
		<?php include('info-col.php'); ?>

		<div id= "content">
			<h2 id= "memberheader">Welcome to the Home Page! </h2>
			<p> <br><br>Neque nisl feugiat augue nullam venenatis cras quisque eget, 
			non erat facilisis at aenean imperdiet nunc enim vivamus volutpat facilisi rutrum placerat rhoncus dui. 
			Justo nam ac sem mauris maecenas turpis semper facilisi non vehicula, 
			fames pellentesque mus inceptos cum ultrices augue ad natoque hendrerit sollicitudin, 
			suspendisse cubilia interdum purus habitasse nulla nisi diam molestie.
			<br> </p>
			
			<img id= "memimg"src= "contentsample2.jpg">

			<p> <br><br>Neque nisl feugiat augue nullam venenatis cras quisque eget, 
			non erat facilisis at aenean imperdiet nunc enim, 
			vivamus volutpat facilisi rutrum placerat rhoncus dui. 
			Justo nam ac sem mauris maecenas turpis semper facilisi non vehicula, 
			fames pellentesque mus inceptos cum ultrices augue ad natoque hendrerit sollicitudin, 
			suspendisse cubilia interdum purus habitasse nulla nisi diam molestie. 
			Ac vivamus ornare orci leo at quisque ligula, 
			aptent posuere dapibus potenti nibh lacinia turpis, 
			ut luctus velit dignissim mauris curabitur. 
			Placerat congue maecenas neque nunc ligula iaculis tellus a rutrum,
			magnis tincidunt purus augue pretium est cubilia facilisis arcu, 
			habitant magna taciti sociis ut ullamcorper tempus rhoncus.
			<br><br> </p>

			<p> 
			Ac vivamus ornare orci leo at quisque ligula, 
			aptent posuere dapibus potenti nibh lacinia turpis, 
			ut luctus velit dignissim mauris curabitur. 
			Placerat congue maecenas neque nunc ligula iaculis tellus a rutrum,
			magnis tincidunt purus augue pretium est cubilia facilisis arcu, 
			habitant magna taciti sociis ut ullamcorper tempus rhoncus.
			<br><br> </p>
		</div>
	</div>
	<?php include('footer.php'); ?>
</body>
</html>