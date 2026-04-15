import React from "react";
import { createRoot } from "react-dom/client";
import { DashboardShell } from "./pages/DashboardShell";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <DashboardShell />
  </React.StrictMode>
);
