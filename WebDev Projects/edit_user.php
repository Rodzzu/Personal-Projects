<?php 
	session_start();
	if(isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 1)){
		header('Location: login.php');
		exit();
	}
?>

<!doctype html>
<html lang= "en">

<head>
	<title> Edit User Info </title>
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
			<h2>Edit User Record</h2>
			<?php 
			if ((isset($_GET['id'])) && (is_numeric($_GET['id']))) { //checking for valid ID
                $id = $_GET['id'];
            } elseif ((isset($_POST['id']) && (is_numeric($_POST['id'])))) {
                $id = $_POST['id'];
            } else { //no id found, bye
                echo '<p class="error">This page has been accessed by mistake.</p>';
                include('footer.php');
                exit();
            }
			require('mysqli_connect.php');
			if ($_SERVER['REQUEST_METHOD'] == 'POST'){
				$errors = array();
				//check if first name, last name, and email has content
				//textbox
				if(empty($_POST['fname'])){
					$errors[] = "Please input your first name.";
				}
				else{
					$fn = trim($_POST['fname']);
				}
				
				if(empty($_POST['lname'])){
					$errors[] = "Please input your last name.";
				}
				else{
					$ln = trim($_POST['lname']);
				}
				
				if(empty($_POST['email'])){
					$errors[] = "Please input your email address.";
				}
				else{
					$e = trim($_POST['email']);
				}

				if(empty($errors)){
					$q =  "UPDATE users SET fname = '$fn', lname = '$ln', email = '$e' WHERE user_id = '$id' LIMIT 1";
					$result = @mysqli_query($dbcon, $q);
					if(mysqli_affected_rows($dbcon) == 1){
						echo '<h4>The user was edited successfully.</h4>';
					} else { //edit not successful
						echo '<h4>The user could not be edited due to a system error.</h4>';
						echo '<p>'.mysqli_error($dbcon).'</p>';
					}
				} else {
					//display content of error
					echo '<h2>Error!</h2>
					<p class="error"> The following error(s) occured: <br/>';
					foreach($errors as $msg){
						echo " - $msg<br/>\n";
					}
					echo '<p>Please try again.</p>';
				}

			}
			$q = "SELECT fname, lname, email FROM users WHERE user_id = '$id'";
			$result = @mysqli_query($dbcon, $q);
			if(mysqli_num_rows($result) == 1) { //valid user id
				$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
				//create the form
				echo '
				<form action = "edit_user.php" method = "post">

				<p> <label class= "label" for="fname"> First Name: <br/></label>
				<input type= "text" id="fname" name = "fname" placeholder= "Enter First Name" size = "35" maxlength="40" 
				value= "'.$row['fname'].'"></input>
				</p>
				
				<p> <label class= "label" for="lname"> Last Name: <br/></label>
				<input type= "text" id="lname" placeholder= "Enter Last Name" name= "lname" size = "35" maxlength="40" 
				value= "'.$row['lname'].'"></input>
				</p>
				
				<p> <label class= "label" for="email"> Email Address: <br/></label>
				<input type= "text" id="email" placeholder= "Enter Email Address" name= "email" size = "35" maxlength="50" 
				value= "'.$row['email'].'"></input>
				</p>

				<p>
				<input type="submit" id="editbtn" name= "submit" value= "Edit"></input>
				</p>

				<p>
				<input type = "hidden" name = "id" value = "'.$id.'">
				</p>

				</form>
				';
			} else{
				echo '<h4>You are not in the database. Would you like to <a href= "register.php">register</a>?</h4>';
				//link to register
			}
			mysqli_close($dbcon);
			?>
		</div>
	</div>
	<?php include('footer.php'); ?>
</body>
</html>