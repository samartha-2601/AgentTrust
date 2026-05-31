type Props = {
  action: string;
  status: string;
  timestamp: string;
};

function AuditLogCard({
  action,
  status,
  timestamp,
}: Props) {

  const formattedDate =
    new Date(timestamp).toLocaleString();

  return (
    <div className="bg-white p-5 rounded-lg shadow">

      <h3 className="font-bold text-lg">
        {action}
      </h3>

      <p className="text-gray-500 mt-2">
        {formattedDate}
      </p>

      <div className="mt-3">

        <span
          className={
            status === "allowed"
              ? "text-green-600 font-semibold"
              : "text-red-600 font-semibold"
          }
        >
          {status.toUpperCase()}
        </span>

      </div>

    </div>
  );
}

export default AuditLogCard;