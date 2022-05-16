import React, {useEffect, useState} from "react";
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

// React Notification
import 'react-notifications/lib/notifications.css';
import {NotificationContainer} from 'react-notifications';

const App = () => {

    const [token, setToken] = useState('')

    useEffect(() => {
        setToken(localStorage.getItem('token') || null)
        console.log(localStorage.getItem('token'), token)
    }, [localStorage])

    const logut = () => {
        localStorage.removeItem('token')
        setToken(null)
    }

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
                                    <li onClick={() => logut()}>
                                        <a href="">Выход</a>
                                    </li>
                                </ul>
                            </nav>
                            <Routes>
                                <Route path="/" element={<Profile token={token}/>}/>
                                <Route path="/dealers" element={<Dealers token={token}/>}/>
                                <Route path="/dealers/:id" element={<Dealer token={token}/>}/>
                                {/* <Route path="/login" element={<Auth/>}/> */}
                                {/* <Route path="/logout" element={<Auth/>}/> */}
                            </Routes>
                            <NotificationContainer/>
                        </div>
                    </Router> :
                    <Auth/>
            }
        </>
    );
}

export default App;
