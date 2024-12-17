<?php
ob_start(); // Start output buffering to prevent header issues
session_start(); // Start the session
?>
<!doctype html>
<html lang="en">

<head>
    <title>Website ni Artuz</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="stylesartuz.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
</head>

<body>
    <div id="topbar">
        <?php include('header.php'); ?>
        <?php include('nav_login.php'); ?>
    </div>
    <div id="container2">
        <div id="content3">
            <div id="errors">
                <?php
                if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                    require('mysqli_connect.php');

                    $e = !empty($_POST['email']) ? mysqli_real_escape_string($dbcon, $_POST['email']) : NULL;
                    $p = !empty($_POST['psword1']) ? mysqli_real_escape_string($dbcon, $_POST['psword1']) : NULL;

                    if ($e && $p) {
                        $hashed = hash('sha256', $p);
                        $q = "SELECT user_id, fname, user_level FROM users WHERE (email = '$e' AND psword = '$hashed')";
                        $result = mysqli_query($dbcon, $q);

                        if (@mysqli_num_rows($result) == 1) {
                            $_SESSION = mysqli_fetch_array($result, MYSQLI_ASSOC);
                            $_SESSION['user_level'] = (int) $_SESSION['user_level'];

                            $url = ($_SESSION['user_level'] === 1) ? 'admin.php' : 'mem_home.php';
                            header('Location: ' . $url);
                            exit();
                        } else {
                            echo '<p class="error">Error! No matching user found.</p>';
                        }
                    } else {
                        echo '<p class="error">Error! Please enter email and password.</p>';
                    }

                    mysqli_close($dbcon);
                }
                ?>
            </div>

            <div id="reg_page">
                <h2 id="regpg">Login Page</h2>
                <form action="login.php" method="post">
                    <div id="text-boxes">
                        <p><label class="label" for="email">Email Address:<br /></label>
                            <input type="text" id="email" placeholder="Enter Email Address" name="email" size="35" maxlength="50"
                                value="<?php if (isset($_POST['email'])) echo $_POST['email']; ?>">
                        </p>

                        <p><label class="label" for="psword1">Password:<br /></label>
                            <input type="password" id="psword1" placeholder="Enter Password" name="psword1" size="35" maxlength="40"
                                value="<?php if (isset($_POST['psword1'])) echo $_POST['psword1']; ?>">
                        </p>

                        <div id="button">
                            <p id="regbtn">
                                <input type="submit" id="submit" name="submit" value="Login">
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
