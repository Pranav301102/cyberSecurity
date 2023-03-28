import React from "react";
import { useSearchParams } from "react-router-dom";
import ResultCard from "../resultCard";
import "./index.css";
import { useEffect, useState } from "react";
import axios from "axios";

function Domain() {
  const [searchParams, setSearchParams] = useSearchParams();
  const domainName = searchParams.get("domain");
  return (
    <div className="result-container">
      <h1>Results</h1>
      <h2>Domain Name:{domainName}</h2>
      <ResultCard
        title={"Ping Audit"}
        domainName={domainName}
        query={"queue-ping"}
      />
      <ResultCard
        title={"Subdomain Audit"}
        domainName={domainName}
        query={"queue-subdomain"}
      />
    </div>
  );
}

export default Domain;
