import {Link} from "react-router-dom";


export const Wrapper = props => {
    return <>
        <header className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
            <button className="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">INVENTARY</button>

            <div className="navbar-nav">
                <div className="nav-item text-nowrap">
                    <button className="nav-link px-3" href="#">Sign out</button>
                </div>
            </div>
        </header>

        <div className="container-fluid">
            <div className="row">
                <nav id="sidebarMenu" className="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
                    <div className="position-sticky pt-3">
                        <ul className="nav flex-column">
                            <li className="nav-item">
                                <Link to={`/`} className="nav-link active" aria-current="page" >
                                    Products
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link to={`/ordersList`} className="nav-link active" aria-current="page" >
                                    Orders
                                </Link>
                            </li>
                        </ul>
                    </div>
                </nav>

                <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    {props.children}
                </main>
            </div>
        </div>
    </>
}