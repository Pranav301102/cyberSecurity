
import './App.css';
import Background from './component/background';
import Home from './component/home';
import Domain from './component/result';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";


function App() {
  return (
    <div className="App">
      <Router>
        <Background/>
          <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/result" element={<Domain />} />
          </Routes>
      </Router>
    </div>
  );
}

export default App;



