import React from 'react'
import { useEffect,useState } from 'react';
import "./index.css"

function Background() {
  const [mousePos, setMousePos] = useState({});

  //use effect to get mouse position
  useEffect(() => {
    const getMousePos = (e) => {
      const pos = { x: 0, y: 0 };
      pos.x = e.clientX;
      pos.y = e.clientY;
      setMousePos(pos);
    };
    window.addEventListener("mousemove", getMousePos);
    return () => window.removeEventListener("mousemove", getMousePos);
  }, []);

  useEffect(() => {
    const blob = document.getElementById("blob");
    blob.animate(
      [
        {
          left: `${mousePos.x}px`,
          top: `${mousePos.y}px`,
        },
        {
          left: `${mousePos.x + 50}px`,
          top: `${mousePos.y + 50}px`,
        },
      ],
      {
        duration: 30000,
        fill: "forwards",
      }
    );
  }, [mousePos]);


  return (
    <div className='background'>
      <div id="blob"></div>
      <div id="blur"></div>
    </div>
  )
}

export default Background
