import { useEffect, useState } from "react";

const API = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const load = () => fetch(`${API}/tasks/`).then(r => r.json()).then(setTasks);
  useEffect(() => { load(); }, []);

  const add = async (e) => {
    e.preventDefault();
    await fetch(`${API}/tasks/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });
    setTitle(""); load();
  };

  const toggle = async (t) => {
    await fetch(`${API}/tasks/${t.id}/`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ done: !t.done }),
    });
    load();
  };

  return (
    <main>
      <h1>TaskFlow</h1>
      <form onSubmit={add}>
        <input value={title} onChange={e => setTitle(e.target.value)} required />
        <button>Ajouter</button>
      </form>
      <ul>
        {tasks.map(t => (
          <li key={t.id} onClick={() => toggle(t)}
              style={{ textDecoration: t.done ? "line-through" : "none", cursor: "pointer" }}>
            {t.title}
          </li>
        ))}
      </ul>
    </main>
  );
}