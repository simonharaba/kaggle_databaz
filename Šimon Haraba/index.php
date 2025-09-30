    <?php 
include('./config.php');

?>
<!DOCTYPE html>
<html lang="sk">

<head>
<title><?php echo(COMPANY_NAME); ?> - <?php echo (COMPANY_ADDRESS);?></title>

<link rel="stylesheet" type="text/css" href="assets/css/root.css">

</head>

<body>
<h1><?php echo(WEB_AUTHOR); ?></h1>
<p1><?php echo(COMPANY_NAME); ?></p1>
<header>
    <div class="header-logo">
        <img src="./assets/imgs/logo.png">
    </div>
    <nav>
        <ul>
            <li><a href="./index.php">=Uvod</a></li>
            <li><a href="./about.php">=O mne</a></li>
            <li><a href="./contacts.php">=Kontakty</a></li>
        </ul>
    </nav>
</header>

<main>
    <h1>nadpis</h1>
    <p>text</p>
</main>

<footer>
    
</footer>
</body>
</html>
