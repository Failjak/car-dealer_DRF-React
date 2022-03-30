import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../css/auth.css';

const Auth = () => {

    let navigate = useNavigate()

    const [isAuth, setIsAuth] = useState(true)
    const [login, setLogin] = useState('')
    const [pass, setPass] = useState('')
    const [secPass, setSecPass] = useState('')

    const request = async () => {

        console.log('request')

        if (isAuth) {

            await fetch('', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({  
                    login: login,
                    password: pass,
                })
            })
            .then(res => res.json())
            .then(res => console.log(res)) // записать токен, проврить всё ли OK и потом redirect
            .then(() => navigate("/profile", { replace: true }))

        }
        else {

            await fetch('', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({  
                    login: login,
                    password: pass,
                    passAgain: secPass
                })
            })
            .then(res => res.json())
            .then(res => console.log(res)) // записать токен, проврить всё ли OK и потом redirect
            .then(() => navigate("/profile", { replace: true }))

        }

    }

    return(
        <div className='auth flex'>
            <h2>{isAuth ? 'Авторизируйтесь' : 'Зарегистрируйтесь'}</h2>
            <div className='form flex'>
                <input type="text" placeholder='Введите логин' onChange={(e) => setLogin(e.target.value)} />
                <input type="text" placeholder='Введите пароль' onChange={(e) => setPass(e.target.value)} />
                {
                    !isAuth && <input type="text" placeholder='Повторие пароль' onChange={(e) => setSecPass(e.target.value)} />
                }
            </div>
            <Link to='/profile' onClick={request()} className='btn'>{isAuth ? 'Войти' : 'Зарегистрироваться'}</Link>
            {
                isAuth ?
                <span>Создать аккаунт? <span className='registr' onClick={() => setIsAuth(false)}>Регистрация</span></span> :
                <span>Есть аккаунт аккаунт? <span className='registr' onClick={() => setIsAuth(true)}>Войти</span></span>
            }
        </div>
    )

}

export default Auth