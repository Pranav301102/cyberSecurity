import React from 'react'
import "./index.css"
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Search() {
  const [input, setInput] = useState('');
  useEffect(() => {
    console.log(input);
  }, [input]);
  const nav = useNavigate();
  

const handleClick = () => {
  //check if input is valid domain name  
  if (input.match(/^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$/)) {
    nav(`/result?domain=${input}`);  
  } else {
    alert("Please enter a valid domain name");
  }
}
  

  return (
    <div className="search">
            <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" media="screen" />
            <input type="text" className="search-txt" name="" placeholder="Enter domain name" onChange={(e)=>setInput(e.target.value) }/>
            <button className="search-btn" onClick={handleClick}><i className="fa fa-search"></i></button>
    </div>   
  )
}

export default Search