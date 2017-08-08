import React from 'react';
import ReactDOM from 'react-dom';
import {
	BrowserRouter as Router,
	Route,
	Link
} from 'react-router-dom';
import { EventsList } from './list';

function renderEventsList({ match }) {
	if ( match.url === "/unfinished" ){
		var status = "?status=false"
	} else if ( match.url === "/finished" ) {
		var status = "?status=true"
	} else {
		var status = ""
	}
	return <EventsList url={`/api/events/${status}`} />;
}


class NavBar extends React.Component {
	render() {
		return(
			<Router>
				<div>
					<Link to='/unfinished'><button>Todo</button></Link>
					<Link to='/finished'><button>Completed</button></Link>
					<Link to='/all'><button>All</button></Link>
					
					<Route exact path="/unfinished" render={ renderEventsList } />
					<Route exact path="/finished" render={ renderEventsList } />
					<Route exact path="/all" render={ renderEventsList } />
				</div>
			</Router>
		);
	}
}

ReactDOM.render(
	<NavBar />,
	document.getElementById('test')
);