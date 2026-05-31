import { useEffect, useState } from "react";
import api from "../services/api";

import TrustChainCard from "../components/TrustChainCard";

function Dashboard() {

  const [agents, setAgents] = useState(0);
  const [chains, setChains] = useState(0);
  const [allowed, setAllowed] = useState(0);
  const [denied, setDenied] = useState(0);

  const [trustChains, setTrustChains] = useState<any[]>([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {

    try {

      const agentsResponse =
        await api.get("/agents");

      const chainsResponse =
        await api.get("/trust-chain");

      const auditResponse =
        await api.get("/audit/logs");

      setAgents(
        agentsResponse.data.length
      );

      setChains(
        chainsResponse.data.length
      );

      setTrustChains(chainsResponse.data);

      const allowedCount =
        auditResponse.data.filter(
          (item: any) =>
            item.status === "allowed"
        ).length;

      const deniedCount =
        auditResponse.data.filter(
          (item: any) =>
            item.status === "denied"
        ).length;

      setAllowed(allowedCount);

      setDenied(deniedCount);

    } catch (error) {

      console.error(error);

    }
  };

  return (
    <div className="min-h-screen bg-gray-100">

      <div className="p-8">

        <h1 className="text-4xl font-bold mb-8">
          AgentTrust Dashboard
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Total Agents
            </h2>

            <p className="text-3xl font-bold">
              {agents}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Trust Chains
            </h2>

            <p className="text-3xl font-bold">
              {chains}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Allowed Actions
            </h2>

            <p className="text-3xl font-bold">
              {allowed}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Denied Actions
            </h2>

            <p className="text-3xl font-bold">
              {denied}
            </p>
          </div>

        </div>

        <div className="mt-10">

            <h2 className="text-2xl font-bold mb-4">
                Recent Trust Chains
            </h2>

            <div className="space-y-4">

                {trustChains.map((chain) => (

                <TrustChainCard
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

      </div>

    </div>
  );
}

export default Dashboard;