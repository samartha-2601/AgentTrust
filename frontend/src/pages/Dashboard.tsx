import { useEffect, useState } from "react";

import api from "../services/api";

import Layout from "../components/Layout";
import TrustChainCard from "../components/TrustChainCard";
import AuditEventCard from "../components/AuditEventCard";

function Dashboard() {

  const [agents, setAgents] = useState(0);
  const [chains, setChains] = useState(0);
  const [allowed, setAllowed] = useState(0);
  const [denied, setDenied] = useState(0);

  const [trustChains, setTrustChains] =
    useState<any[]>([]);

  const [auditEvents, setAuditEvents] =
    useState<any[]>([]);

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

      setTrustChains(
        chainsResponse.data
      );

      setAuditEvents(
        auditResponse.data
      );

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

    <Layout>

      <div className="p-8">

        <h1 className="text-4xl font-bold mb-8">
          AgentTrust Dashboard
        </h1>

        {/* Metrics */}

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Total Agents
            </h2>

            <p className="text-4xl font-bold mt-2">
              {agents}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Trust Chains
            </h2>

            <p className="text-4xl font-bold mt-2">
              {chains}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Allowed Actions
            </h2>

            <p className="text-4xl font-bold mt-2 text-green-600">
              {allowed}
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-gray-500">
              Denied Actions
            </h2>

            <p className="text-4xl font-bold mt-2 text-red-600">
              {denied}
            </p>
          </div>

        </div>

        {/* Trust Chains */}

        <div className="mt-12">

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

        {/* Audit Events */}

        <div className="mt-12">

          <h2 className="text-2xl font-bold mb-4">
            Recent Audit Events
          </h2>

          <div className="space-y-4">

            {auditEvents.map((event) => (

              <AuditEventCard
                key={event.event_id}
                action={event.action}
                status={event.status}
                timestamp={event.timestamp}
              />

            ))}

          </div>

        </div>

      </div>

    </Layout>

  );
}

export default Dashboard;