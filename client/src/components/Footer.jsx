import { Link } from 'react-router-dom';
import routes from '../assets/routes.json';
import '../styles/Footer.component.css';

export default function Footer() {
  return (
    <footer className='footer'>
      <nav className='nav-footer'>
        {routes.map((route) => {
          return (
            <Link
              to={route.to}
              className={`nav-footer__link${route.internal ? ' external' : ''}`}
              key={route.label}
            >
              {route.label}
              {route.external ? (
                <span className='nav-footer__link-arrow-icon'>
                  <IoIosArrowRoundForward />
                </span>
              ) : (
                <></>
              )}
            </Link>
          );
        })}
      </nav>
      <div className='footer__sub-footer'></div>
    </footer>
  );
}
