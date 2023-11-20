import React from 'react'
import { Link } from 'react-router-dom'


export const FileRequestItem = ({file, id}) => {
  return (
    <>
        <p>{file.title}</p>
        <Link to={`/edit-file-request/${id}`} >
          <button>EDIT</button>
        </Link>
        <Link to='/open-file-requests/'>
          <button>SEND EMAIL</button>
        </Link>
    </>
  )
}

export default FileRequestItem