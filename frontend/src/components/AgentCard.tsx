type Props = {
  agent_id: string;
  name: string;
  role: string;
};

function AgentCard({
  agent_id,
  name,
  role,
}: Props) {
  return (
    <div className="bg-white p-5 rounded-lg shadow">

      <h3 className="text-xl font-bold">
        {name}
      </h3>

      <p className="mt-2 text-gray-600">
        Role: {role}
      </p>

      <p className="mt-2 text-sm text-gray-500 break-all">
        ID: {agent_id}
      </p>

    </div>
  );
}

export default AgentCard;