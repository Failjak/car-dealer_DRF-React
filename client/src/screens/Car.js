import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

const Car = () => {

    const {id} = useParams()
    
    // const [token, setToken] = useState(localStorage.getItem('token'))a
    const [carInfo, setCarInfo] = useState([])

    const getCarInfo = async () => {

        await fetch('', {
            headers: {
                'Content-Type': 'Application/json',
                'Authorization': 'Bearer' + token
            }
        })
        .then(res => res.json())
        .then(res => setCarInfo(res))

    }

    useEffect(() => {

        getCarInfo()
        
    }, [id])


    return(
        <div>
            car {id}
        </div>
    )

}

export default Car