import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import '../css/dillers.css'

const Dillers = () => {

    const [search, setSearch] = useState('')
    const [dillers, setDillers] = useState('')

    const searchDillers = () => {



    }

    const getDillers = async () => {

        await fetch('')
        .then(res => res.json())
        .then(res => setDillers(res))

    }

    useEffect(() => {
        getDillers()
    }, [])


    return (
        <div className='container dillers'>
            <div className="search">
                <h2>Список диллеров</h2>
                <input value={search} onClick={searchDillers} onChange={e => setSearch(e.target.value)} type="text" placeholder='Поиск' />
            </div>
            <div>
                <h2>Фильтр</h2>
            </div>
            <div className="filter">
                <input type="text" placeholder='поле'/>
                <input type="text" placeholder='поле'/>
                <input type="text" placeholder='поле'/>
            </div>
            <div className="table">
                <table>
                    <thead>
                        <tr>
                            <th><Link to='/diller/1'>Имя</Link></th>
                            <th>Имя</th>
                            <th>Имя</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>имя</td>
                            <td>имя</td>
                            <td>имя</td>
                        </tr>
                        <tr>
                            <td>имя</td>
                            <td>имя</td>
                            <td>имя</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )

}

export default Dillers