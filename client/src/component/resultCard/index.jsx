import React from "react";
import "./index.css";
import { useEffect, useState } from "react";
import axios from "axios";

function ResultCard({title,domainName,query}) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [ID, setID] = useState();
  

    useEffect(() => {
      axios
        .get(`http://localhost:8000/${query}?domain=${domainName}`)
        .then((res) => {
          setID(res.data.requestId);
        })
        .catch((err) => {
          console.log(err);
        });
    }, [domainName,query]);
  
    useEffect(() => {
      console.log({ID});
      if(ID){
       const interval = setInterval(() => {
        axios
          .get(`http://localhost:8000/get-result?id=${ID}`)
          .then((res) => {
            if (res.data.completed === true) {
              setData(res.data.result);
              setLoading(false);
              clearInterval(interval);
            }else{
              setLoading(true);
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
      , 1000);
      return () => clearInterval(interval);
      }
    }, [ID]);
    if(loading){
        return (
            <div className="card">
              <details>
                <summary>{title} <img src="loading.gif" alt="loading"/> </summary>
                <div className="loading">
                  Loading...
                </div>
              </details>
            </div>
          );
    }
  return (
    <div className="card">
      <details>
        <summary>{title}</summary>
        <div>
        {data}
        </div>
      </details>
    </div>
  );
}
export default ResultCard;