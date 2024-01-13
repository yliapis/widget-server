import React, { useState, useEffect } from 'react';

import logo from './logo.svg';
import './App.css';

const BASE_URL = "http://localhost:8000"

interface Widget {
  id: string;
  name: string;
}

const widgetCell = (widget: Widget, renderList: () => void) => {
  const deleteCallback = () => {
    fetch(BASE_URL + "/widgets/delete", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "id": widget.id,
      }),
    })
      .then(renderList);
  }
  return (
    <tr key={widget.id}>
      <th scope="row" style={{ fontSize: 17 }}>{widget.id}</th>
      <td style={{ fontSize: 17 }}>{widget.name}</td>
      <td style={{ fontSize: 17 }}><button onClick={deleteCallback}>Delete</button></td>
    </tr>
  );
};

function CreateWidgetInputForm() {
  const [widgetName, setWidgetName] = useState('');
  const [widgets, setWidgets] = useState<Widget[]>([]);

  const renderList = () => {
    fetch(BASE_URL + "/widgets")
      .then(response => response.json())
      .then(data => setWidgets(data.widgets));
  };

  useEffect(renderList, []);

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
      <h1>Widget List</h1>
      <span style={{ display: 'flex', justifyContent: 'center' }}>
        <input type="text" value={widgetName} onChange={(e) => setWidgetName(e.target.value)} style={{ flex: '1 0 auto' }} />
        <input type="submit" value="Create Widget" onClick={clickHandler} style={{ marginLeft: '10px' }} />
      </span>
      <table className="table">
        <thead>
          <tr>
            <th style={{ fontSize: 32, fontWeight: 'bold' }} scope="col">ID</th>
            <th style={{ fontSize: 32, fontWeight: 'bold' }} scope="col">Name</th>
            <th style={{ fontSize: 32, fontWeight: 'bold' }} scope="col"/>
          </tr>
        </thead>
        <tbody>
          {widgets.map((widget) => widgetCell(widget, renderList))}
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
