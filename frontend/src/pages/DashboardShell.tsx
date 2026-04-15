const pages = [
  "Executive Overview",
  "User Adoption",
  "GPT Portfolio",
  "Projects",
  "Impact",
];

export function DashboardShell(): JSX.Element {
  return (
    <main style={{ fontFamily: "Inter, system-ui, sans-serif", margin: "2rem" }}>
      <h1>ChatGPT Enterprise Workspace Analytics</h1>
      <p>Starter dashboard navigation scaffold:</p>
      <ul>
        {pages.map((page) => (
          <li key={page}>{page}</li>
        ))}
      </ul>
    </main>
  );
}
