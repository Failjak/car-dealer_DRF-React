import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router';
import '../css/profile.css'

const Profile = (props) => {

    const [userInfo, setUserInfo] = useState([])
    const [carInfo, setCarInfo] = useState([])
    const [currentCar, setCurrentCar] = useState(0)
    const [email, setEmail] = useState('')

    const navigate = useNavigate()

    const getCarInfo = async () => {

        await fetch('http://127.0.0.1:8000/api/auth/profile/car/', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => setCarInfo(res[0]))

    }

    const updateUserInfo = async () => {

        if (email != '') {

            console.log({
                ...userInfo.user,
                email: email
            })

            try {
                await fetch(`http://127.0.0.1:8000/api/auth/profile/${userInfo.user.id}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + props.token,
                    },
                    body: JSON.stringify({
                        ...userInfo.user,
                        email: email
                    })
                })
                .then(res => res.json())
                .then(res => console.log(res))
            } catch (error) {
                console.log(error)
            }

            await getUserInfo()

        }
        
    }

    const getUserInfo = async () => {

        console.log('fetch')

        await fetch('http://127.0.0.1:8000/api/auth/profile/', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => setUserInfo(res[0]))
        
        await getCarInfo()

        console.log('complete')
        
    }

    useEffect(() => {
        getUserInfo()
        console.log('useff')
    }, [])

    return (
        <div className='container'>
            <h2>Профиль</h2>
            <div className='info'>
                <div className='row'>
                    <div className='col'>
                        <span>email</span>
                        {
                            userInfo?.user?.email ?
                            <p>{userInfo?.user?.email}</p> :
                            <input type="text" placeholder='email' onChange={e => setEmail(e.target.value)} />
                        }
                    </div>
                    <div className='col'>
                        <span>Баланс</span>
                        <p>{userInfo?.balance}</p>
                    </div>
                    <div className='col'>
                        <span>Имя</span>
                        <p>{userInfo?.user?.first_name + ' ' + userInfo?.user?.last_name}</p>
                    </div>
                    <div className='col'>
                        <span>Логин</span>
                        <p>{userInfo?.user?.username}</p>
                    </div>
                </div>
                {
                    !userInfo?.user?.email &&
                    <div className='btn' onClick={() => updateUserInfo()} style={{width: '30%', textAlign: 'center', marginLeft: 'auto', marginRight: 'auto'}}>Сохранить</div>
                }
            </div>
            <h3 style={{ fontSize: 24 }}>Мои машины:</h3>
            <div className='cars'>
                {
                    carInfo?.length > 0 && carInfo.map(elem => (
                        <div onClick={() => {
                            setCurrentCar(elem)
                        }} className='car__card' key={elem.id}>
                            {/* <div onClick={() => navigate(`/car/${elem.id}`, { replace: true })} className='car__card' key={elem.id}> */}
                            <h2 style={{ textAlign: 'center' }}>{elem.brand + ' ' + elem.model + 'dfdfdfdffdfdf'}</h2>
                            <p>{elem.release_year}</p>
                            <p>{elem.drive}</p>
                            <p>{elem.transmission}</p>
                        </div>
                    ))
                }
            </div>
            {/* <Modal
                isOpen={openModal}
                // onAfterOpen={afterOpenModal}
                // onRequestClose={closeModal}
                className='car__modal'
                contentLabel="Example Modal"
            >
                <button className='modal__btn' onClick={() => setOpenModal(false)}>close</button>
                <div className='modal_car_info'>
                    <h2>{currentCar.name}</h2>
                    <p>{currentCar.year}</p>
                    <p>{currentCar.date}</p>
                </div>
            </Modal> */}
        </div>
    )

}

export default Profile