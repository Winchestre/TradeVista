import PropTypes from 'prop-types';
import Navbar from '../Navbar/Navbar';

export default function Mainlayout({ children }) {
    return (
        <>
            <Navbar />
            <div>
                {children}
            </div>
        </>
    )
};
Mainlayout.PropTypes = {
    children: PropTypes.node.isRequired,
};