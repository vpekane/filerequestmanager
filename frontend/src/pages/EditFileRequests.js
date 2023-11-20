import React, {useEffect, useState} from 'react'
import EditFileRequestItem from '../components/EditFileRequestItem'
import { useParams } from 'react-router-dom';

const EditFileRequests = () => {
    const [requests, setRequests] = useState([]);

    useEffect(() => {
        getRequests()
    }, [])

    let {id} = useParams();

    // let getId = async () => {
    //     let IDs = await fetch('/file-requests/');
    //     // return id in [IDs];
    // }

    let getRequests = async () => {
        let response = await fetch(`/edit-file-request/${id}/`)
        let data = await response.json()

        setRequests(data["files"])
        // console.log("DATAS", data)
    }

  return (
    <div>
        <EditFileRequestItem />
    </div>
  )
}

export default EditFileRequests