import './App.css';
import EditFileRequests from './pages/EditFileRequests';
import ListFileRequests from './pages/ListFileRequests'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'


function App() {
  return (
    <Router>
      {/* <div className="App"> */}
        <Routes>
          <Route index path='/' element={ <ListFileRequests /> } />
          <Route path='/edit-file-request/:id' element={ <EditFileRequests/> } />
        </Routes>
      {/* </div> */}
    </Router>
  );
}

export default App;
