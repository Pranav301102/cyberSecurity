import React from "react";
import "./index.css";

function ResultCard({title,data ,loading}) {
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