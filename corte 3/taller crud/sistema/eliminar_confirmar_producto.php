<?php 
	session_start();
	if($_SESSION['rol'] != 1)
	{
		header("location: ./");
	}
	include "../conexion.php";

	if(!empty($_POST))
	{
		if(empty($_POST['idp'])){
			header("location: lista_productos.php");
			mysqli_close($conection);
			
		}
		$idp = $_POST['idp'];

		$query_delete = mysqli_query($conection,"DELETE FROM productos WHERE idp =$idp ");
		$query_delete = mysqli_query($conection,"UPDATE productos SET estatus = 0 WHERE idp = $idp ");
		mysqli_close($conection);
		if($query_delete){
			header("location: lista_productos.php");
		}else{
			echo "Error al eliminar";
		}

	}




	if(empty($_REQUEST['id']) )
	{
		header("location: lista_productos.php");
		mysqli_close($conection);
	}else{

		$idp = $_REQUEST['id'];

		$query = mysqli_query($conection,"SELECT * FROM productos WHERE idp = $idp");
		
		mysqli_close($conection);
		$result = mysqli_num_rows($query);

		if($result > 0){
			while ($data = mysqli_fetch_array($query)) {
				# code...
				$cantidad 	= $data['cantidad'];
				$nombre 	= $data['nombre'];
				$marca     	= $data['marca'];
				$fecha_vencimiento 	= $data['fecha_vencimiento'];
				$costo    	= $data['costo'];
			}
		}else{
			header("location: lista_productos.php");
		}


	}


 ?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<?php include "includes/scripts.php"; ?>
	<title>Eliminar Producto</title>
</head>
<body>
	<?php include "includes/header.php"; ?>
	<section id="container">
		<div class="data_delete">
			<h2>¿Está seguro de eliminar el siguiente registro?</h2>
			<p>Cantidad: <span><?php echo $cantidad; ?></span></p>
			<p>Nombre: <span><?php echo $nombre; ?></span></p>
			<p>Marca: <span><?php echo $marca; ?></span></p>
			<p>Fecha Vencimiento: <span><?php echo $fecha_vencimiento; ?></span></p>
			<p>Costo: <span><?php echo $costo; ?></span></p>
			

			<form method="post" action="">
				<input type="hidden" name="idp" value="<?php echo $idp; ?>">
				<a href="lista_productos.php" class="btn_cancel">Cancelar</a>
				<input type="submit" value="Aceptar" class="btn_ok">
			</form>
		</div>


	</section>
	<?php include "includes/footer.php"; ?>
</body>
</html>