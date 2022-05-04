import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Auth from "./screens/Auth";
import Car from "./screens/Car";
import Profile from "./screens/Profile";
import Dealers from "./screens/Dealers";
import Dealer from "./screens/Dealer";

const App = () => {

  const [token, setToken] = useState('')

  useEffect(() => {
    setToken(localStorage.getItem('token') || null)
    console.log(localStorage.getItem('token'), token)
  }, [localStorage])

  return (
    <>
      {
        token ?
          <Router>
            <div className="main__container">
              <nav>
                <ul>
                  <li>
                    <Link to="/">Профиль</Link>
                  </li>
                  <li>
                    <Link to="/dealers">Список диллеров</Link>
                  </li>
                  <li >
                    <Link to="/users">Выход</Link>
                  </li>
                </ul>
              </nav>

              <Routes>
                <Route path="/" element={<Profile token={token} />} />
                <Route path="/dealers" element={<Dealers token={token} />} />
                <Route path="/dealers/:id" element={<Dealer token={token} />} />
                <Route path="/login" element={<Auth />} />
              </Routes>
            </div>
          </Router> :
          <Auth />
      }

    </>
  );
}

export default App;
