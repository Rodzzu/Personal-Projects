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
	<title> Registered Users Page </title>
	<meta charset = "utf-8">
	<link rel="stylesheet" type= "text/css" href = "stylesartuz.css">
</head>

<body>
	<div id= "topbar"> 
		<?php include('header.php'); ?>
		<?php include('nav_admin.php'); ?>
		</div>
	<div id= "container">
		<?php include('info-col.php'); ?>

		<div id= "content"> 
			<h2> Registered Users </h2>

			<p>
				<?php
				require('mysqli_connect.php');
				//fetch data through query
				$q = "SELECT user_id, lname, fname, email, DATE_FORMAT(registration_date, '%M %d, %Y' ) as regdate 
				FROM users ORDER BY registration_date ASC";
				$result = @mysqli_query($dbcon, $q);

				if($result){ //if fetching is successful
					echo '<table>
					<tr class= "column_head">
					<td class= "column1"> Name </td>
					<td class= "column2"> Email </td>
					<td class= "column3"> Registration Date </td>
					<td class= "column4" colspan = 2> Actions </td>
					</tr>';

					while($row = mysqli_fetch_array ($result, MYSQLI_ASSOC)){

						echo '<tr>
						<td class= "rows"> ' .$row['lname']. ', '.$row['fname']. '</td> 
						<td class= "rows"> ' .$row['email']. '</td> 
						<td class= "rows"> ' .$row['regdate']. '</td>
						<td><a class = "edit" href = "edit_user.php?id='.$row['user_id'].'">Edit</a></td>	
						<td><a class = "delete" href="delete_user.php?id='.$row['user_id'].'">Delete</a></td>
						</tr>';

					} echo '</table>';
					 mysqli_free_result($result);

				} else { //not successful
					echo '<p class="error"> The current users cannot be retrieved due to system error, 
					please report this error to the system admin. Error Code: 123.</p>'; //error code is just an example
				} 
				mysqli_close($dbcon);
				?>
			</p>
		</div>
	</div>
	<?php include('footer.php'); ?>
</body>
</html>