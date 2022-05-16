import React, {useEffect, useState} from 'react';

// React Notification
import {NotificationManager} from 'react-notifications';

import '../css/auth.css';
import config from '../config.json'

const Auth = () => {

    const [isAuth, setIsAuth] = useState(true)
    const [login, setLogin] = useState('')
    const [pass, setPass] = useState('')
    const [secPass, setSecPass] = useState('')
    const [balance, setBalance] = useState(0)
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')

    const request = async () => {

        if (isAuth) {

            console.log('auth', login, pass)
            try {
                await fetch(`${config.url}api/auth/token/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: login,
                        password: pass,
                    })
                })
                    .then(res => res.json())
                    .then(res => {
                        console.log(res)
                        if (res.access) {
                            NotificationManager.success('Успешно авторизованы!', 'Успешно!', 2000);
                            localStorage.setItem('token', res.access)
                            window.location.href = '/'
                        } else {
                            NotificationManager.error('Неверный логин или пароль ', 'Ошибка', 4000)
                        }
                    })
            } catch (error) {
                NotificationManager.error('Ошибка', 'Ошибка!', 404)
                console.log(error)
            }

        } else {

            console.log('registr')

            try {
                await fetch(`${config.url}api/auth/register/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: login,
                        password: pass,
                        balance: balance,
                        first_name: name,
                        last_name: '',
                        email: email,
                    })
                })
                    .then(res => {
                        console.log(res)
                        if (res.ok) {
                            setIsAuth(true)
                            NotificationManager.success('Регистрация прошла успешно!', 'Успешно!', 2000);
                        } else {
                            NotificationManager.error('Такой логин уже существует ', 'Ошибка', 4000)
                        }
                    })
            } catch (err) {
                console.log(err)
            }
        }
    }

    return (
        <div className='auth flex'>
            <h2>{isAuth ? 'Авторизируйтесь' : 'Зарегистрируйтесь'}</h2>
            <div className='form flex'>
                <input type="text" placeholder='Введите логин' onChange={(e) => setLogin(e.target.value)}/>
                <input type="password" placeholder='Введите пароль' onChange={(e) => setPass(e.target.value)}/>
                {
                    !isAuth &&
                    <input type="text" placeholder='Введите ваше имя' onChange={(e) => setName(e.target.value)}/>
                }
                {
                    !isAuth &&
                    <input type="password" placeholder='Повторие пароль' onChange={(e) => setSecPass(e.target.value)}/>
                }
                {
                    !isAuth &&
                    <input type="email" placeholder='Email' onChange={(e) => setEmail(e.target.value)}/>
                }
            </div>
            <div onClick={() => request()} className='btn'>{isAuth ? 'Войти' : 'Зарегистрироваться'}</div>
            {
                isAuth ?
                    <span>Создать аккаунт? <span className='registr' onClick={() => setIsAuth(false)}>Регистрация</span></span> :
                    <span>Есть аккаунт аккаунт? <span className='registr'
                                                      onClick={() => setIsAuth(true)}>Войти</span></span>
            }
        </div>
    )

}

export default Auth