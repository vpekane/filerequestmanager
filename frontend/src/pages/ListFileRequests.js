import React, {useEffect, useState} from 'react'
import Header from '../components/Header';
import FileRequestItem from '../components/FileRequestItem'

const ListFileRequests = () => {

    let [requests, setRequests] = useState([])

    useEffect(() => {
        getRequests()
    }, [])

    let getRequests = async () => {
        let response = await fetch('/file-requests/')
        let data = await response.json()

        setRequests(data["files"])
        // console.log(data['files'])
    }

  return (
    <div>
      <Header headername="Open file requests" />
      {requests.map((file, index) => (
        <FileRequestItem key={index} file={file} id={file.id}/>
      ))}
    </div>
  )
}

export default ListFileRequests