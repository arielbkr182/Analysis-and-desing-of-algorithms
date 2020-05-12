<?php 
//
if($_POST['action'] == 'procesarVenta'){
    if(empty($_POST['codcliente'])){
        $codcliente = 1;
    }else{
        $codcliente = $_POST['codcliente'];
    }
    $token = md5($_SESSION['idUser']);
    $usuario =$_SESSION['idUser'];



    $query = mysqli_query($conection,"SELECT * FROM detalle_temp WHERE token_user = '$token'");
    $result = mysqli_num_rows($query);

    if($result > 0)
    {
        $query_procesar = mysqli_query($conection,"CALL procesar_venta($usuario,$codcliente,'$token')");
        $result_detalle = mysqli_num_rows($query_procesar);

        if($result_detalle > 0 ){
            $data = mysqli_fetch_assoc($query_procesar);
            echo json_encode($data,JSON_UNESCAPED_UNICODE);
        
        
        }else{
            echo "error1";
        }
    }else{
        echo "error2";
    }
    mysqli_close($conection);
    exit;


}





?>
