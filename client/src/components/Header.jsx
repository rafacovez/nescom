import Image from './Image';
import Nav from './Nav';
import Profile from './Profile';
import logo from '../assets/logo.png';
import '../styles/Header.component.css';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className='header'>
      <Link to='/' className='header__logo'>
        <Image src={logo} alt='Nescom' />
        <h1 className='header__heading'>Nescom</h1>
      </Link>
      <div className='header__utilities'>
        <Profile />
        <Nav />
      </div>
    </header>
  );
}
