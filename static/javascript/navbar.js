var inputBox = document.getElementById("inputBox");
var hideableElements = document.getElementsByClassName("hideable");

// A CORRIGIR: 
// Se clicar rápido fora e dentro da barra de pesquisa, não funciona mais como o esperado

function fadeOut(elements, i){
    var op = 1; // largura inicial

    function decrease()
    {   
        op -= 0.05;

        if(op <= 0)
        {
            elements[i].style.opacity = 0;
            elements[i].style.display = "none";
            i += 1
            if(i == elements.length){return true;}
            else{return fadeOut(elements, i)}
        }
        
        elements[i].style.opacity = op;
        requestAnimationFrame(decrease);
    }
    decrease();
}

function fadeIn(elements, i){
    elements[i].style.display = "block";
    var op = 0; // largura inicial

    function increase()
    {   
        op += 0.05;

        if(op >= 1)
        {
            elements[i].style.opacity = 1;
            i -= 1
            if(i== -1){return true;}
            else{return fadeIn(elements, i)}
        }
        
        elements[i].style.opacity = op;
        requestAnimationFrame(increase);
    }
    increase();
}


function show()
{
    fadeIn(hideableElements, hideableElements.length-1);
}

function hide()
{
    fadeOut(hideableElements, 0);
}

if (screen.width <= 600)
{
    inputBox.addEventListener("focus", hide);

    inputBox.addEventListener("focusout", show);
}