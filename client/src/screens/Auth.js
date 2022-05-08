import React, { useEffect, useState } from 'react';
import '../css/auth.css';

const Auth = () => {

    const [isAuth, setIsAuth] = useState(true)
    const [login, setLogin] = useState('')
    const [pass, setPass] = useState('')
    const [secPass, setSecPass] = useState('')
    const [balance, setBalance] = useState(0)
    const [name, setName] = useState('')

    const request = async () => {

        if (isAuth) {

            console.log('auth', login, pass)
            try {
                await fetch('http://127.0.0.1:8000/api/auth/token/', {
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
                        // if (res.ok) {
                            localStorage.setItem('token', res.access)
                            window.location.href = '/'
                        // }
                    })
            } catch (error) {
                console.log(error)
            }

        }
        else {

            console.log('registr')

            try {
                await fetch('http://127.0.0.1:8000/api/auth/register/', {
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
                    })
                })
                    .then(res => {
                        // if (res) {
                            console.log(res)
                            setIsAuth(true)
                        // }
                    })
            }
            catch (err) {
                console.log(err)
            }

        }

    }

    return (
        <div className='auth flex'>
            <h2>{isAuth ? 'Авторизируйтесь' : 'Зарегистрируйтесь'}</h2>
            <div className='form flex'>
                <input type="text" placeholder='Введите логин' onChange={(e) => setLogin(e.target.value)} />
                <input type="text" placeholder='Введите ваше имя' onChange={(e) => setName(e.target.value)} />
                <input type="text" placeholder='Введите ваш баланс' onChange={(e) => setBalance(e.target.value)} />
                <input type="password" placeholder='Введите пароль' onChange={(e) => setPass(e.target.value)} />
                {
                    !isAuth && <input type="password" placeholder='Повторие пароль' onChange={(e) => setSecPass(e.target.value)} />
                }
            </div>
            <div onClick={() => request()} className='btn'>{isAuth ? 'Войти' : 'Зарегистрироваться'}</div>
            {
                isAuth ?
                    <span>Создать аккаунт? <span className='registr' onClick={() => setIsAuth(false)}>Регистрация</span></span> :
                    <span>Есть аккаунт аккаунт? <span className='registr' onClick={() => setIsAuth(true)}>Войти</span></span>
            }
        </div>
    )

}

export default Auth