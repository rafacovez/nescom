import { FaChevronDown, FaUser } from 'react-icons/fa';
import { useState } from 'react';
import '../styles/Profile.component.css';

export default function Profile() {
  const [isProfileMenuActive, setIsProfileMenuActive] = useState(false);

  return (
    <div
      role='button'
      onClick={() => {
        setIsProfileMenuActive(!isProfileMenuActive);
      }}
      className='header__profile'
    >
      <div className='profile-photo'>
        <FaUser className='profile-photo__default' />
      </div>
      <FaChevronDown
        className={`profile-icon ${isProfileMenuActive ? 'active' : ''}`}
      />
      <div
        aria-expanded={isProfileMenuActive ? 'true' : 'false'}
        className={`profile-menu ${isProfileMenuActive ? 'active' : ''}`}
      ></div>
    </div>
  );
}
