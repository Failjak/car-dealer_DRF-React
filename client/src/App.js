import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Auth from "./screens/Auth";
import Car from "./screens/Car";
import Profile from "./screens/Profile";

const App = () => {
  return (
    <Router>
      <div>
        {/* <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/auth">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav> */}

        <Routes>
          <Route path="/auth" element={<Auth />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/car/:id" element={<Car />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
