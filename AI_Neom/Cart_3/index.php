<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="icon" href="/AI_Neom/images/logo-light.png"/>

	<title>AI_Neom</title>
	<style>
        body {
            /* The image used */


            /* Full height */
            background-image: url("/AI_Neom/images/bg-2.jpg");

            /* Center and scale the image nicely */

            background-size: cover;
        }

    </style>
</head>
<body>
	<div id="show"></div>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script type="text/javascript">
    $(document).ready(function() {
        setInterval(function () {
            $('#show').load('/AI_Neom/Cart_3/data.php')
			}, 1000);
    });
	</script>


</body>
</html>