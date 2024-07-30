import React from 'react';
import { createRoot } from 'react-dom/client';

const App = () => {
    return <h1>Rendered by Django, cooked by React</h1>;
};

export default App;

const container = document.getElementById('app');
const root = createRoot(container);
root.render(<App />);