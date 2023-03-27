import React from 'react'
import './Header.css'

export default function Header() {
    window.onload = function(){ 
/* -- Glow effect -- */

const blob = document.getElementById("blob");

window.onpointermove = event => { 
  const { clientX, clientY } = event;
  
  blob.animate({
    left: `${clientX}px`,
    top: `${clientY}px`
  }, { duration: 3000, fill: "forwards" });
}

/* -- Text effect -- */

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

document.querySelector("h1").onmouseover = event => {  
  let iteration = 0;
  
  clearInterval(interval);
  
  interval = setInterval(() => {
    event.target.innerText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if(index < iteration) {
          return event.target.dataset.value[index];
        }
      
        return letters[Math.floor(Math.random() * 26)]
      })
      .join("");
    
    if(iteration >= event.target.dataset.value.length){ 
      clearInterval(interval);
    }
    
    iteration += 1 / 3;
  }, 30);
}
}

  return (
    <body>
        <div className="search">
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" media="screen" />
            <input type="text" className="search-txt" name="" placeholder="Enter your IP address" />
            <a href="/" className="search-btn"><i className="fa fa-search"></i></a>
        </div>
        
        <div className='body'>
            <div id="blob"></div>
            <div id="blur"></div>
            <h1 data-value="CyberSecurity">CyberSecurity</h1>
        </div>    
    </body>    

  )
}
