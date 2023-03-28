import React from 'react'
import Search from '../search';
import "./index.css"

function Home() {
    window.onload = function(){        
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
    <div>
        <h1 id='title' data-value="Cyber Security">CYBER SECURITY</h1>
        <Search />
    </div>
  )
}

export default Home
