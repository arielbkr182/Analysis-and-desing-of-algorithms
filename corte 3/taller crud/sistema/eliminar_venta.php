<?php 
	session_start();
	if($_SESSION['rol'] != 1)
	{
		header("location: ./");
	}
	include "../conexion.php";

	if(!empty($_POST))
	{
		if(empty($_POST['nofac'])){
			header("location: lista_venta.php");
			mysqli_close($conection);
			
		}
		$nofac = $_POST['nofac'];

		$query_delete = mysqli_query($conection,"DELETE FROM factura WHERE nofac =$nofac ");
		$query_delete = mysqli_query($conection,"UPDATE factura SET estatus = 0 WHERE nofac = $nofac ");
		mysqli_close($conection);
		if($query_delete){
			header("location: lista_venta.php");
		}else{
			echo "Error al eliminar";
		}

	}




	if(empty($_REQUEST['id']) )
	{
		header("location: lista_venta.php");
		mysqli_close($conection);
	}else{

		$nofac= $_REQUEST['id'];

		$query = mysqli_query($conection,"SELECT * FROM factura WHERE nofac = $nofac");
		
		mysqli_close($conection);
		$result = mysqli_num_rows($query);

		if($result > 0){
			while ($data = mysqli_fetch_array($query)) {
				# code...
				$cantidad 	= $data['cantidad'];
				$nombre 	= $data['nombre'];
				$marca     	= $data['marca'];
				$fecha_venta 	= $data['fecha_venta'];
				$precio_total    	= $data['precio_total'];
			}
		}else{
			header("location: lista_venta.php");
		}


	}


 ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <?php include "includes/scripts.php"; ?>
    <title>Eliminar Factura</title>
</head>

<body>
    <?php include "includes/header.php"; ?>
    <section id="container">
        <div class="data_delete">
            <h2>¿Está seguro de eliminar la siguiente factura:..?</h2>
            <p>Cantidad: <span><?php echo $cantidad; ?></span></p>
            <p>Nombre: <span><?php echo $nombre; ?></span></p>
            <p>Marca: <span><?php echo $marca; ?></span></p>
            <p>Fecha Venta: <span><?php echo $fecha_venta; ?></span></p>
            <p>precio total: <span><?php echo $precio_total; ?></span></p>


            <form method="post" action="">
                <input type="hidden" name="nofac" value="<?php echo $nofac; ?>">
                <a href="lista_venta.php" class="btn_cancel">Cancelar</a>
                <input type="submit" value="Aceptar" class="btn_ok">
            </form>
        </div>


    </section>
    <?php include "includes/footer.php"; ?>
</body>

</html>