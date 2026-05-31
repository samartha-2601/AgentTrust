type Props = {
  finding: string;
  research_agent: string;
  review_agent: string;
  security_agent: string;
  chain_valid: boolean;
};

function TrustChainCard({
  finding,
  research_agent,
  review_agent,
  security_agent,
  chain_valid,
}: Props) {
  return (
    <div className="bg-white p-5 rounded-lg shadow">

      <h3 className="font-bold text-lg">
        {finding}
      </h3>

      <p className="mt-2 text-gray-600">
        {research_agent}
        {" → "}
        {review_agent}
        {" → "}
        {security_agent}
      </p>

      <div className="mt-3">

        <span
          className={
            chain_valid
              ? "text-green-600 font-semibold"
              : "text-red-600 font-semibold"
          }
        >
          {chain_valid
            ? "VALID"
            : "INVALID"}
        </span>

      </div>

    </div>
  );
}

export default TrustChainCard;