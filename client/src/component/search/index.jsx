import React from 'react'
import "./index.css"

function Search() {

  return (
    <div className="search">
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" media="screen" />
            <input type="text" className="search-txt" name="" placeholder="Enter your IP address" />
            <a href="/domain" className="search-btn"><i className="fa fa-search"></i></a>
    </div>   
  )
}

export default Search