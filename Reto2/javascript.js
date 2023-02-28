function numeros(entero){
    
    if(entero<10){
         let primeros =["cero","uno","dos","tres","cuanto ","cinco","seis","siete","ocho","nueve"];
        
        return(primeros[entero]);
        
    }
    if(entero >= 10 && entero<21){
        let segundos =["Diez","once","Doce","trece","catorce ","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte"];
        let indice = entero-10;
       return(segundos[indice]);
         
       
       }
    if(entero>=21 && entero<101){
        let decenas=["","Diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa","cien"];
           let unidades =["uno","uno","dos","tres","cuanto ","cinco","seis","siete","ocho","nueve","cien"];
        let convertir = Math.floor(entero/10);
        let unidad= Math.floor(((entero/10)-convertir)*10);
        if(entero%10 >= 1){
       
           return decenas[convertir]+" y "+unidades[unidad];
       }
     return decenas[convertir]; 
    }
    
}

document.write(numeros(10));