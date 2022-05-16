import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import '../css/dillers.css'
import config from '../config.json'

const Dealers = (props) => {

    const [search, setSearch] = useState('')
    const [dealers, setDealers] = useState([])
    const [allStats, setAllStats] = useState([])

    const getStatistic = async () => {

        await fetch(`${config.url}api/dealer/statistic/`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => {
            console.log(res)
            setAllStats(res)
        })

    }

    const getDealers = async () => {

        await fetch(`${config.url}api/dealer`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + props.token,
            },
        })
        .then(res => res.json())
        .then(res => setDealers(res))

    }

    const getUrlParam = (currentDealer) => {
        return{
            pathname: `/dealers/${currentDealer.id}`,
        }
    }

    useEffect(() => {
        getDealers()
        getStatistic()
    }, [])


    return (
        <div className='container dillers'>
            <div className="search">
                <h2>Список диллеров</h2>
                <input value={search} onChange={e => setSearch(e.target.value)} type="text" placeholder='Поиск' />
            </div>
            <div>
                <h2>Фильтр</h2>
            </div>
            <div className="filter">
                <input type="text" placeholder='имя'/>
                <input type="text" placeholder='страна'/>
                <input type="text" placeholder='город'/>
            </div>
            <div className="table">
                <table>
                    <thead>
                        <tr>
                            <th>Имя</th>
                            <th>Страна</th>
                            <th>Город</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            dealers.map(elem => (
                                <tr key={elem.id}>
                                    <td>
                                        <Link to={getUrlParam(elem)} >{elem.name}</Link>
                                        </td>
                                    <td>{elem?.address?.country}</td>
                                    <td>{elem?.address?.city}</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
            <div style={{marginTop: 100}}>
                <h2>Статистика всех дилеров</h2>
            </div>
            <div className="table">
                <table style={{marginBottom: 50}}>
                    <thead>
                        <tr>
                            <th>Имя дилера</th>
                            <th>Средняя стоимость машин</th>
                            <th>Максимальная стоимость машины</th>
                            <th>популярная модель</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            allStats.length > 0 && allStats.map(elem => (
                                <tr key={elem.id}>
                                    <td>{elem.name}</td>
                                    <td>{elem.avg_car_price}</td>
                                    <td>{elem.max_car_price}</td>
                                    <td>{elem?.most_popular_car?.brand + ' ' + elem?.most_popular_car?.model}</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
        </div>
    )

}

export default Dealers