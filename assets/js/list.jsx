import React from 'react';
import ReactDOM from 'react-dom';
import {
	BrowserRouter as Router,
	Route,
	Link
} from 'react-router-dom';


export class EventsList extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			data: []
		}
	}
	
	loadData() {
		$.ajax({
			url: this.props.url,
			datatype: 'json',
			cache: false,
			success: function(data) {
				this.setState({
					data: data.results
				});
			}.bind(this)
		});
	}
	
	componentDidMount() {
		console.log(this.props.url);
		this.loadData();
//		setInterval(this.loadData,
//				   this.props.pollInterval);
	}
	
	render() {
		if (this.state.data) {
			var eventNodes = 
				this.state.data.map( ( event ) => {					
					return (
						<li key={event.id}>
							<Link to={`/events/${ event.id }`}>{ event.title }</Link>
						</li>
					);
				});
		}
		
		return (
			<Router>
				<div>
					<ol>{eventNodes}</ol>
					<Route path="/events/:id"
						render={({ match }) => <EventText id={ match.params.id } events={ this.state.data }/>}/>
				</div>
			</Router>
		);
	}
}


class EventText extends React.Component {	
	render() {
		var id = this.props.id;
		var events = this.props.events;
		var eventText = events.find( e => e.id == id)['text'];
		return(<p>{ eventText }</p>);
	}
}

//ReactDOM.render(
//	<EventsList url='/api/events' pollInterval={10000} />,
//	document.getElementById('events')
//);
