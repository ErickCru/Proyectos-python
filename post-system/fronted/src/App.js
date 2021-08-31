import './App.css';
import {useState, useEffect} from 'react';
import axios from 'axios';
import PostList from './components/post-list';

const url = "http://localhost:8000/api/posts/"

function App() {
  const [posts, setPost] = useState([])

  useEffect(() => {
   fetchData()
  },[]);

  const fetchData = () => {
    axios.get(url)
    .then(res => {
      setPost(res.data);
    })
    .catch(err => console.log(err))
  };

  const handleSendTasks = () => {
    const data = {
      title: 'test title',
      description: 'test description',
      author: 'alonzo'
    };

    axios.post(url, data)
    .then( res => {
      const newData = [...posts, res.data]
      setPost(newData)
    })
    .catch(err => console.log(err))
  }

  return (
    <div className="App">
     <p>Hello World</p>
     <button onClick={handleSendTasks}>Send task</button>
     <hr />
     <PostList data={posts}/>
    </div>
  );
}

export default App;
