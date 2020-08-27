<?php
session_start();
?>

<?php
require '../config.php';
$id = $_GET['id'];
$stmt = $conn->prepare("SELECT * FROM Cart_Table WHERE Cart_ID=3");
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_assoc();
if (!$row) {
    header("Location: /AI_Neom/Cart_3/home.php");
    die;
}
?>
<?php
                // display all items in cart table
                require '../config.php';
                $stmt = $conn->prepare("SELECT * FROM Cart_Table WHERE Cart_ID=3");
                $stmt->execute();
                $result = $stmt->get_result();
                $caid = $row['Cart_ID'];
                $cuid = $row['Customer_ID'];
        ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>AI_Neom</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
</head>

<body>


    <div class="container">
    <div class="row">
            <div class="col-5">
                <img src="/AI_Neom/images/mainAR_logo.png" class="mt-5 w-75" >
            </div>
            <div class="col-7 mt-4 m⁩r-2">
                <div class="mt-4">
                    <div class="row">
                        <div class="col-1 mr-4">
                            <i class="fas fa-shopping-cart fa-3x" style="color:white"></i>
                        </div>
                        <div class="col-3 mr-3 mt-1">
                            <span
                                style="width: 150px;height:40px;font-size:23px;background-color:dodgerblue;color:white "
                                class="badge">CART ID</span>
                        </div>
                        <div class="col-4 mr-3 mt-1">
                            <span style="width: 150px;height:40px;color:dodgerblue;font-size:23px"
                                class="badge badge-light"><?= $caid ?></span>
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-1 mr-4">
                            <i class="fas fa-id-card fa-3x" style="color:white"></i>
                        </div>
                        <div class="col-3 mr-3 mt-1">
                            <span
                                style="width: 150px;height:40px;font-size:23px;background-color:dodgerblue;color:white "
                                class="badge">Customer ID</span>
                        </div>
                        <div class="col-4 mr-3 mt-1">
                            <span style="width: 150px;height:40px;color:dodgerblue;font-size:23px"
                                class="badge badge-light"><?= $cuid ?></span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        <div class="table-responsive mt-5">
            <table class="table table-bordered table-striped text-center bg-light">
                <thead>
                    <tr>
                        <td colspan="4">
                            <h4 class="text-center text-info m-0">Products in your cart</h4>
                        </td>
                    </tr>
                    <tr>

                        <th>Item</th>
                        <th>Count</th>
                        <th>Total Price</th>
                        <th>
                            <a href="/AI_Neom/Cart_3/action.php?clear=all" class="badge-danger badge p-1"
                                onclick="return confirm('Are you sure want to clear your cart?');"><i
                                    class="fas fa-trash"></i>&nbsp;&nbsp;Clear Cart</a>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // display all items in cart table
                    require '../config.php';
                    $stmt = $conn->prepare("SELECT * FROM InStore_Table WHERE Cart_ID=3");
                    $stmt->execute();
                    $result = $stmt->get_result();
                    $grand_total = 0;
                    while ($row = $result->fetch_assoc()) :
                    ?>
                    <tr>

                        <td><?= $row['Item'] ?></td>
                        <input type="hidden" class="pitem" value="<?= $row['Count'] ?>">
                        <td><?= $row['Count'] ?></td>
                        <input type="hidden" class="itemQty" value="<?= $row['Item'] ?>">

                        <td><?= number_format($row['Total_Price'], 2); ?> SAR</td>
                        <input type="hidden" class="pprice" value="<?= $row['Total_Price'] ?>">
                        <td>
                            <a href="/AI_Neom/Cart_3/action.php?remove=<?= $row['Item'] ?>" class="text-danger lead"
                                onclick="return confirm('Are you sure want to remove this item?');"><i
                                    class="fas fa-trash-alt"></i></a>
                        </td>
                    </tr>
                    <?php $grand_total += $row['Total_Price']; ?>

                    <?php endwhile ?>
                    <td colspan="3"><b>Grand Total</b></td>
                    <td>
                        <b> <i class="fas fa-money-bill-wave"></i>&nbsp;&nbsp;<?= number_format($grand_total, 2); ?>
                            SAR</b>
                    </td>
                </tbody>
            </table>
            <h1 class="text-center mt-5" style="color:white"><b>Recommended Items</b></h1>
            <?php
                    // display all items in cart table
                    require '../config.php';
                    $stmt = $conn->prepare("SELECT * FROM Recommendation WHERE Cart_ID=3");
                    $stmt->execute();
                    $result = $stmt->get_result();
                 
                    while ($row = $result->fetch_assoc()) :
                    ?>
            <div class="card mb-3 " >
  <div class="row no-gutters rounded-lg ">
    <div class="col-md-2 ">
    <img src="<?= $row['Recommend_Image'] ?>" class="img-fluid mh-25">
        </div>
    <div class="col-md-10">
      <div class="card-body">
        <h2 class="card-title text-center"><?= $row['Recommend_Item'] ?></h2>
        
      </div>
    </div>
  </div>
</div>      
<?php endwhile ?>  
        </div>
        
    </div>
    <script type="text/javascript">
    $(document).ready(function() {
        // send the id and price of the item that i want to chang it's quantity
        $(".itemQty").on('change', function() {
            var $el = $(this).closest('tr');
            var pid = $el.find('.pid').val();
            var pprice = $el.find('.pprice').val();
            var qty = $el.find('.itemQty').val();
            location.reload(true);

            $.ajax({
                url: '/AI_Neom/Cart_3/action.php',
                method: 'post',
                cache: false,
                data: {
                    qty: qty,
                    pid: pid,
                    pprice: pprice
                },
                success: function(response) {
                    console.log(response);
                }

            });
        });

    });
    </script>
</body>

</html>