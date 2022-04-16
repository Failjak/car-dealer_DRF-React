import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Auth from "./screens/Auth";
import Profile from "./screens/Profile";
import Dillers from "./screens/Dillers";
import Diller from "./screens/Diller";

const App = () => {
  return (
    <>
      <Router>
        <div className="main__container">
          <nav>
            <ul>
              <li>
                <Link to="/">Профиль</Link>
              </li>
              <li>
                <Link to="/dillers">Список диллеров</Link>
              </li>
              <li >
                <Link to="/users">Выход</Link>
              </li>
            </ul>
          </nav>
  
          <Routes>
            <Route path="/" element={<Profile />} />
            <Route path="/dillers" element={<Dillers />} />
            <Route path="/diller/:id" element={<Diller />} />
          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
