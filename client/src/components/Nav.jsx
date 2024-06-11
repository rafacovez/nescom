import routes from '../assets/routes.json';
import '../styles/Nav.component.css';
import { IoIosArrowRoundForward } from 'react-icons/io';
import { Link } from 'react-router-dom';
import { useState } from 'react';

export default function Nav() {
  const [isNavOpened, setIsNavOpened] = useState(false);

  return (
    <>
      <div
        role='button'
        onClick={() => {
          setIsNavOpened(!isNavOpened);
        }}
        className='header__burger-menu'
      >
        <span className='header__burger-menu-bars'></span>
      </div>
      <nav
        aria-expanded={isNavOpened ? 'true' : 'false'}
        className={`nav-header${isNavOpened ? ' active' : ''}`}
      >
        {routes.map((route) => {
          return (
            <Link
              to={route.to}
              className={`nav-header__link${route.internal ? ' external' : ''}`}
              key={route.label}
            >
              {route.label}
              {route.external ? (
                <span className='nav-header__link-arrow-icon'>
                  <IoIosArrowRoundForward />
                </span>
              ) : (
                <></>
              )}
            </Link>
          );
        })}
      </nav>
    </>
  );
}
