import React from 'react'
import { useSearchParams } from 'react-router-dom';
import './index.css'

function Domain() {
    const [searchParams, setSearchParams] = useSearchParams();
    const domainName =searchParams.get('domain');
  return (
    <div className='result-container'>
        <h1>Results</h1>
        <h2>Domain Name:{domainName}</h2>
    </div>
  )
}

export default Domain