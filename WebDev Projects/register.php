<!doctype html>
<html lang= "en">

<head>
	<title> Website ni Artuz </title>
	<meta charset = "utf-8">
	<link rel="stylesheet" type= "text/css" href = "stylesartuz.css">
	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
</head>

<body>
	<div id= "topbar"> 
		<?php include('header.php'); ?>
		<?php include('nav_reg.php'); ?>
		</div>
	<div id= "container2">
		<div id= "content3">
		<div id= "errors">
		<?php
			if($_SERVER['REQUEST_METHOD'] == 'POST'){
				//error array to store all the errors
				$errors = array();
				//may nilagay ba na first name?
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
				
				//check if last name and email is empty
				//parehas lang ba ung password at repeat password?
				if(!empty($_POST['psword1'])){
					if($_POST['psword1'] != $_POST['psword2']){
						$errors[] = "Your passwords do not match.";
					} 
					else{
						$p = trim($_POST['psword1']);
					}
				
				} else{
					$errors[] = "Please input your password.";
				}
				//all fields are successful
				if(empty($errors)){
					require('mysqli_connect.php');
					$hashedPassword = hash('sha256', $p); //hashing
					$q = "INSERT INTO users(fname, lname, email, psword, registration_date, user_level) values('$fn', '$ln', '$e', '$hashedPassword', NOW(), 0);";
					$result = @mysqli_query($dbcon, $q);
					if($result){ //if result is okay
						header("location: register-success.php");
						exit();
					}
					
					else{ //if result is not okay
						//display error
						echo '<h2> SYSTEM ERROR </h2>
						
						<p class = "error"> Your registration failed due to an unexpected error, sorry for the inconvenience </p>';
						// for debugging purposes
						
						echo '<p>'.mysqli_error($dbcon).'</p>';
					}
					//close connection of the database
					mysqli_close($dbcon);
					include('footer.php');
					exit();
					
				} else{ //errors occured must display.
					echo '<h2>Error!</h2>
					<p class="error"> The following error(s) occured: <br/>';
					foreach($errors as $msg){
						echo " - $msg<br/>\n";
					}
					echo '</p><h4>Please try again.</h4><br/><br/>';
				}
				
			}
			
		?> 
		</div>
		<div id="reg_page">
		
		<h2 id= "regpg">Registration Page</h2>
			<form action= "register.php" method= "post">
			
			<div id= "text-boxes">
				<p> <label class= "label" for="fname"> First Name: <br/></label>
				<input type= "text" id="fname" name = "fname" placeholder= "Enter First Name" size = "35" maxlength="40" 
				value= "<?php if(isset($_POST['fname'])) echo $_POST['fname'];?>"></input>
				</p>
				
				<p> <label class= "label" for="lname"> Last Name: <br/></label>
				<input type= "text" id="lname" placeholder= "Enter Last Name" name= "lname" size = "35" maxlength="40" 
				value= "<?php if(isset($_POST['lname'])) echo $_POST['lname'];?>"></input>
				</p>
				
				<p> <label class= "label" for="email"> Email Address: <br/></label>
				<input type= "text" id="email" placeholder= "Enter Email Address" name= "email" size = "35" maxlength="50" 
				value= "<?php if(isset($_POST['email'])) echo $_POST['email'];?>"></input>
				</p>
				
				<p> <label class= "label" for="psword1"> Password: <br/></label>
				<input type= "password" id="psword1" placeholder= "Enter Password" name= "psword1" size = "35" maxlength="40" 
				value= "<?php if(isset($_POST['psword1'])) echo $_POST['psword1'];?>"></input>
				</p>
				
				<p> <label class= "label" for="psword2"> Confirm Password: <br/></label>
				<input type= "password" id="psword2" placeholder= "Confirm Password" name= "psword2" size = "35" maxlength="40" 
				value= "<?php if(isset($_POST['psword2'])) echo $_POST['psword2'];?>"></input>
				</p>
				<div id="button">
				<p id= "regbtn">
				<input type="submit" id="submit" name= "submit" value= "Register"></input>
				</p>
				</div>

				</div>
			</form>
			
		</div>
			
		</div>
	</div>
	<?php include('footer.php'); ?>
</body>
</html>