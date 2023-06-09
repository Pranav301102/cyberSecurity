import React from 'react'
import Search from '../search';
import { Canvas, useFrame } from '@react-three/fiber'
import { useGLTF, Html, OrbitControls, Environment, ContactShadows,Stars } from '@react-three/drei'
import "./index.css"

function Model(props) {
  const ref = React.useRef()
  /*
  Auto-generated by: https://github.com/pmndrs/gltfjsx
  author: JasperTobias (https://sketchfab.com/JasperTobias)
  license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/)
  source: https://sketchfab.com/3d-models/lowpoly-earth-ce0cce9b528b47c7984bf0b2b600d705
  title: LowPoly Earth
  */ 
  const { nodes, materials } = useGLTF('/earth.gltf')
  return (
    <group ref={ref}scale={1.6} rotation={[-Math.PI / 2, 0, Math.PI]} {...props} dispose={null}>
      <mesh geometry={nodes['URF-Height_Lampd_Ice_0'].geometry} material={materials.Lampd_Ice} />
      <mesh geometry={nodes['URF-Height_watr_0'].geometry} material={materials.watr} material-roughness={0} />
      <mesh geometry={nodes['URF-Height_Lampd_0'].geometry} material={materials.Lampd} material-color="lightgreen">
      </mesh>
    </group>
  )
}


function Home() {
    window.onload = function(){        
        /* -- Text effect -- */
        
        const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        let interval = null;
        //disable scrolling for the page
        document.body.style.overflow = "hidden";
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
        <div className="container">
        <Canvas camera={{ position: [5, 0, 0], fov: 50 }}>
            
            <Model position={[0, 0.25, 0]} />
            <Stars radius={50} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
            <Environment preset="park" />
            <OrbitControls />
        </Canvas>
        </div>
        <h1 id='title' data-value="ScanX">ScanX</h1>

        <Search />
    </div>
  )
}

export default Home
