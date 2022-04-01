import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router';
import '../css/profile.css'

const Profile = () => {
    const token = 0

    const [ifno, setInfo] = useState({})
    const [carInfo, setCarInfo] = useState([
        {
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
        {
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
        {
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
    ])

    const navigate = useNavigate()

    const getProfile = async () => {

        await fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                token: token
            })
        })
            .then(res => res.json())
            .then(res => console.log(res)) // записать токен, проврить всё ли OK и потом redirect

    }

    const getCars = async () => {

        await fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                token: token
            })
        })
            .then(res => res.json())
            .then(res => console.log(res)) // записать токен, проврить всё ли OK и потом redirect

    }

    useEffect(() => {
        // getProfile()
        // getCars()
    }, [])

    return (
        <div className='container'>
            <h2>Профиль</h2>
            <div className='info'>
                <div className='row'>
                    <div className='col'>
                        <span>ФИО</span>
                        <p>Зубенко Михаил Петрович</p>
                    </div>
                    <div className='col'>
                        <span>Возраст</span>
                        <p>12</p>
                    </div>
                    <div className='col'>
                        <span>Пол</span>
                        <p>Мужской</p>
                    </div>
                    <div className='col'>
                        <span>Поле</span>
                        <p>Какой-то текст</p>
                    </div>
                </div>
                <div className='row'>
                    <div className='col'>
                        <span>ФИО</span>
                        <p>Зубенко Михаил Петрович</p>
                    </div>
                    <div className='col'>
                        <span>Возраст</span>
                        <p>12</p>
                    </div>
                    <div className='col'>
                        <span>Пол</span>
                        <p>Мужской</p>
                    </div>
                    <div className='col'>
                        <span>Поле</span>
                        <p>Какой-то текст</p>
                    </div>
                </div>
            </div>
            <div className='cars'>
                {
                    carInfo.map(elem => (
                        <div onClick={() => navigate(`/car_info?id=${elem.id}`, { replace: true })} className='car__card' key={elem.id}>
                            <h2>{elem.name}</h2>
                            <p>{elem.year}</p>
                            <p>{elem.date}</p>
                        </div>
                    ))
                }
            </div>
        </div>
    )

}

export default Profile