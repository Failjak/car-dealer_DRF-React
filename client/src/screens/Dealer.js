import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import config from '../config.json'

const Diller = (props) => {


    const {id} = useParams()
    
    const [dealer, setDealer] = useState({})
    const [dealerCars, setDealerCars] = useState([])
    const [carPrice, setCarPrice] = useState([])
    const [currentCar, setCurrentCar] = useState([])
    const [userInfo, setUserInfo] = useState()
    const [dealerStats, setDealerStats] = useState([])
    const [error, setError] = useState('')

    const getStats = async (name) => {

        await fetch(`${config.url}api/dealer/statistic/`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => {
            const current = res.filter(elem => elem.name == name)
            console.log("Statistic:" + current)
            setDealerStats(current)
        })

    }

    const getDealer = async () => {

        let dealerName

        await fetch(`${config.url}api/dealer/${id}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => {
            setDealer(res)
            dealerName = res.name
            setDealerCars(res.car_prices)
            console.log(res)
        })

        await getStats(dealerName)

    }

    const buyCar = async (id) => {

        try {
            await fetch(`${config.url}api/offer/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
            body: JSON.stringify({
                dealer: dealer.id,
                car: id,
                profile: userInfo.id
            })
        })
        .then(res => res.json())
        .then(res => {
            console.log(res)
        })
        } catch (error) {
            alert(error.message)
        }

    }

    const getUserInfo = async () => {

        console.log('fetch')

        await fetch(`${config.url}api/auth/profile/`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => setUserInfo(res[0]))

        await getDealer()
        
        console.log('complete')
        
    }

    useEffect(() => {
        getUserInfo()
    }, [])

    return (
        <div className="container">
            <h2>Профиль диллера</h2>
            <div className="diller__body">
                <div className="info">
                    <div className='row'>
                        <div className='col'>
                            <span>Имя</span>
                            <p>{dealer?.name}</p>
                        </div>
                        <div className='col'>
                            <span>Страна</span>
                            <p>{dealer?.address?.country}</p>
                        </div>
                        <div className='col'>
                            <span>Город</span>
                            <p>{dealer?.address?.city}</p>
                        </div>
                        <div className='col'>
                            <span>Улица</span>
                            <p>{dealer?.address?.street + ' ' + dealer?.address?.building}</p>
                        </div>
                    </div>
                </div>
            </div>
            <h3 style={{ fontSize: 24 }}>Предложения дилера:</h3>
            <div className='cars'>
                {
                    dealerCars?.length > 0 && dealerCars.map(elem => (
                        <div onClick={() => {
                            setCurrentCar(elem)
                        }} className='car__card' key={elem.id}>
                            <h2 style={{ textAlign: 'center' }}>{elem.car.brand + ' ' + elem.car.model + ' ' + elem.car.release_year}</h2>
                            <p>{elem.price + ' ' + elem.currency}</p>
                            <p>{elem.car.drive}</p>
                            <p>{elem.car.transmission}</p>
                            <div className="btn" onClick={() => buyCar(elem.id)}>Купить</div>
                        </div>
                    ))
                }
            </div>
            <h3 style={{ fontSize: 24 }}>Статистика дилера:</h3>
            <div className='cars'>
                {
                    dealerStats?.length > 0 && dealerStats.map(elem => (
                        <div onClick={() => {
                            // setCurrentCar(elem)
                            console.log('///')
                        }} className='car__card' key={elem.id}>
                            {/* <h2 style={{ textAlign: 'center' }}>{elem.car.brand + ' ' + elem.car.model + ' ' + elem.car.release_year}</h2> */}
                            <p>Средняя цена машин: {elem?.avg_car_price}</p>
                            <p>Максимальная цена машины: {elem?.max_car_price}</p>
                            <p>Самая популярная модель: {elem?.most_popular_car?.brand + ' ' + elem?.most_popular_car?.model}</p>
                        </div>
                    ))
                }
            </div>
        </div>
    )

}

export default Diller