import { Link, useLocation } from "react-router-dom";

type LayoutProps = {
  children: React.ReactNode;
};

function Layout({ children }: LayoutProps) {

  const location = useLocation();

  const navItems = [
    {
      name: "Dashboard",
      path: "/dashboard",
    },
    {
      name: "Agents",
      path: "/agents",
    },
    {
      name: "Trust Chains",
      path: "/trust-chains",
    },
    {
      name: "Audit Logs",
      path: "/audit-logs",
    },
  ];

  return (
    <div className="flex min-h-screen bg-gray-100">

      <aside className="w-64 bg-slate-900 text-white">

        <div className="p-6 border-b border-slate-700">

          <h1 className="text-2xl font-bold">
            AgentTrust
          </h1>

          <p className="text-sm text-slate-400 mt-1">
            AI Trust Platform
          </p>

        </div>

        <nav className="p-4">

          <ul className="space-y-2">

            {navItems.map((item) => (

              <li key={item.path}>

                <Link
                  to={item.path}
                  className={`block px-4 py-2 rounded ${
                    location.pathname === item.path
                      ? "bg-slate-700"
                      : "hover:bg-slate-800"
                  }`}
                >
                  {item.name}
                </Link>

              </li>

            ))}

          </ul>

        </nav>

      </aside>

      <main className="flex-1">
        {children}
      </main>

    </div>
  );
}

export default Layout;