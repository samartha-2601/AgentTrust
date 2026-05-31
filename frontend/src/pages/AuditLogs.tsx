import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import AuditLogCard from "../components/AuditLogCard";
import api from "../services/api";

function AuditLogs() {

  const [logs, setLogs] =
    useState<any[]>([]);

  const [filter, setFilter] =
    useState("all");

  useEffect(() => {
    loadLogs();
  }, []);

  const loadLogs = async () => {

    try {

      const response =
        await api.get("/audit/logs");

      setLogs(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  const filteredLogs =
    logs.filter((log) => {

      if (filter === "all")
        return true;

      return log.status === filter;

    });

  return (

    <Layout>

      <div className="p-8">

        <h1 className="text-4xl font-bold mb-8">
          Audit Logs
        </h1>

        <div className="mb-6">

          <select
            value={filter}
            onChange={(e) =>
              setFilter(
                e.target.value
              )
            }
            className="bg-white border rounded p-2"
          >

            <option value="all">
              All
            </option>

            <option value="allowed">
              Allowed
            </option>

            <option value="denied">
              Denied
            </option>

          </select>

        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {filteredLogs.map((log) => (

            <AuditLogCard
              key={log.event_id}
              action={log.action}
              status={log.status}
              timestamp={log.timestamp}
            />

          ))}

        </div>

      </div>

    </Layout>

  );
}

export default AuditLogs;