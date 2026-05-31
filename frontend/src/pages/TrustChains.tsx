import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import TrustChainTableCard from "../components/TrustChainTableCard";
import api from "../services/api";

function TrustChains() {

  const [chains, setChains] =
    useState<any[]>([]);

  useEffect(() => {
    loadChains();
  }, []);

  const loadChains = async () => {

    try {

      const response =
        await api.get("/trust-chain");

      setChains(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <Layout>

      <div className="p-8">

        <h1 className="text-4xl font-bold mb-8">
          Trust Chains
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {chains.map((chain) => (

            <TrustChainTableCard
              key={chain.chain_id}
              finding={chain.finding}
              research_agent={chain.research_agent}
              review_agent={chain.review_agent}
              security_agent={chain.security_agent}
              chain_valid={chain.chain_valid}
            />

          ))}

        </div>

      </div>

    </Layout>

  );
}

export default TrustChains;