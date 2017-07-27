var React = require('react')
var ReactDOM = require('react-dom')

var EventsList = React.createClass({
    loadEventsFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data.results});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadEventsFromServer();
        setInterval(this.loadEventsFromServer,
                    this.props.pollInterval)
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var eventNodes = this.state.data.map(function(event){
                return <li> {event.title} </li>
            })
        }

        return (
            <div>
                <h1>以下是由 React 生成的数据</h1>
                <ul>
                    {eventNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<EventsList url='/api/events' pollInterval={1000} />,
    document.getElementById('events'))