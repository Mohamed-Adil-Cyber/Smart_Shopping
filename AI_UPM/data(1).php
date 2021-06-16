<?php
session_start();
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
        <div class="table-responsive mt-5">
            <table class="table table-bordered table-striped text-center">
                <thead>
                    <tr>
                        <td colspan="5">
                            <h4 class="text-center text-info m-0">Products in your cart</h4>
                        </td>
                    </tr>
                    <tr>
                        <th>Product ID</th>
                        <th>Product Name</th>
                        <th>Quantity</th>
                        <th>Product Price</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                // display all items in cart table
                require 'config.php';
                $stmt = $conn->prepare("SELECT * FROM Products_Table");
                $stmt->execute();
                $result = $stmt->get_result();
                $grand_total = 0;
                while ($row = $result->fetch_assoc()) :
                ?>
                    <tr>
                        <td><?= $row['Product_ID'] ?></td>
                        <input type="hidden" class="pid" value="<?= $row['Product_ID'] ?>">

                        <td><?= $row['Product_Name'] ?></td>

                        <td><?= $row['Quantity_InStock'] ?></td>
                        <input type="hidden" class="itemQty" value="<?= $row['Quantity_InStock'] ?>">

                        <td><?= number_format($row['Product_Price'], 2); ?></td>
                        <input type="hidden" class="pprice" value="<?= $row['Product_Price'] ?>">
                        <td>
                            <a href="action.php?remove=<?= $row['Product_ID'] ?>" class="text-danger lead"
                                onclick="return confirm('Are you sure want to remove this item?');"><i
                                    class="fas fa-trash-alt"></i></a>
                        </td>
                    </tr>
                    <?php $grand_total += $row['Quantity_InStock']*$row['Product_Price']; ?>

                    <?php endwhile ?>
                    <td colspan="4"><b>Grand Total</b></td>
                    <td>
                        <b> <i class="fas fa-money-bill-wave"></i>&nbsp;&nbsp;<?= number_format($grand_total, 2); ?></b>
                    </td>
                </tbody>
            </table>

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
                    url: 'action.php',
                    method: 'post',
                    cache: false,
                    data: {
                        qty:qty,
                        pid:pid,
                        pprice:pprice
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