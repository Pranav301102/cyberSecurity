import React from 'react'
import { useSearchParams } from 'react-router-dom';
import ResultCard from '../resultCard';
import './index.css'

function Domain() {
    const [searchParams, setSearchParams] = useSearchParams();
    const domainName =searchParams.get('domain');
  return (
    <div className='result-container'>
        <h1>Results</h1>
        <h2>Domain Name:{domainName}</h2>
        <ResultCard title={"Ping-test"} data={'description'} loading={true}/>
        <ResultCard title={"Ping-test"} data={'description'} loading={false}/>
        <ResultCard title={"Ping-test"} data={'description'} loading={false}/>
    </div>
  )
}

export default Domain