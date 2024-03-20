import {Route, Routes} from 'react-router-dom'
import './App.css';
import Header from './component/Header';
import Login from './component/Login';
import Products from './component/Products';
import Registration from './component/Registration';
import Cart from './component/Сart';
import Order from './component/Order';
function App() {
  return (
    <div className="App">
      <>
      <Header/>
      <Routes>
        <Route path='/' element={<Products />} />
        <Route path='/login' element={<Login />} />
        <Route path='/cart' element={<Cart />} />
        <Route path='/order' element={<Order />} />
        <Route path='/reg' element={<Registration />} />

      </Routes>
      </>

    </div>
  );
}

export default App;
