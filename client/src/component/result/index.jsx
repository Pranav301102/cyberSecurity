import React from "react";
import { useSearchParams } from "react-router-dom";
import ResultCard from "../resultCard";
import "./index.css";
import { useEffect, useState } from "react";
import axios from "axios";

function Domain() {
  const [searchParams, setSearchParams] = useSearchParams();
  const domainName = searchParams.get("domain");
  document.body.style.overflowY = "scroll";
  document.body.style.overflowX = "hidden";
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
      <ResultCard
        title={"SSL Audit"}
        domainName={domainName}
        query={"queue-ssl"}
      />
      <ResultCard
        title={"OS Audit"}
        domainName={domainName}
        query={"queue-os"}
      />
      <ResultCard
        title={"TraceRoute"}
        domainName={domainName}
        query={"queue-traceroute"}
      />
      <ResultCard
        title={"Port Scan"}
        domainName={domainName}
        query={"queue-portscan"}
      />
      <ResultCard
        title={"Reverse DNS"}
        domainName={domainName}
        query={"queue-reversedns"}
      />
    </div>
  );
}

export default Domain;
