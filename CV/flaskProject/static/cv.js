let txt="Welcome To My CV Webpage";
let i=0;
let speed= 70;

function Typewriter(){
    if(i< txt.length){
        document.getElementById("welcome").innerHTML += txt.charAt(i);
        i++;
        setTimeout(Typewriter,speed);
    }
}

