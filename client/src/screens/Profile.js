import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router';
import '../css/profile.css'
import Modal from 'react-modal'

const Profile = () => {
    const token = 0

    const [ifno, setInfo] = useState({})
    const [carInfo, setCarInfo] = useState([
        {
            id: 0,
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
        {
            id: 1,
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
        {
            id: 2,
            name: 'ersr sersr ser',
            year: 2010,
            date: '19 jokoj, 2020 ijsdf'
        },
    ])
    const [openModal, setOpenModal] = useState(false)
    const [currentCar, setCurrentCar] = useState(0)

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
                        <div onClick={() => {
                            setCurrentCar(elem)
                            setOpenModal(true)
                        }} className='car__card' key={elem.id}>
                            {/* <div onClick={() => navigate(`/car/${elem.id}`, { replace: true })} className='car__card' key={elem.id}> */}
                            <h2>{elem.name}</h2>
                            <p>{elem.year}</p>
                            <p>{elem.date}</p>
                        </div>
                    ))
                }
            </div>
            <Modal
                isOpen={openModal}
                // onAfterOpen={afterOpenModal}
                // onRequestClose={closeModal}
                className='car__modal'
                contentLabel="Example Modal"
            >
                {/* <h2 ref={(_subtitle) => (subtitle = _subtitle)}>Hello</h2> */}
                <button className='modal__btn' onClick={() => setOpenModal(false)}>close</button>
                <div className='modal_car_info'>
                    <h2>{currentCar.name}</h2>
                    <p>{currentCar.year}</p>
                    <p>{currentCar.date}</p>
                </div>
            </Modal>
        </div>
    )

}

export default Profile