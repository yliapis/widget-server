import React, { useState, useEffect } from 'react';

import logo from './logo.svg';
import './App.css';

const BASE_URL = "http://localhost:8000"

interface Widget {
  id: string;
  name: string;
}

function CreateWidgetInputForm() {
  const [widgetName, setWidgetName] = useState('');
  const [widgets, setWidgets] = useState<Widget[]>([]);

  useEffect(() => {
    fetch(BASE_URL + "/widgets")
      .then(response => response.json())
      .then(data => setWidgets(data.widgets));
  }, []);

  const clickHandler = () => {
    console.log(widgetName);
    fetch(BASE_URL + "/widgets/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "name": widgetName
      })
    })
      .then(() => {
        // Refresh the list of widgets after successful submission
        fetch(BASE_URL + "/widgets")
          .then(response => response.json())
          .then(data => setWidgets(data.widgets));
      });
  };

  return (
    <div>
      <span>
        <input type="text" id="fname" name="fname" value={widgetName} onChange={(e) => setWidgetName(e.target.value)} />
        <input type="submit" value="Create Widget" onClick={clickHandler} />
      </span>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {widgets.map(widget => (
            <tr key={widget.id}>
              <td>{widget.id}</td>
              <td>{widget.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}


function App() {
  return (
    <div className="App">
      <header className="App-header">
      <CreateWidgetInputForm />
      </header>
    </div>
  );
}

export default App;
