
function primo (numero){
    let raiz = Math.floor(Math.sqrt(numero))+1;
   
      for(let i=2 ; i< raiz; ++i){
          
        if(numero % i == 0){
      return "no es primpo " + numero;
           
           
           
      }  
    } 
       return "es primo "+ numero;
}


    document.write(primo(3));


