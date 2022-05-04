import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const Diller = (props) => {

    const {id} = useParams()
    
    const [dealer, setDealer] = useState({})
    const [dealerCars, setDealerCars] = useState([])
    const [carPrice, setCarPrice] = useState([])

    const getCars = async () => {

        await fetch(`http://127.0.0.1:8000/api/car/${id}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => {
            setDealer(res)
            setCarPrice(res.car_prices)
        })

    }

    const getDealer = async () => {

        await fetch(`http://127.0.0.1:8000/api/dealer/${id}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => {
            setDealer(res)
            setCarPrice(res.car_prices)
        })

        

    }

    useEffect(() => {
        getDealer()
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
                            <p>{dealer?.address?.street}</p>
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
                            <h2 style={{ textAlign: 'center' }}>{elem.brand + ' ' + elem.model + 'dfdfdfdffdfdf'}</h2>
                            <p>{elem.release_year}</p>
                            <p>{elem.drive}</p>
                            <p>{elem.transmission}</p>
                        </div>
                    ))
                }
            </div>
        </div>
    )

}

export default Diller