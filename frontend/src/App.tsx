import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Agents from "./pages/Agents";
import TrustChains from "./pages/TrustChains";
import AuditLogs from "./pages/AuditLogs";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Navigate to="/dashboard" />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/agents"
          element={<Agents />}
        />

        <Route
          path="/trust-chains"
          element={<TrustChains />}
        />

        <Route
          path="/audit-logs"
          element={<AuditLogs />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;