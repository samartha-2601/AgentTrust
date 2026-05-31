import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import AgentCard from "../components/AgentCard";
import api from "../services/api";

function Agents() {

  const [agents, setAgents] =
    useState<any[]>([]);

  useEffect(() => {
    loadAgents();
  }, []);

  const loadAgents = async () => {

    try {

      const response =
        await api.get("/agents");

      setAgents(
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
          Agents
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

          {agents.map((agent) => (

            <AgentCard
              key={agent.agent_id}
              agent_id={agent.agent_id}
              name={agent.name}
              role={agent.role}
            />

          ))}

        </div>

      </div>

    </Layout>

  );
}

export default Agents;