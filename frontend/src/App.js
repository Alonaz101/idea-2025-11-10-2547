import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [mood, setMood] = useState('');
  const [recipes, setRecipes] = useState([]);

  const handleMoodChange = (e) => {
    setMood(e.target.value);
  };

  const submitMood = async () => {
    try {
      // For demo, token is hardcoded or should be obtained via login flow
      const token = 'dummy-jwt-token';
      await axios.post('/submit_mood', { mood }, { headers: { Authorization: `Bearer ${token}` } });
      const res = await axios.get(`/recipes?mood=${mood}`, { headers: { Authorization: `Bearer ${token}` } });
      setRecipes(res.data.recipes);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Mood-based Recipe Recommendation</h1>
      <input type="text" value={mood} onChange={handleMoodChange} placeholder="Enter your mood" />
      <button onClick={submitMood}>Get Recipes</button>
      <ul>
        {recipes.map((recipe, index) => (
          <li key={index}>{recipe}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
