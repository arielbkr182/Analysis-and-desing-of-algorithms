<?php 
	
	session_start();
	if($_SESSION['rol'] != 1)
	{
		header("location: ./");
	}

	include "../conexion.php";

	if(!empty($_POST))
	{
		$alert='';
		if(empty($_POST['cantidad']) || empty($_POST['nombre']) || empty($_POST['marca'])  || empty($_POST['fecha_venta']) || empty($_POST['precio_total']))
		{
			$alert='<p class="msg_error">Todos los campos son obligatorios.</p>';
		}else{

			$nofac 		= $_POST['nofac'];
			$cantidad 	= $_POST['cantidad'];
			$nombre  	= $_POST['nombre'];
			$marca   	= $_POST['marca'];
			$fecha_venta  = $_POST['fecha_venta'];
			$precio_total 	= $_POST['precio_total'];

			$sql_update = mysqli_query($conection,"UPDATE factura
															SET cantidad = $cantidad, nombre='$nombre',marca='$marca',fecha_venta='$fecha_venta',precio_total=$precio_total
															WHERE nofac= $nofac");
				
				if($sql_update){
					$alert='<p class="msg_save">Factura actualizada correctamente.</p>';
				}else{
					$alert='<p class="msg_error">Error al actualizar el factura.</p>';
				}

			}


		}
	//Mostrar Datos
	if(empty($_REQUEST['id']))
	{
		header('Location: lista_venta.php');
		mysqli_close($conection);
	}
	$nofac = $_REQUEST['id'];

	$sql= mysqli_query($conection,"SELECT * FROM factura WHERE nofac= $nofac ");
	mysqli_close($conection);
	$result_sql = mysqli_num_rows($sql);

	if($result_sql == 0){
		header('Location: lista_venta.php');
	}else{
		
		while ($data = mysqli_fetch_array($sql)) {
			# code...
			$nofac  		= $data['nofac'];
			$cantidad 	= $data['cantidad'];
			$nombre  	= $data['nombre'];
			$marca   	= $data['marca'];
			$fecha_venta= $data['fecha_venta'];
			$precio_total   	= $data['precio_total'];

		}
	}

 ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <?php include "includes/scripts.php"; ?>
    <title>Actualizar Ventas</title>
</head>

<body>
    <?php include "includes/header.php"; ?>
    <section id="container">

        <div class="form_register">
            <h1>Actualizar Ventas</h1>
            <hr>
            <div class="alert"><?php echo isset($alert) ? $alert : ''; ?></div>

            <form action="" method="post">
                <input type="hidden" name="nofac" value="<?php echo $nofac; ?>">

                <label for="cantidad">Cantidad</label>

                <input type="numeric" name="cantidad" id="cantidad" placeholder="Digite la cantidad"
                    value="<?php echo $cantidad;?>">

                <label for="nombre">Nombre</label>

                <input type="text" name="nombre" id="nombre" placeholder="Nombre completo"
                    value="<?php echo $nombre;?>">

                <label for="marca">Marca</label>

                <input type="text" name="marca" id="marca" placeholder="marca" value="<?php echo $marca;?>">

                <label for="fecha_venta">fecha venta</label>

                <input type="text" name="fecha_venta" id="fecha_venta" placeholder="fecha_venta"
                    value="<?php echo $fecha_venta;?>">

                <label for="cantidad">precio total</label>

                <input type="numeric" name="precio_total" id="precio_total" placeholder="precio_total"
                    value="<?php echo $precio_total;?>">

                <input type="submit" value="Actualizar Venta" class="btn_save">



            </form>

        </div>


    </section>
    <?php include "includes/footer.php"; ?>
</body>

</html>