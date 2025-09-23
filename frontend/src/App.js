import React, { useEffect, useState } from 'react';
import { getClients, getKeywords, getRankResults } from './api';

function App() {
  const [clients, setClients] = useState([]);
  const [keywords, setKeywords] = useState([]);
  const [rankResults, setRankResults] = useState([]);

  useEffect(() => {
    getClients().then(setClients);
    getKeywords().then(setKeywords);
    getRankResults().then(setRankResults);
  }, []);

  return (
    <div>
      <h1>RankTracker Dashboard</h1>
      <section>
        <h2>Clients</h2>
        <ul>
          {clients.map(client => <li key={client.id}>{client.name}</li>)}
        </ul>
      </section>
      <section>
        <h2>Keywords</h2>
        <ul>
          {keywords.map(keyword => <li key={keyword.id}>{keyword.name}</li>)}
        </ul>
      </section>
      <section>
        <h2>Rank Results</h2>
        <ul>
          {rankResults.map(rr => (
            <li key={rr.id}>
              {rr.domain} - {rr.keyword.name} - Position: {rr.position} ({rr.checked_at})
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default App;