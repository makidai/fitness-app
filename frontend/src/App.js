import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./pages";
import NotFoundPage from "./pages/404";
import SigninPage from "./pages/signin";
import BlogPage from "./pages/blog";

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/signin" component={SigninPage} exact />
                <Route path="/blog" component={BlogPage} exact />
                <Route component={NotFoundPage} />
            </Switch>
        </Router>
    );
}

export default App;
