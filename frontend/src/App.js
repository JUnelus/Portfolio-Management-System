import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [portfolios, setPortfolios] = useState([]);

  // Fetch portfolios from the Flask API
  useEffect(() => {
    axios.get('http://localhost:5000/portfolio')  // Ensure the URL points to your Flask backend
      .then(response => {
        setPortfolios(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the portfolios!", error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Portfolio Management System</h1>
        <ul>
          {portfolios.map(portfolio => (
            <li key={portfolio._id}>
              <strong>{portfolio.name}</strong> - Assets: {portfolio.assets.join(', ')}
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
