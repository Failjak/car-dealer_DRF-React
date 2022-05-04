import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import '../css/dillers.css'

const Dealers = (props) => {

    const [search, setSearch] = useState('')
    const [dealers, setDealers] = useState([])

    const getDealers = async () => {

        await fetch('http://127.0.0.1:8000/api/dealer', {
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
                                    <td>{elem.address.country}</td>
                                    <td>{elem.address.city}</td>
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