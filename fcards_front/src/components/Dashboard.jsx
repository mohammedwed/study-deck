 import React, { useState, useEffect } from "react";
import API from "../api/api";

 function Dashboard() {
    const [decks, setDecks] = useState([]);

    // Placeholder for fetching decks later
    useEffect(() => {
    // Will fetch decks on Day 2
    }, []);


   return (
    <div>
      <h2>Dashboard</h2>
      <p>Your decks will appear here.</p>
      <ul>
        {decks.map((deck) => (
          <li key={deck.id}>{deck.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard