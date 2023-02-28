
function palabra(){
let palabra= prompt("Dame la palabra");

let convertir= palabra.split("");
 let palabra2= convertir.reverse();
let palabra3= palabra2.join("");

if(palabra3 == palabra){
   return "La palabra "+palabra+" es Palíndroma";
   
   }else{
       return "La palabra "+palabra+" no es Palíndroma"
   }
}

document.write(palabra());