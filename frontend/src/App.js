import {useState} from 'react'
import './App.css';
import axios from 'axios'

function App() {
  const [data,setData]=useState('')
  const url='http://127.0.0.1:5000';

  axios.get(url)
  .then(response=>{
    setData(response.data)
  }).catch(error=>{
    console.log(error)
  })
  return (
    <div className="App">
     Data fetched from backend flask server is: {data}
    </div>
  );
}

export default App;
