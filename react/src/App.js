// Built in
import React from 'react';

// Own made
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Matches from './pages/Matches';
import Collaborators from './pages/Collaborators';
import Chat from './pages/Chat';
import ResourceHub from './pages/ResourceHub';
import Profile from './pages/Profile';
import About from './pages/About';
import Login from './pages/Login';
import SignUp from './pages/Signup';


// Tweaked name
// Third party
import 'bootstrap/dist/css/bootstrap.css';

// Own made
import './styles.css';
import './App.css';
import './index.css';


const App = () => {
  return (
      <Router>
      <Navbar />
      <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/matches' component={Matches} />
          <Route path='/login' component={Login} />
          <Route path='/sign-up' component={SignUp} />
          <Route path='/chat' component={Chat} />
          <Route path='/profile' component={Profile} />
          {/*
          <Route path='/collaborators' component={Collaborators} />
          <Route path='/resource-hub' component={ResourceHub} />
          <Route path='/about' component={About} />
          */}
      </Switch>
      </Router>
  );
}

export default App;