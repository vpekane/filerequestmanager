import React from 'react'
import Header from './Header'

const EditFileRequestItem = () => {
  return (
    <html>
        <head>
            <title>File request</title>
        </head>
        <body>
            <Header headername="Edit file request" />
            <form>
                <h3>Title</h3>
                <input type="text"></input>
                {/* <input type="text" value={props.file.title} /> */}
                <h3>Description</h3>
                <input type="text"></input>
                {/* <input type="text" value={props.file.description}></input> */}
                <h3>Destination</h3>
                {/* {% if location %} */}
                    {/* <select> */}
                        {/* {% for location in location %} */}
                            {/* <option value="{{ location }}">{{ location }}</option> */}
                        {/* {% endfor %} */}
                    {/* </select> */}
                    {/* {% else %} */}
                        {/* <i>No file directory available</i> */}
                {/* {% endif %} */}
            </form>
        </body>
    </html>
  )
}

export default EditFileRequestItem