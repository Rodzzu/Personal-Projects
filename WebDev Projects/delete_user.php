<?php 
	session_start();
	if(isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 1)){
		header('Location: login.php');
		exit();
	}
?>

<!doctype html>
<html lang="en">

<head>
    <title>Deleting User</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="stylesartuz.css">
</head>

<body>
    <div id="topbar">
        <?php include('header.php'); ?>
        <?php include('nav_admin.php'); ?>
    </div>
    <div id="container">
        <?php include('info-col.php'); ?>

        <div id="content">
            <h2>Deleting Record</h2>
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
            if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                if ($_POST['sure'] == 'Yes') {
                    //delete method
                    $q = "DELETE FROM users WHERE user_id = $id"; //query to delete the user
                    $result = @mysqli_query($dbcon, $q);
                    if (mysqli_affected_rows($dbcon) == 1) { //if no problem, delete success
                        echo '<h3>The record has been deleted.</h3>';
                    } else { //if not deleted
                        echo '<h3>Record failed to be deleted.</h3>';
                    }
                } else {
                    echo '<h3>The record has not been deleted.</h3>';
                }
            } else {
                //display information of the user to be deleted
                $q = "SELECT CONCAT(fname, ' ', lname) FROM users WHERE user_id = $id"; //fixed query
                $result = @mysqli_query($dbcon, $q);
                if (mysqli_affected_rows($dbcon) == 1) { //there's a user that has that id
                    $row = mysqli_fetch_array($result, MYSQLI_NUM);
                    echo "<h3>Are you sure you want to permanently delete $row[0] ? </h3>";
                    //display buttons for delete and cancel
                    echo '
                    <form action="delete_user.php" method="post">
                        <input id="submit-yes" type="submit" name="sure" value="Yes">
                        <input id="submit-no" type="submit" name="sure" value="No">
                        <input type="hidden" name="id" value="' . $id . '">
                    </form>
                    ';
                } else {
                    //no user exists
                    echo 'User does not exist.';
                }
            }
            mysqli_close($dbcon);
            include('footer.php');
            ?>
        </div>
    </div>
    <?php include('footer.php'); ?>
</body>
</html>