import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router';
import '../css/profile.css'
import Modal from 'react-modal'
import config from '../config.json'

const Profile = (props) => {

    const [userInfo, setUserInfo] = useState([])
    const [offers, setOffers] = useState([])
    const [currentCar, setCurrentCar] = useState(null)
    const [currentCarDate, setCurrentCarDate] = useState('')
    const [email, setEmail] = useState('')
    const [openModal, setOpenModal] = useState(false)
    const [error, setError] = useState('')

    const navigate = useNavigate()

    const getOffer = async (_id) => {

        await fetch(`${config.url}api/offer/`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
            .then(res => res.json())
            .then(res => {
                let offersBuf = []

                res.map(elem => {
                    console.log(elem)
                    if (elem?.profile?.id == _id) {
                        offersBuf.push(elem)
                    }
                })

                setOffers(offersBuf)
            })

    }

    const updateUserInfo = async () => {

        if (email != '') {
            console.log({
                currency: 'USD',
                user: {
                    username: userInfo.user.username,
                    first_name: userInfo.user.first_name,
                    last_name: userInfo.user.last_name,
                    email: email
                }
            })

            console.log(userInfo)

            try {
                await fetch(`${config.url}api/auth/profile/${userInfo.user.id}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + props.token,
                    },
                    body: JSON.stringify({
                        currency: 'USD',
                        user: {
                            username: userInfo.user.username,
                            first_name: userInfo.user.first_name,
                            last_name: userInfo.user.last_name,
                            email: email
                        }
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
        let _id

        await fetch(`${config.url}api/auth/profile/`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
            .then(res => res.json())
            .then(res => {
                _id = res[0].id
                setUserInfo(res[0])
            })

        await getOffer(_id)

        console.log('complete')

    }

    useEffect(() => {
        getUserInfo()
    }, [])

    return (
        <div className='container'>
            <h2>Профиль</h2>
            <div className='info'>
                <div className='row'>

                    <div className='col'>
                        <span>Логин</span>
                        <p>{userInfo?.user?.username}</p>
                    </div>
                    <div className='col'>
                        <span>Имя</span>
                        <p>{userInfo?.user?.first_name + ' ' + userInfo?.user?.last_name}</p>
                    </div>
                    <div className='col'>
                        <span>Баланс</span>
                        <p>{userInfo?.balance} {userInfo?.currency}</p>
                    </div>
                    <div className='col'>
                        <span>email</span>
                        {/*userInfo?.user?.email*/}
                        <p>{userInfo?.user?.email}</p>
                        {/*<input type="text" placeholder='email' onChange={e => setEmail(e.target.value)} />*/}
                    </div>
                </div>
                {/*{*/}
                {/*    !userInfo?.user?.email &&*/}
                {/*    <div className='btn' onClick={() => updateUserInfo()} style={{width: '30%', textAlign: 'center', marginLeft: 'auto', marginRight: 'auto'}}>Сохранить</div>*/}
                {/*}*/}
            </div>
            <h3 style={{fontSize: 24}}>Мои заказы:</h3>
            <div className='cars'>
                {
                    offers?.length > 0 && offers.map(elem => (
                        <div onClick={() => {
                            setCurrentCar(elem)
                            setCurrentCarDate(new Date(elem.updated_at))
                            // console.log(new Date(elem.updated_at))
                            setOpenModal(true)
                        }} className='car__card' key={elem.car.id}>
                            {/* <div onClick={() => navigate(`/car/${elem.id}`, { replace: true })} className='car__card' key={elem.id}> */}
                            <h2 style={{textAlign: 'center'}}>{elem.car.car.brand + ' ' + elem.car.car.model}</h2>
                            <p>Год выпуска: {elem.car.car.release_year}</p>
                            <p>Привод: {elem.car.car.drive}</p>
                            <p>Управление: {elem.car.car.transmission}</p>
                            <p>Стоимость: {elem.car.price} {elem.car.currency}</p>
                            <p>Статус: {elem.status}</p>
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
                <button className='modal__btn' onClick={() => setOpenModal(false)}>close</button>
                <div className='modal_car_info'>
                    {
                        currentCar &&
                        <>
                            <h2>{currentCar.car.car.brand + ' ' + currentCar.car.car.model}</h2>
                            <p>Дилер: {currentCar.dealer.name}</p>
                            <p>Статус заказа: {currentCar.status}</p>
                            <p>Дата
                                заказа: {currentCarDate.getDate()}:{currentCarDate.getMonth() + 1}:{currentCarDate.getFullYear()}</p>
                        </>
                    }
                </div>
            </Modal>
        </div>
    )

}

export default Profile