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
		if(empty($_POST['cantidad']) || empty($_POST['nombre']) || empty($_POST['marca'])  || empty($_POST['fecha_vencimiento']) || empty($_POST['costo']))
		{
			$alert='<p class="msg_error">Todos los campos son obligatorios.</p>';
		}else{

			$idp 		= $_POST['idp'];
			$cantidad 	= $_POST['cantidad'];
			$nombre  	= $_POST['nombre'];
			$marca   	= $_POST['marca'];
			$fecha_vencimiento  = $_POST['fecha_vencimiento'];
			$costo   	= $_POST['costo'];

			$sql_update = mysqli_query($conection,"UPDATE productos
															SET cantidad = $cantidad, nombre='$nombre',marca='$marca',fecha_vencimiento='$fecha_vencimiento',costo=$costo
															WHERE idp= $idp");
				
				if($sql_update){
					$alert='<p class="msg_save">Producto actualizado correctamente.</p>';
				}else{
					$alert='<p class="msg_error">Error al actualizar el producto.</p>';
				}

			}


		}
	//Mostrar Datos
	if(empty($_REQUEST['id']))
	{
		header('Location: lista_productos.php');
		mysqli_close($conection);
	}
	$idp = $_REQUEST['id'];

	$sql= mysqli_query($conection,"SELECT * FROM productos WHERE idp= $idp ");
	mysqli_close($conection);
	$result_sql = mysqli_num_rows($sql);

	if($result_sql == 0){
		header('Location: lista_productos.php');
	}else{
		
		while ($data = mysqli_fetch_array($sql)) {
			# code...
			$idp   		= $data['idp'];
			$cantidad 	= $data['cantidad'];
			$nombre  	= $data['nombre'];
			$marca   	= $data['marca'];
			$fecha_vencimiento= $data['fecha_vencimiento'];
			$costo   	= $data['costo'];

		}
	}

 ?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<?php include "includes/scripts.php"; ?>
	<title>Actualizar Productos</title>
</head>
<body>
	<?php include "includes/header.php"; ?>
	<section id="container">
		
		<div class="form_register">
			<h1>Actualizar Productos</h1>
			<hr>
			<div class="alert"><?php echo isset($alert) ? $alert : ''; ?></div>

			<form action="" method="post">
				<input type="hidden" name="idp" value="<?php echo $idp; ?>">
				
				<label for="cantidad">Cantidad</label>
				
				<input type="numeric" name="cantidad" id="cantidad" placeholder="Digite la cantidad" value="<?php echo $cantidad;?>">
				
				<label for="nombre">Nombre</label>
				
				<input type="text" name="nombre" id="nombre" placeholder="Nombre completo" value="<?php echo $nombre;?>">
				
				<label for="marca">Marca</label>
				
				<input type="text" name="marca" id="marca" placeholder="marca" value="<?php echo $marca;?>">
				
				<label for="fecha_vencimiento">fecha vencimiento</label>
				
				<input type="text" name="fecha_vencimiento" id="fecha_vencimiento" placeholder="fecha_vencimiento" value="<?php echo $fecha_vencimiento;?>">
				
				<label for="cantidad">costo</label>

				<input type="numeric" name="costo" id="costo" placeholder="costo" value="<?php echo $costo;?>">
				
				<input type="submit" value="Actualizar Productos" class="btn_save">

				

			</form>

		</div>


	</section>
	<?php include "includes/footer.php"; ?>
</body>
</html>